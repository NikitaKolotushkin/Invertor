#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SECRET_KEY = 'a6c4758dde5b04abbcad31ead65f009c0df2ce16'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'invertor.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
