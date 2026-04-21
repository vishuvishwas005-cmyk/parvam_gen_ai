# Simple Flask + SQLAlchemy CRUD Example

Files created:

- `app.py` - Flask app, SQLAlchemy setup, and CRUD routes
- `templates/index.html` - List users view
- `templates/add.html` - Add user form
- `templates/edit.html` - Edit user form
- `requirements.txt` - Python dependencies

Run locally:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

This app uses SQLite and will create `users.db` automatically.
