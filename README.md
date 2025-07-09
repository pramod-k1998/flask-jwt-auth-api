# flask-jwt-auth-api
# 🔐 Flask JWT Auth API

A lightweight and modular **Flask REST API** boilerplate featuring **JWT-based Authentication**, built using best practices like:

- ✅ App Factory Pattern
- ✅ Blueprints for modular routing
- ✅ SQLAlchemy + Flask-Migrate for ORM & DB migrations
- ✅ Secure password hashing
- ✅ JWT access token authentication

---

## 📁 Project Structure

flask-jwt-auth-api/
├── app/
│ ├── init.py # App factory
│ ├── config.py # Config class
│ ├── extensions.py # db, migrate, jwt setup
│ ├── models.py # User model
│ └── routes/ # Blueprints (auth, main)
│ ├── init.py
│ ├── auth.py
│ └── main.py
├── migrations/ # Flask-Migrate folder
├── .env # Environment variables
├── run.py # App entry point
└── requirements.txt # Dependencies



---

## ⚙️ Tech Stack

- **Flask** – micro web framework
- **SQLAlchemy** – ORM
- **Flask-Migrate** – DB migrations
- **Flask-JWT-Extended** – JWT Auth
- **Werkzeug** – password hashing
- **python-dotenv** – load environment variables

---

## 🚀 Getting Started

### 📌 1. Clone the repo

```bash
git clone https://github.com/pramod-k1998/flask-jwt-auth-api.git
cd flask-jwt-auth-api
```
**2. Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
**3. Install dependencies**
```bash
pip install -r requirements.txt
```

 **4. Configure environment variables**
 ```bash
SECRET_KEY=your-secret
JWT_SECRET_KEY=your-jwt-secret
DATABASE_URL=sqlite:///app.db
```

 **5. Set up the database**
 ```bash
flask db init
flask db migrate
flask db upgrade
```

** 6. Run the server**
```bash
python run.py
```

🔐 API Endpoints
✅ 1. Register User
POST /auth/register

Request Body:

{
  "username": "user123",
  "password": "secure123"
}

Response:
{
  "message": "User registered"
}

✅ 2. Login
POST /auth/login

Request Body:
{
  "username": "user123",
  "password": "secure123"
}

Response:
{
  "access_token": "your_jwt_token"
}

✅ 3. Protected Route
GET /

Headers:
Authorization: Bearer <access_token>

Response:
{
  "message": "Welcome to the protected home page!"
}



🙌 Author
Pramod K
GitHub: @pramod-k1998

