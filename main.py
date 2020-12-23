#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask


app = Flask("Inventory Controller")

@app.route("/")
def hello():
    return "Hello, world!"
