#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for
from app import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/cabinet', methods=['GET', 'POST'])
def cabinet():
    return render_template('cabinet.html')


@app.route('/tables', methods=['GET', 'POST'])
def tables():
    pass
