import sqlite3, os, create_db

'''
MAIN
'''

if __name__ == "__main__":

    db_filename = 'exercisebase.db'

    db_exists = os.path.exists(db_filename)

    if db_exists:
        print('Database already existed. Your tables will be filled with data')
    else:
        print('Database not existed. You need to create database')
        permission = input('Do you want to create database (y/n): ')
        if permission == 'y':
            create_db.creating_or_not_tables(db_filename)    