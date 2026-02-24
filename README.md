# 📝 Django Notes Taking App

A simple and secure Notes Taking Web Application built using **Django**.  
Users can register, log in, create notes, edit them, and manage their personal notes efficiently.

---

## 🚀 Features

- User Registration & Login Authentication
- Create Notes
- Edit Existing Notes
- Delete Notes
- View Personal Notes Dashboard
- Secure User-based Data Access
- Responsive UI with CSS styling
- Logout functionality

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite3
- **Authentication:** Django Built-in Authentication System
- **Version Control:** Git & GitHub

---

## 📂 Project Structure
notes_project/
│
├── notes/ # Main app
│ ├── migrations/
│ ├── templates/
│ │ ├── notes/
│ │ └── registration/
│ ├── static/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── notes_project/
│ ├── settings.py
│ ├── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/notes-app.git
cd notes-app
2️⃣ Create Virtual Environment
python -m venv myenv
source myenv/bin/activate     # Linux/Mac
myenv\Scripts\activate        # Windows
3️⃣ Install Dependencies
pip install django
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Create Superuser (Optional)
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver

Open browser:

http://127.0.0.1:8000/
🔐 Authentication

The app uses Django’s built-in authentication system:

User Registration

Login

Logout

Session-based authentication

User-specific notes visibility
