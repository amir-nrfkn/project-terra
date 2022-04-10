import requests
import json
import sqlite3 as sq

# DATABASE

# connect to or create a database
conn = sq.connect('my_db.db')
# or to create a db in memory that gets wiped after close
# conn_temp = sq.connect(':memory:')

# create a table
# first create a curser
curs = conn.cursor()
# now you can create the table
# curs.execute("""CREATE TABLE customers (
#                     first_name text,
#                     last_name text,
#                     email text
#                     )
#                 """)
# SQLITE3 has 5 data types: null, int, real, text, blob

# customers = [
#     ('Krisjen', 'Avaserala', 'krissy@mail.com'),
#     ('Naomi', 'Nagata', 'naynay@mail.com'),
#     ('Ames', 'Burton', 'ames@mail.com')
# ]

# to add multiple items to db, use .executemany()
# curs.executemany("INSERT INTO customers VALUES (?,?,?)", customers)

# curs.execute("""INSERT INTO customers
#                 VALUES ('James', 'Holden', 'holden@gmail.com')
# """)

curs.execute("""UPDATE customers SET email = 'k_avaserala@mail.com'
                WHERE rowid = 1
""")

conn.commit()

# query the database to read it
curs.execute("SELECT rowid, * FROM customers")
# data_one = curs.fetchone()  # get first item in table
# data_many = curs.fetchmany(3)
data_all = curs.fetchall()  # returns python list

# for item in data_all:
#     print(item)

print(data_all)

# commit command to database, pushes curs.execute() to database
# conn.commit()

# close connection
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
