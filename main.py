#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, redirect, current_app, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

import logging


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/cabinet")
def cabinet():
    pass


@app.route("/tables")
def tables():
    pass

