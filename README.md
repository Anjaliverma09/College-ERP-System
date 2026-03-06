🎓 College Enterprise Resource Planner

A College ERP (Enterprise Resource Planning) System built using the Django Framework (Python).
This application helps manage interactions between students, staff, and administrators and automates common academic processes within a college environment.

🚀 Features of this Project
👨‍💼 Admin Users Can

📊 View summary charts of:

Students

Staff

Courses

Subjects

Attendance

⚙️ Manage system data

➕ Add Staff

✏️ Update Staff

❌ Delete Staff

➕ Add Students

✏️ Update Students

❌ Delete Students

➕ Add Courses

✏️ Update Courses

❌ Delete Courses

➕ Add Subjects

✏️ Update Subjects

❌ Delete Subjects

📅 Manage Sessions

➕ Add Session

✏️ Update Session

❌ Delete Session

📋 Other admin controls

📊 View student attendance

💬 View student feedback

💬 View staff feedback

✅ Approve / Reject leave requests

👨‍🏫 Staff / Teachers Can

📊 Dashboard showing

Students

Subjects

Leave status

📚 Academic management

📝 Take student attendance

✏️ Update attendance

🎯 Result management

➕ Add student results

✏️ Update student results

📤 Communication

📝 Apply for leave

💬 Send feedback to admin

🎓 Students Can

📊 View dashboard summary

Subjects

Attendance

📚 Academic information

👀 View attendance records

👀 View results

📤 Communication

📝 Apply for leave

💬 Send feedback to admin

⚙️ Installation and Setup
📌 Prerequisites

Install the following:

🐍 Python

📦 Pip

🔧 Git

🛠 Installation Steps
1️⃣ Create Project Folder

Create a folder where you want to store the project.

2️⃣ Create Virtual Environment

Install virtualenv

pip install virtualenv

Create environment

Windows

python -m venv venv

Mac / Linux

python3 -m venv venv

Activate environment

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Database Migrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Development Server
python manage.py runserver

Open browser

http://127.0.0.1:8000/
🧩 Main Modules

🔐 Authentication System

👨‍💼 Admin Dashboard

👨‍🏫 Staff Dashboard

🎓 Student Dashboard

📊 Attendance Management

📝 Result Management

🏖 Leave Management

💬 Feedback System

👤 Profile Management

🛠 Technologies Used
Backend

🐍 Python
🌐 Django

Frontend

🎨 HTML
🎨 CSS
⚡ JavaScript
🎯 Bootstrap
📊 Chart.js
📦 jQuery

Database

🗄 SQLite
🗄 MySQL (optional)
