# Ajspire Technologies Pvt. Ltd. — Flask Demo Website

A simple multi-page Flask website with:

- Bootstrap 5 responsive design
- Home, About, Services and Contact pages
- Contact form
- SQLite database for contact enquiries
- Admin login
- Admin dashboard to view enquiries

## 1. Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 2. Run

```powershell
python app.py
```

Open:

http://127.0.0.1:5000

## 3. Admin

Open:

http://127.0.0.1:5000/admin/login

Demo credentials:

- Username: admin
- Password: admin123

Change these credentials before production.

## 4. Database

SQLite database is automatically created at:

`instance/ajspire.db`

The contact form stores:

- Name
- Email
- Phone
- Message
- Created date

## 5. GitHub

```powershell
git init
git add .
git commit -m "Initial Ajspire Flask website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ajspire-flask-website.git
git push -u origin main
```

## 6. Important Vercel note

SQLite is suitable for local development/demo use. Vercel's serverless environment does not provide persistent local SQLite storage for production writes. For a real Vercel deployment, use a hosted database such as PostgreSQL or another supported external database.

Also set a strong secret key and store admin credentials in environment variables before production.
