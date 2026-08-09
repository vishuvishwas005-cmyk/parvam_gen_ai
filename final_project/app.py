from flask import Flask, render_template
import os
from blueprints.auth import auth_bp
from blueprints.contacts import contacts_bp
from blueprints.groups import groups_bp
from database import init_db

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'cms-demo-secret-key-2026-stable')

# Initialize SQLite Database
init_db()

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(contacts_bp, url_prefix='/dashboard')
app.register_blueprint(groups_bp, url_prefix='/groups')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
