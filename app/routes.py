#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import abort, render_template, flash, redirect, url_for, request, session
from flask_login import LoginManager
import os
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, login_manager
from app.models import *
from app.FDataBase import FDataBase


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    dbase = FDataBase(get_db())

    if request.method == 'POST':
        if len(request.form['login']) > 3 and len(request.form['password']) > 4 \
            and len(request.form['email']) > 4 \
            and request.form['password'] == request.form['password_confirm']:
            password_hash = generate_password_hash(request.form['password'])
            result = dbase.addUser(request.form['login'], request.form['email'], request.form['phone'], password_hash)
            if result:
                flash('Вы успешно зарегистрировались!', 'success')
                return redirect(url_for('login'))
            else:
                flash('Ошибка при выполнении запроса к базе данных!', 'error')    
        else:
            flash('Ошибка заполнения!', 'error')

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

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
@app.errorhandler(401)
def Unauthorized(error):
    return render_template('unauthorized.html'), 401


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404