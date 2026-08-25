from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import init_db, add_contact, get_contacts

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key-in-production"

# Demo admin credentials — change these before production
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in all required fields.", "danger")
            return render_template("contact.html")

        add_contact(name, email, phone, message)
        flash("Thank you! Your message has been submitted successfully.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if session.get("admin_logged_in"):
        return redirect(url_for("admin_dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect(url_for("admin_dashboard"))

        flash("Invalid username or password.", "danger")

    return render_template("admin/login.html")


@app.route("/admin")
def admin_dashboard():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    contacts = get_contacts()
    return render_template("admin/dashboard.html", contacts=contacts)


@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))


if __name__ == "__main__":
    app.run(debug=True)
