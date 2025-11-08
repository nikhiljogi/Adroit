import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import csv
from pathlib import Path

# Load environment variables
load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USER = os.getenv("njogi16@gmail.com")
EMAIL_PASS = os.getenv("jryw zfni fyux bqjf")
RECEIVER = os.getenv("RECEIVER_EMAIL")

# Tell Flask your HTML folder is named "template"
app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET", "changeme")

DATA_FILE = Path("contacts.csv")
if not DATA_FILE.exists():
    DATA_FILE.write_text("name,email,subject,message\n")

def send_email(name, email, subject, message):
    msg = EmailMessage()
    msg["Subject"] = f"Contact form: {subject}"
    msg["From"] = EMAIL_USER
    msg["To"] = RECEIVER
    msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

@app.route("/", methods=["GET"])
def home():
    return redirect(url_for("contact"))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not (name and email and subject and message):
            flash("Please fill all fields!", "error")
            return redirect(url_for("contact"))

        with DATA_FILE.open("a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([name, email, subject, message])

        try:
            send_email(name, email, subject, message)
            flash("Message sent successfully!", "success")
        except Exception as e:
            print("Email error:", e)
            flash("Error sending email.", "error")

        return redirect(url_for("contact"))

    return render_template("contactus.html")

if __name__ == "__main__":
    app.run(debug=True)
