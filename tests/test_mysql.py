#!/usr/bin/python3
'''Tests for MySQL database'''
import unittest
import os
import tests
import MySQLdb

my_env = os.environ.copy()
TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
DB_HOST = os.getenv('HBNB_MYSQL_HOST')
DB_USER = os.getenv('HBNB_MYSQL_USER')
DB_PWD = os.getenv('HBNB_MYSQL_PWD')
DB_NAME = os.getenv('HBNB_MYSQL_DB')
STAGE = os.getenv('HBNB_ENV')


class TestMySQLdb(unittest.TestCase):
    '''This will test the database'''

    def test_establish_connection(self):
        '''test able to connect to mysql db with configs'''
        try:
            db = MySQLdb.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PWD
            )
        except Exception as e:
            print(my_env)
            print("Establish connection with DB failed due to {}", e)
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
