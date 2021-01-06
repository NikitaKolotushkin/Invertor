#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sqlite3
import time


class FDataBase:

    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def addUser(self, login, email, phone, password_hash):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM Users WHERE email like '{email}'")
            result = self.__cur.fetchone()
            if result['count'] > 0:
                print('Пользователь с таким email уже существует!')
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO Users VALUES(NULL, ?, ?, ?, ?, ?)", (login, email, phone, password_hash, tm))
            self.__db.commit()

        except sqlite3.Error as e:
            print('Ошибка добавления пользователя в базу данных:' + str(e))
            return False
        
        return True