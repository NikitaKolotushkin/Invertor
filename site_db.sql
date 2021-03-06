CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR (64) NOT NULL UNIQUE,
    email VARCHAR (120) NOT NULL UNIQUE,
    phone VARCHAR (32) NOT NULL,
    password_hash VARCHAR (256),
    time INTEGER NOT NULL
);

-- CREATE TABLE IF NOT EXISTS Items (
--     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
--     cabinet INTEGER NOT NULL,
--     inv_no VARCHAR (64) NOT NULL,
--     name VARCHAR (128) NOT NULL,
--     time INTEGER NOT NULL
-- );

CREATE TABLE IF NOT EXISTS Items (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    cabinet INTEGER,
    floor_ INTEGER,
    status_ BOOLEAN NOT NULL,
    type_ VARCHAR (64),
    model VARCHAR (128),
    inv_no VARCHAR (128) NOT NULL,
    worker VARCHAR (256),
    phone VARCHAR (32),
    email VARCHAR (64),
    comment TEXT,
    picture VARBINARY (8000),
    time_ INTEGER NOT NULL
);