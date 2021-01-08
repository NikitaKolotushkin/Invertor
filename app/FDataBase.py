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

    
    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM Users WHERE id = {user_id} LIMIT 1")
            result = self.__cur.fetchone()
            if not result:
                print('Пользователь не найден')
                return False

            return result

        except sqlite3.Error as e:
            print('Ошибка получения данных из Базы Данных' + str(e))

        return False


    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM Users WHERE email = '{email}' LIMIT 1")
            result = self.__cur.fetchone()
            if not result:
                print('Пользователь с таким адресом не существует')
                return False

            return result

        except sqlite3.Error as e:
            print(f'Ошибка получения данных из Базы Данных' + str(e))

        return False


    def addItem(self, cabinet, inv_no):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM Items WHERE email like '{inv_no}'")
            result = self.__cur.fetchone()
            if result['count'] > 0:
                print('Предмет с таким инвентарным номером уже существует!')
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO Items VALUES(NULL, ?, ?, ?)", (cabinet, inv_no, tm))
            self.__db.commit()

        except sqlite3.Error as e:
            print('Ошибка добавления предмета в базу данных:' + str(e))
            return False

        return True


    def getItem(self, item_id):
        try:
            self.__cur.execute(f"SELECT * FROM Items WHERE id = {item_id} LIMIT 1")
            result = self.__cur.fetchone()
            if not result:
                print('Предмет не найден')
                return False

            return result

        except sqlite3.Error as e:
            print('Ошибка получения данных из Базы Данных' + str(e))

        return False


    def getAllItems(self):
        try:
            self.__cur.execute(f"SELECT * FROM Items")
            result = self.__cur.fetchall()
            if result:
                return result

        except sqlite3.Error as e:
            print('Ошибка чтения данных из Базы Данных' +  str(e))

        return []