#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import abort, render_template, flash, redirect, url_for, request, session
from app import app

import os


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if len(request.form['password']) > 3 and request.form['password'] == request.form['password_confirm']:
            flash('Успех!', category='success')
        elif len(request.form['password']) < 4:
            flash('Пароль слишком короткий!', category='error')
        elif request.form['password'] != request.form['password_confirm']:
            flash('Пароли не совпадают!', category='error')
        else:
            flash('Ошибка отправки!', category='error')

    if 'userLogged' in session:
        return redirect(url_for('cabinet', login=session['userLogged']))
    elif request.method == 'POST' and request.form['login'] == 'Rensys' and request.form['password'] == '1234':
        session['userLogged'] = request.form['login']
        return redirect(url_for('cabinet', login=session['userLogged']))

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('cabinet', login=session['userLogged']))
    elif request.method == 'POST' and request.form['login'] == 'Rensys' and request.form['password'] == '1234':
        session['userLogged'] = request.form['login']
        return redirect(url_for('cabinet', login=session['userLogged']))

    return render_template('login.html')


@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

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