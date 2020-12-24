#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, redirect, current_app
from flask_sqlalchemy import SQLAlchemy

import logging


app = Flask("Inventory Controller")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/users'
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
