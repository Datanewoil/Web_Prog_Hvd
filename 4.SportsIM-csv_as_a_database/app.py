import csv
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods = ['POST'])
def register():
    name = request.form.get('name')
    dorm = request.form.get('dorm')
    if not name or not dorm:
        return render_template('failure.html')
    file = open("registered.csv", "a")          #hey python open this csv file in "a"/append mode. so that we can add the entries
    writer = csv.writer(file)
    writer.writerow((name, dorm))
    file.close()
    return render_template("success.html")


@app.route('/registered')
def registered():
    # file = open("registered.csv", "r")
    # reader = csv.reader(file)
    # students = list(reader)
    # file.close()

    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)

    return render_template('registered.html', students = students)