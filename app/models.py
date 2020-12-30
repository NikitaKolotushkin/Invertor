#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(32), nullable=True)

    def __repr__(self):
        return f'Пользователь {self.full_name}'
