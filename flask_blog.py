#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:17:32 2020

@author: shintaromasuno
"""

import flask

from flask import Flask, render_template, url_for
from forms  import RegistrationForm, LoginForm
app = Flask(__name__)

posts = [
        {
                'author': 'Shintaro Masuno',
                'title': 'Blog Post 1',
                'content': 'First post content',
                'date_posted': 'March 11, 2020'
                },
        {
                'author': 'Shintaro Masuno',
                'title': 'Blog Post 2',
                'content': 'Second post content',
                'date_posted': 'March 9, 2020'
                }
        ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
    
