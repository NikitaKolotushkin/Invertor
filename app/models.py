#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from app import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(32), nullable=True)
    password_hash = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return f'Пользователь {self.full_name}'


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