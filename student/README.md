# Student Management System

This project is a Student Management System built using Django and Flask. The Django project handles the main application, while a Flask API is used to manage student data using SQLite and Faker library.

## Project Structure

## Requirements

- Python 3.x
- Django
- Flask
- Faker

## Installation

### Step 1: Clone the repository

```sh
git clone <repository_url>
cd student_django
```


### Step 2: Create Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

```sh
pip install django flask faker
```

## Run the Flask API

### Step 1 : Navigate to the Flask API directory
```sh
cd student/student_data_flask
```

### Step 2: Run the Flask API

```sh
python student_sqlite_api.py
```

## Running the Django Project

### Step 1: Navigate to the Django project directory

```sh
cd student
```

### Step 2: Apply migrations

```sh
python manage.py migrate
```

### Step 3: Run the Django development server

```sh
python manage.py runserver
```

## URLs
- Student List: /
- Add Student: /add/
- Edit Student: /edit/<int:pk>/
- Delete Student: /delete/<int:pk>/

### All URLs are directed using buttons in the application.

- **Notes**

- Ensure the Flask API is running before starting the Django project.
- The Flask API uses the Faker library to generate fake student data.
