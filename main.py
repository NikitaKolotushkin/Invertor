#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, redirect, current_app, session
from flask_sqlalchemy import SQLAlchemy

import logging


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'a6c4758dde5b04abbcad31ead65f009c0df2ce16'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1234@localhost/'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/cabinet")
def cabinet():
    pass

@app.route("/tables")
def tables():
    pass
