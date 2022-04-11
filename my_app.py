import db_func

# add record to db
# db_func.add_one('Camina', 'Drummer', 'beltaloda@mail.com')

# delete a record (use row id as string)
# db_func.delete_one('4')

# add many records to db
# items = [
#     ('James', 'Holden', 'jhold@mail.com'),
#     ('Alex', 'Kamal', 'alexk@space.com'),
#     ('Fred', 'Johnson', 'fredjohn@medina-st.com')
# ]
# db_func.add_many(list=items)

# lookup email address record
db_func.email('jhold@mail.com')

# show db
# db_func.show_all()
