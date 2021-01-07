#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import g
from flask_login import LoginManager
import sqlite3

from app import app, db
from app.FDataBase import FDataBase
from app.UserLogin import UserLogin


def connect_db():
    '''
    Функция для подключения к базе данных
    '''
    conn = sqlite3.connect('invertor.db')
    conn.row_factory = sqlite3.Row

    return conn


def create_db():
    '''
    Функция для создания таблиц Базы Данных
    '''
    db = connect_db()
    with app.open_resource('../site_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    db.commit()
    db.close()


def get_db():
    '''
    Установление соединения с Базой Данных, в случае, если оно ещё не установлено
    '''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None
@app.before_request
def before_request():
    '''
    Установление соединения с Базой данных ПЕРЕД выполнением запроса
    '''
    global dbase
    db = get_db()
    dbase = FDataBase(db)


# @app.teardown_appcontext
def close_db():
    '''
    Разрыв соединения с базой данных, в случае, если оно установлено
    '''
    if hasattr(g, 'link_db'):
        g.link_db.close()
        

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Пожалуйста, авторизуйтесь'
login_manager.login_message_category = 'success'

@login_manager.user_loader
def load_user(user_id):
    print('load_user')
    return UserLogin().fromDB(user_id, dbase)