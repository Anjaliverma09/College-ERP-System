# 🎓 College ERP System

### Enterprise Resource Planning Solution for Educational Institutions

![GitHub stars](https://img.shields.io/github/stars/username/repo?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/django-framework-green?style=for-the-badge&logo=django)
![License](https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge)

---

## 📋 Table of Contents

* [About](#-about)
* [Features](#-features)
* [Demo Credentials](#login-details)
* [Technology Stack](#-technology-stack)
* [Installation](#️-installation-and-setup--prerequisites)

---

## 🎯 About

**College ERP** is a comprehensive Enterprise Resource Planning system designed specifically for educational institutions. Built with Python and Django, this full-stack web application streamlines administrative tasks, student management, and staff operations in one unified platform.

### ✨ Why Choose This ERP?
* 🚀 **Modern Tech Stack** - Built with Django for robust performance
* 📊 **Data-Driven Insights** - Visual dashboards for performance tracking
* 👥 **Multi-Role Support** - Separate interfaces for Admin, Staff, and Students
* 🔒 **Secure** - Role-based access control and authentication
* 📱 **Responsive Design** - Works seamlessly on all devices

---

## 🚀 Features

### 👨‍💼 Admin Dashboard
<details>
  <summary>Click to expand Admin features</summary>
  </details>

### 👩‍🏫 Staff Portal
<details>
  <summary>Click to expand Staff features</summary>
  </details>

### 🎓 Student Portal
<details>
  <summary>Click to expand Student features</summary>
  </details>

---

### Login Details

| Role | Email | Password |
| :--- | :--- | :--- |
| 🎓 Student | `studentone@student.com` | `studentone` |
| 👩‍🏫 Staff | `staffone@staff.com` | `staffone` |

---

## 🛠 Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | Python, Django Framework |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap |
| **Database** | SQLite (Development), PostgreSQL (Production Ready) |
| **Authentication** | Django Auth, Google reCAPTCHA |
| **Deployment** | PythonAnywhere |

---

⚙️ Installation and Setup
📌 Prerequisites

Install the following:

🐍 Python

📦 Pip

🔧 Git

## Step-by-Step Setup

### 1️⃣ Clone the Repository

git clone https://github.com/Anjaliverma09/College-ERP-System.git

cd College-ERP-System


---

### 2️⃣ Create Virtual Environment

#### Option A: Using Conda (Recommended)


conda env create -f college-erp.yml
conda activate Django-env


#### Option B: Using venv

▶ **Windows**


python -m venv venv
venv\Scripts\activate


▶ **macOS**
python3 -m venv venv
source venv/bin/activate


▶ **Linux**


python3 -m venv venv
source venv/bin/activate


---

### 3️⃣ Install Dependencies


pip install -r requirements.txt


---

### 4️⃣ Run Database Migrations


python manage.py migrate


---

### 5️⃣ Create Superuser


python manage.py createsuperuser


---

### 6️⃣ Run the Development Server


python manage.py runserver


Open in browser:


http://127.0.0.1:8000/
