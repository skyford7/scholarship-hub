"""
Simple Flask application for a scholarship application website.

This app provides two main parts:

1. Applicant-facing form at the root URL (`/`). Applicants can submit
   their name, email, phone number and a short description about
   themselves. Upon submission, the data is appended to a JSON file
   (`applications.json`) stored in the same folder as the app. A
   confirmation page lets the applicant know the submission was
   successful.

2. Administrator interface. Administrators can log in at `/login`
   using hard‑coded credentials (defined below) and view all
   applications at `/admin`. Admin sessions are stored in Flask’s
   session, so logging out simply clears the session and redirects
   back to the login page.

The goal of this code is to provide a minimal, easy‑to‑understand
scholarship portal that can be run without complex setup. It uses
no database—submissions are persisted in a JSON file. For a more
robust solution, consider using a database engine such as SQLite
or MySQL and adding user management.
"""

from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)

# Change this secret key for production. It is used to sign session cookies.
app.secret_key = "super_secret_key"

# Hard‑coded administrator credentials. In a real system you would
# store these securely (e.g. in a database with hashed passwords).
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "password"

# File where applications will be stored. This file will be created if it
# does not exist. It is kept in the same folder as this script.
DATA_FILE = os.path.join(os.path.dirname(__file__), "applications.json")


def load_applications() -> list:
    """Load applications from the JSON file. Returns an empty list if
    the file does not exist or cannot be parsed."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # If the file is corrupted or unreadable, start fresh
        return []


def save_applications(applications: list) -> None:
    """Persist applications to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(applications, f, indent=4, ensure_ascii=False)


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the applicant form or handle form submission."""
    if request.method == "POST":
        # Retrieve form fields. Strip whitespace to avoid leading/trailing
        # spaces. Basic validation—fields are required via the HTML form.
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        description = request.form.get("description", "").strip()

        # Build an application record
        application = {
            "name": name,
            "email": email,
            "phone": phone,
            "description": description,
        }

        # Append to existing applications and save to disk
        applications = load_applications()
        applications.append(application)
        save_applications(applications)

        # Render a success page, passing the applicant’s name
        return render_template("success.html", name=name)

    # GET request—render the empty form
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Display and handle the admin login form."""
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        # Check credentials. Both email and password must match the
        # configured admin credentials.
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect(url_for("admin"))
        else:
            # Show the form again with an error message
            return render_template("login.html", error="Invalid credentials")

    # GET request—render the login form
    return render_template("login.html")


@app.route("/admin")
def admin():
    """Protected admin dashboard showing all applications."""
    if not session.get("admin_logged_in"):
        # If not logged in, redirect to login page
        return redirect(url_for("login"))

    applications = load_applications()
    return render_template("admin.html", applications=applications)


@app.route("/logout")
def logout():
    """Log the administrator out and redirect to login."""
    session.pop("admin_logged_in", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
       port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

