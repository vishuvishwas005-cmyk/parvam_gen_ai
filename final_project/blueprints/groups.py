import random
import string
from flask import Blueprint, request, redirect, url_for, session, flash, render_template
from database import get_db_connection

groups_bp = Blueprint('groups', __name__)

def generate_invite_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@groups_bp.route('/create', methods=['POST'])
def create_group():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    group_name = request.form.get('group_name')
    owner_id = session['user_id']
    invite_code = generate_invite_code()
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # 1. Create Group
        cursor.execute(
            "INSERT INTO shared_groups (name, owner_id, invite_code) VALUES (?, ?, ?)",
            (group_name, owner_id, invite_code)
        )
        group_id = cursor.lastrowid
        
        # 2. Add owner as member
        cursor.execute(
            "INSERT INTO group_memberships (user_id, group_id) VALUES (?, ?)",
            (owner_id, group_id)
        )
        conn.commit()
        flash(f'Collaborative Vault "{group_name}" created! Code: {invite_code}', 'success')
    except Exception as e:
        conn.rollback()
        flash('Failed to create group. Please try again.', 'danger')
    finally:
        conn.close()
        
    return redirect(url_for('contacts.dashboard'))

@groups_bp.route('/join', methods=['POST'])
def join_group():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    invite_code = request.form.get('invite_code').upper().strip()
    user_id = session['user_id']
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # 1. Find Group
        cursor.execute("SELECT id, name FROM shared_groups WHERE invite_code = ?", (invite_code,))
        group = cursor.fetchone()
        
        if not group:
            flash('Invalid invite code.', 'danger')
            return redirect(url_for('contacts.dashboard'))
        
        # 2. Join Group
        cursor.execute(
            "INSERT OR IGNORE INTO group_memberships (user_id, group_id) VALUES (?, ?)",
            (user_id, group['id'])
        )
        conn.commit()
        flash(f'Joined collaborative vault: {group["name"]}!', 'success')
    finally:
        conn.close()
        
    return redirect(url_for('contacts.dashboard'))
