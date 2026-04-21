# Student CRUD Operations

A Flask web application for managing student records with Create, Read, Update, and Delete operations.

## Features

- Add new students
- View all students
- Edit student information
- Delete students
- SQLite database for data persistence
- Responsive web interface

## Installation

1. Install the required packages:
```bash
pip install flask
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and go to `http://localhost:5000`

## Database Schema

The application uses SQLite with a `students` table containing:
- id (Primary Key)
- name (Text, Required)
- email (Text, Unique, Required)
- age (Integer)
- grade (Text)
- created_at (Timestamp)

## API Endpoints

- `GET /` - List all students
- `GET/POST /add` - Add new student
- `GET/POST /edit/<id>` - Edit student
- `POST /delete/<id>` - Delete student

## Technologies Used

- Flask
- SQLite
- HTML/CSS/JavaScript
- Bootstrap (via CDN)