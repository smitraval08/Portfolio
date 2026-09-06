from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.secret_key = os.getenv(
    "SECRET_KEY",
    "change-this-secret-key"
)


def get_db():
    import mysql.connector

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", "3306"))
    )


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/contact")
def contact():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:

        flash(
            "Please fill in your name, email and message.",
            "error"
        )

        return redirect(
            url_for("home") + "#contact"
        )

    conn = None
    cursor = None

    try:

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO contact_messages
            (name, email, subject, message, created_at)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                name,
                email,
                subject,
                message,
                datetime.now()
            )
        )

        conn.commit()

        flash(
            "Message sent successfully. Thank you!",
            "success"
        )

    except Exception as exc:

        app.logger.exception(
            "Database error: %s",
            exc
        )

        flash(
            "Message could not be sent right now. Please use email instead.",
            "error"
        )

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

    return redirect(
        url_for("home") + "#contact"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=True
    )
