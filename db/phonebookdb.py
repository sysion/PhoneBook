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