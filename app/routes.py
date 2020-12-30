#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for
from app import app


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
