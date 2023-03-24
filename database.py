from flask import g
import sqlite3
import os

def connect_db():
    path = os.getcwd()
    data_path=os.path.join(path,"questions.db")
    print(data_path)
    #sql = sqlite3.connect('/home/maniac/workspace/flask-food-app/left_join/food_log.db')
    sql = sqlite3.connect(data_path)
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
    
def init_db():
    db = connect_db()

    db[1].execute(open('schema.sql', 'r').read())
    db[1].close()

    db[0].close()

def init_admin():
    db = connect_db()

    db[1].execute('update users set admin = True where name = %s', ('admin', ))

    db[1].close()
    db[0].close()
