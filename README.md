# Simple Scholarship Application Website

This project contains a minimal web application for collecting scholarship applications and allowing an administrator to review them. The app is written in Python using the [Flask](https://flask.palletsprojects.com/) micro‑framework and does not require a separate database—applications are stored in a JSON file.

## Features

* **Applicant form** — A user‑friendly form at the root URL (`/`) collects basic information from applicants (name, email, phone and a short description).
* **Success page** — After submission, applicants are shown a confirmation page.
* **Admin login** — Administrators can log in at `/login` using a predefined username and password. Sessions are stored in secure cookies.
* **Dashboard** — Once logged in, the admin can view all submitted applications on the dashboard at `/admin`. A simple table lists each applicant’s details.
* **Logout** — Admins can end their session via the `/logout` route.

## Getting started

These steps assume you have [Python](https://www.python.org/) installed on your computer.

1. **Install Flask**

   Open a terminal or command prompt and install Flask via pip:

   ```sh
   pip install flask
   ```

2. **Download the project**

   Copy the `scholarship_app` folder somewhere convenient on your machine.

3. **Run the application**

   In the terminal, navigate into the project folder and start the Flask development server:

   ```sh
   cd path/to/scholarship_app
   python app.py
   ```

   You should see output similar to:

   ```
   * Serving Flask app 'app'
   * Debug mode: on
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

4. **Open the site**

   Open a web browser and navigate to `http://127.0.0.1:5000/` to see the scholarship application form.

5. **Admin access**

   To access the admin dashboard, go to `http://127.0.0.1:5000/login` and use these credentials:

   * **Email:** `admin@example.com`
   * **Password:** `password`

   Once logged in, you’ll see all submitted applications. Use the “Logout” link to end the session.

## Customizing

* **Change admin credentials** — In `app.py`, modify the `ADMIN_EMAIL` and `ADMIN_PASSWORD` variables. Remember to restart the server after changing them.
* **Add more fields** — To collect additional information from applicants, edit the form in `templates/index.html` and update the `application` dictionary in `app.py` accordingly. Also update the table headings in `templates/admin.html`.
* **Persisting data** — The current version stores applications in `applications.json`. For more robustness in production, consider integrating a database system like SQLite or MySQL.

## License

This project is provided for educational purposes and does not include a license. Feel free to modify it for your own use.