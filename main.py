#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template


app = Flask("Inventory Controller")

@app.route("/")
def hello():
    return render_template("index.html")
