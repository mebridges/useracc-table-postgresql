CREATE TABLE USERACC (
    id SERIAL PRIMARY KEY,
    userid TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    birthday DATE,
    gender TEXT,
    email TEXT UNIQUE NOT NULL,
    pwd TEXT NOT NULL
);

select * from USERACC;