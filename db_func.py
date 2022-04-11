import requests
import json
import sqlite3 as sq

# query the db and return all records


def show_all():
    # connect to or create a database
    conn = sq.connect('my_db.db')
    # or to create a db in memory that gets wiped after close
    # conn_temp = sq.connect(':memory:')

    # create a table
    # first create a curser
    curs = conn.cursor()

    # Query the database
    curs.execute("SELECT rowid, * FROM customers")

    data_all = curs.fetchall()

    for item in data_all:
        print(item)

    # commit command to database, pushes curs.execute() to database
    conn.commit()
    # close connection
    conn.close()


# add new record to db
def add_one(first, last, email):
    conn = sq.connect('my_db.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # commit our command
    conn.commit()
    # close out connection
    conn.close()


# add many records to db
def add_many(list):
    conn = sq.connect('my_db.db')
    curs = conn.cursor()
    curs.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    # commit our command
    conn.commit()
    # close out connection
    conn.close()


# delete record from db
def delete_one(id):
    conn = sq.connect('my_db.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM customers WHERE rowid = (?)", (id))
    # commit our command
    conn.commit()
    # close out connection
    conn.close()

# data_one = curs.fetchone()  # get first item in table
# data_many = curs.fetchmany(3)
  # returns python list


def email(email):
    conn = sq.connect('my_db.db')
    curs = conn.cursor()
    curs.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))

    data = curs.fetchall()
    for item in data:
        print(item)

    # commit our command
    conn.commit()
    # close out connection
    conn.close()


# API

# response = requests.get('http://api.open-notify.org/astros.json')


# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)


# name = response.json()['people']
# # jprint(name)

# crafts = []
# people = []

# for i in name:
#     craft = i['craft']
#     crafts.append(craft)
#     person = i['name']
#     people.append(person)

# print(crafts[1])
# print(people[1])
