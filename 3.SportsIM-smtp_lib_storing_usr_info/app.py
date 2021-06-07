import os
import smtplib
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods = ['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    dorm = request.form.get('dorm')
    if not name or not email or not dorm:
        return render_template('failure.html')
    message = "You are registered"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("user_xyz_name@gmail.com", os.getenv("PASSWORD"))
    server.sendmail("proctor_name@gmail.com", email, message)       #from address, to address, message
    return render_template("success.html")