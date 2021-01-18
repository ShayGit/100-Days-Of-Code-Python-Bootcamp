from flask import Flask, render_template, request
import random
from datetime import datetime
import requests
import smtplib

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=posts)

@app.route('/contact', methods=['GET','POST'])
def contact():
    msg_sent = False
    if request.method == 'POST':
        data = request.form
        msg_sent = True
        send_email(data["name"], data["email"], data["phone"], data["message"])
    return render_template("contact.html", msg_sent=msg_sent)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<int:id>')
def post(id):
    for blog_post in posts:
        if blog_post["id"] == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":

    app.run(debug=True)
