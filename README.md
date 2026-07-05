# 🚀 TaskFlow (Django)

A simple task management web application built with **Django**, **HTML**, **CSS**, and **Vanilla JavaScript**.

Users can:

- ➕ Add new tasks
- ✅ Mark tasks as completed
- 🗑 Delete completed tasks
- ⚡ Update the UI instantly using Fetch API (without page refresh)

---

# Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript (Fetch API)

---

# Features

- Add tasks
- Complete tasks
- Delete completed tasks
- Responsive popup for adding tasks
- AJAX communication using Fetch API
- Django ORM
- SQLite database

---

# Project Structure

```
taskflow/
│
├── taskflow/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── db.sqlite3
├── manage.py
└── .gitignore
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/rbalaji-2007/TaskFlow-Django.git
```

Move into the project.

```bash
cd TaskFlow-Django/taskflow
```

---

## 2. Install dependencies

```bash
pip install django
```

or

```bash
pip install -r requirements.txt
```

---

## 3. Apply migrations

```bash
python manage.py migrate
```

---

## 4. Run the development server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

# Database

The project currently uses **SQLite**.

No additional setup is required.

---

# Author

**Vethantha Vel**

Computer Science (AI & ML)

Building software, AI projects, and startups one project at a time.