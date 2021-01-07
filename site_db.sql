CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR (64) NOT NULL UNIQUE,
    email VARCHAR (120) NOT NULL UNIQUE,
    phone VARCHAR (32) NOT NULL,
    password_hash VARCHAR (256),
    time INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Items (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    cabinet INTEGER NOT NULL,
    inv_no VARCHAR (64) NOT NULL,
    time INTEGER NOT NULL
);