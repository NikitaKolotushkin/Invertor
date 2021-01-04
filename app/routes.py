#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import abort, render_template, flash, redirect, url_for, request, session
from app import app

import os


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('cabinet', login=session['userLogged']))
    elif request.method == 'POST' and request.form['login'] == 'Rensys' and request.form['password'] == '123':
        session['userLogged'] = request.form['login']
        return redirect(url_for('cabinet'))

    return render_template('login.html')


@app.route('/main', methods=['GET', 'POST'])
def main():
    # return render_template('main.html')
    if request.method == 'POST':
        return request.form


@app.route('/cabinet/<login>', methods=['GET', 'POST'])
def cabinet(login):
    if 'userLogged' not in session or session['userLogged'] != login:
        abort(401)
    else:
        return render_template('cabinet.html')


@app.route('/tables', methods=['GET', 'POST'])
def tables():
    pass


# ERRORS

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404