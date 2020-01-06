#!/usr/bin/env python3

from flask import Flask, render_template, request
import mysql
# import app_functions

app = Flask(__name__)


def connect_db():
    connection = mysql.connector.connect(
            user='root', password='LoginPass@@11223344',
            host='localhost', database='tiger')
    return connection


def view_messages():
    connection = connect_db()
    message = connection.cursor()
    message.execute("SELECT * FROM tiger.messages")
    view = message.fetchall()
    # for row in view will change after implement of the view_massages.html
    # print(row)
    return view


@app.route('/')
def Home():
    return render_template('Home.html')


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')


@app.route('/log_in', methods=['GET', 'POST'])
# TODO write logic to this function
def log_in():
    if request.method == 'POST':
        return render_template('Home.html')
    return render_template('/sign_up.html')


@app.route('/log_out')
# TODO after seesion will be merge write this function
def log_out():
    return render_template('Home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
