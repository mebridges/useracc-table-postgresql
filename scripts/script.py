# -*- coding: utf-8 -*-
"""
Created on Wed May 28 16:46:08 2025

@author: marye
"""


    
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv(dotenv_path=".env")

try:
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()

    # Insert data
    insert_query = '''
    INSERT INTO useracc (userid, name, surname, birthday, gender, email, pwd)
    VALUES 
    ('U001', 'Alice', 'Smith', '1990-01-01', 'F', 'alice@example.com', 'pass123'),
    ('U002', 'Bob', 'Jones', '1988-05-10', 'M', 'bob@example.com', 'secure456');
    '''
    cur.execute(insert_query)
    conn.commit()
    print("Sample data inserted successfully.")

    # Query data
    cur.execute("SELECT * FROM useracc;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

except Exception as e:
    print("Database operation failed.")
    print(e)
