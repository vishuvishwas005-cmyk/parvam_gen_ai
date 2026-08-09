import csv
from io import StringIO
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, Response
from database import get_db_connection

contacts_bp = Blueprint('contacts', __name__)

def get_my_groups(cursor, user_id):
    """Helper to fetch sidebar groups"""
    cursor.execute("""
        SELECT g.* 
        FROM shared_groups g
        JOIN group_memberships m ON g.id = m.group_id
        WHERE m.user_id = ?
    """, (user_id,))
    return cursor.fetchall()

@contacts_bp.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        my_groups = get_my_groups(cursor, user_id)
        
        # Dashboard shows PERSONAL contacts only
        if session.get('role') == 'admin':
            # Admin sees all personal contacts across system
            cursor.execute("""
                SELECT c.*, u.username as owner_name, 'Personal' as vault_name
                FROM contacts c
                JOIN users u ON c.user_id = u.id
                WHERE c.shared_group_id IS NULL
                ORDER BY c.name ASC
            """)
        else:
            cursor.execute("""
                SELECT c.*, u.username as owner_name, 'Personal' as vault_name
                FROM contacts c
                JOIN users u ON c.user_id = u.id
                WHERE c.user_id = ? AND c.shared_group_id IS NULL
                ORDER BY c.name ASC
            """, (user_id,))
        
        contacts = cursor.fetchall()
        
        # Stats for personal dashboard
        cursor.execute("SELECT category, COUNT(*) as count FROM contacts WHERE user_id = ? AND shared_group_id IS NULL GROUP BY category", (user_id,))
        cat_stats = cursor.fetchall()
        
        stats = {
            'total_contacts': len(contacts),
            'cat_stats': cat_stats
        }
    finally:
        conn.close()
        
    return render_template('dashboard.html', contacts=contacts, stats=stats, my_groups=my_groups, active_vault=None, members=[])

@contacts_bp.route('/vault/<int:group_id>')
def view_vault(group_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        my_groups = get_my_groups(cursor, user_id)
        
        # 1. Check membership
        cursor.execute("SELECT * FROM shared_groups WHERE id = ?", (group_id,))
        active_vault = cursor.fetchone()
        
        cursor.execute("SELECT 1 FROM group_memberships WHERE user_id = ? AND group_id = ?", (user_id, group_id))
        is_member = cursor.fetchone()
        
        if not (is_member or session.get('role') == 'admin'):
            flash('Access denied to this vault.', 'danger')
            return redirect(url_for('contacts.dashboard'))

        # 2. Fetch Vault Contacts
        cursor.execute("""
            SELECT c.*, u.username as owner_name, g.name as vault_name
            FROM contacts c
            JOIN users u ON c.user_id = u.id
            JOIN shared_groups g ON c.shared_group_id = g.id
            WHERE c.shared_group_id = ?
            ORDER BY c.name ASC
        """, (group_id,))
        contacts = cursor.fetchall()

        # 3. Fetch Vault Members
        cursor.execute("""
            SELECT u.username
            FROM users u
            JOIN group_memberships m ON u.id = m.user_id
            WHERE m.group_id = ?
            ORDER BY u.username ASC
        """, (group_id,))
        members = cursor.fetchall()

        # 4. Stats for vault
        cursor.execute("SELECT category, COUNT(*) as count FROM contacts WHERE shared_group_id = ? GROUP BY category", (group_id,))
        cat_stats = cursor.fetchall()

        stats = {
            'total_contacts': len(contacts),
            'cat_stats': cat_stats
        }
    finally:
        conn.close()
        
    return render_template('dashboard.html', contacts=contacts, stats=stats, my_groups=my_groups, active_vault=active_vault, members=members)

@contacts_bp.route('/add', methods=['POST'])
def add_contact():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    group = request.form.get('group')
    shared_group_id = request.form.get('shared_group_id')
    if shared_group_id == "" or shared_group_id == "None": shared_group_id = None
    
    user_id = session['user_id']
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (user_id, name, phone, email, category, shared_group_id) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, name, phone, email, group, shared_group_id)
        )
        conn.commit()
        flash('Contact added successfully!', 'success')
    finally:
        conn.close()
        
    if shared_group_id:
        return redirect(url_for('contacts.view_vault', group_id=shared_group_id))
    return redirect(url_for('contacts.dashboard'))

@contacts_bp.route('/edit/<int:id>', methods=['POST'])
def edit_contact(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    group = request.form.get('group')
    shared_group_id = request.form.get('shared_group_id')
    if shared_group_id == "" or shared_group_id == "None": shared_group_id = None
    
    user_id = session['user_id']
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # Security: only allow editing your own contacts (or admin)
        cursor.execute("SELECT shared_group_id, user_id FROM contacts WHERE id = ?", (id,))
        existing = cursor.fetchone()
        if not existing:
            flash('Contact not found.', 'danger')
            return redirect(url_for('contacts.dashboard'))
        if existing['user_id'] != user_id and session.get('role') != 'admin':
            flash('You do not have permission to edit this contact.', 'danger')
            return redirect(url_for('contacts.dashboard'))

        old_shared_id = existing['shared_group_id']
        cursor.execute(
            "UPDATE contacts SET name = ?, phone = ?, email = ?, category = ?, shared_group_id = ? WHERE id = ?",
            (name, phone, email, group, shared_group_id, id)
        )
        conn.commit()
        flash('Contact updated successfully!', 'success')
    finally:
        conn.close()
        
    if shared_group_id:
        return redirect(url_for('contacts.view_vault', group_id=shared_group_id))
    return redirect(url_for('contacts.dashboard'))

@contacts_bp.route('/delete/<int:id>')
def delete_contact(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT shared_group_id FROM contacts WHERE id = ?", (id,))
        contact = cursor.fetchone()
        shared_id = contact['shared_group_id'] if contact else None
        
        cursor.execute("DELETE FROM contacts WHERE id = ?", (id,))
        conn.commit()
        flash('Contact deleted.', 'warning')
    finally:
        conn.close()
        
    if shared_id:
        return redirect(url_for('contacts.view_vault', group_id=shared_id))
    return redirect(url_for('contacts.dashboard'))

@contacts_bp.route('/export')
def export_csv():
    # Keep global export for now or update to context-aware
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name, phone, email, category FROM contacts WHERE user_id = ?", (user_id,))
        results = cursor.fetchall()
        
        si = StringIO()
        cw = csv.writer(si)
        cw.writerow(['Name', 'Phone', 'Email', 'Group'])
        for row in results:
            cw.writerow([row['name'], row['phone'], row['email'], row['category']])
        
        return Response(si.getvalue(), mimetype="text/csv", headers={"Content-disposition": "attachment; filename=my_contacts.csv"})
    finally:
        conn.close()
