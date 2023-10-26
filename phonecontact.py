"""
phonecontact module containing PhoneContact class 
used for phonebook command line application with 
sqlite database
"""

import os
from db.phonebookdb import create_connection
from sqlite3 import Error

# get full path to the database file phonebook.db
dbfilepath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'db/phonebook.db')

# get connection to database phonebook.db
dbconn=create_connection(dbfilepath)


""" PhoneContact class and its methods """
class PhoneContact:
  def __init__(self):
    pass

  def addAttribute(self,name, email, phoneno):
    self.__name=name.strip()
    self.__email=email.strip()
    self.__phoneno=phoneno.strip()

  def getName(self):
    return self.__name

  def getEmail(self):
    return self.__email

  def getPhoneno(self):
    return self.__phoneno

  def setName(self,name):
    self.__name=name

  def setEmail(self,email):
    self.__email=email

  def setPhoneno(self,phoneno):
    self.__phoneno=phoneno

  def showContact(self):
    print("Contact's name: "+self.getName()+", email: "+self.getEmail()+", phone number: "+self.getPhoneno())

  def toString(self):
    return ",".join([self.getName(),self.getEmail(),self.getPhoneno()])

  """ Save new contact to database """
  def savePhoneContact(self,name,email,phoneno):
    query="INSERT INTO tblphonecontact (name,email,phoneno) VALUES (?,?,?)"
    cursor=dbconn.cursor()

    if name==None or email==None or phoneno==None:
      return -4

    try:
      cursor.execute(query,(name,email,phoneno))
      dbconn.commit()
      cursor.close()
      return 1
    except Error as e:
      if 'UNIQUE constraint' in str(e) and 'tblphonecontact.phoneno' in str(e):
        return -1
      elif 'UNIQUE constraint' in str(e) and 'tblphonecontact.email' in str(e):
        return -2
      else:
        return -3

  """ Edit contact and update database with changes """
  def editPhoneContact(self,record,id):    
    if not id==-1:
      response=self._updateChanges(record,id)
      return response
    else:
      return -5

  def deletePhoneContact(self,cid):
    query="DELETE FROM tblphonecontact WHERE _id=?"
    cursor=dbconn.cursor()
    try:
      cursor.execute(query,(cid,))
      dbconn.commit()
      cursor.close()
      print("Contact deleted from database")
      return 1
    except Error as e:
      print(str(e))
      return -2

  """ Display All contacts in database or only specified contact """
  def showPhoneContact(self,name):
    queryAll="SELECT * FROM tblphonecontact"
    query="SELECT * FROM tblphonecontact WHERE name=?"
    cursor=dbconn.cursor()

    if name=="All":
      return cursor.execute(queryAll)
    else:
      return cursor.execute(query,(name,))
    cursor.close()

  """ Check if contact's phone number exists in database """
  def _checkPhoneNum(self,phoneno):
    query="SELECT * FROM tblphonecontact WHERE phoneno=?"
    cursor=dbconn.cursor()
    cursor.execute(query,(phoneno,))
    rows=cursor.fetchone()
    cursor.close()

    return rows

  """ Check if contact's name exists in database """
  def _checkName(self,name):
    query="SELECT * FROM tblphonecontact WHERE name=?"
    cursor=dbconn.cursor()
    cursor.execute(query,(name,))
    rows=cursor.fetchall()
    cursor.close()

    return rows

  def _updateChanges(self,row,cid):
    query="UPDATE tblphonecontact SET name=?,email=?,phoneno=? WHERE _id=?"
    cursor=dbconn.cursor()
    try:
      cursor.execute(query,(row[0],row[1],row[2],cid))
      dbconn.commit()
      cursor.close()
      return 1
    except Error as e:
      if 'UNIQUE constraint' in str(e) and 'tblphonecontact.phoneno' in str(e):
        print('Phone number already in database, nothing to update')
        return -2
      elif 'UNIQUE constraint' in str(e) and 'tblphonecontact.email' in str(e):
        print('Email already in database, nothing to update')
        return -3
      else:
        print('Unknown error when updating contact')
        return -4   