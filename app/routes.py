#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import abort, render_template, flash, redirect, url_for, request, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import os
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, login_manager
from app.models import *
from app.FDataBase import FDataBase
from app.UserLogin import UserLogin


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

    if current_user.is_authenticated:
        return redirect(url_for('cabinet'))

    dbase = FDataBase(get_db())

    if request.method == 'POST':
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['password_hash'], request.form['password']):
            UserLogged = UserLogin().create(user)
            remainme = True if request.form.get('remainme') else False
            login_user(UserLogged, remember=remainme)
            return redirect(request.args.get("next") or url_for('cabinet'))

        flash('Введены неверные данные!', 'error')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', 'success')
    return redirect(url_for('login'))


@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    return render_template('main.html')


@app.route('/cabinet')
@login_required
def cabinet():
    return render_template('cabinet.html')


@app.route('/all_items', methods=['GET', 'POST'])
@login_required
def all_items():
    dbase = FDataBase(get_db())
    return render_template('all_items.html', items=dbase.getAllItems())


# ERRORS
@app.errorhandler(401)
def Unauthorized(error):
    return redirect(url_for('login')), 401


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404