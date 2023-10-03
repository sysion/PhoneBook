import sqlite3
from sqlite3 import Error


def create_connection(dbfilepath):
  """ 
  create database specified by the dbfilepath 

  :param dbfilepath: full path to database file
  :return: Connection object or None
  """
  conn=None

  try:
    conn=sqlite3.connect(dbfilepath)
  except Error as e:
    print(e)
  
  return conn


"""
def create_table(conn):
  query="CREATE TABLE IF NOT EXISTS tblphonecontact( \
  _id INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY, \
  name TEXT(100) NOT NULL, \
  email TEXT(100) NOT NULL UNIQUE, \
  phoneno INTEGER(11) NOT NULL UNIQUE);"
"""