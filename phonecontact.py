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
    return self.getName()+","+self.getEmail()+","+self.getPhoneno()
    #return "".join(",","self.getName(),self.getEmail(),self.getPhoneno()")

  """ Save new contact to database """
  #def savePhoneContact(self,pba):
  def savePhoneContact(self,name,email,phoneno):
    #print(phonecontact.toString())
    #query="INSERT INTO tblphonecontact VALUES (?,?,?,?)"
    query="INSERT INTO tblphonecontact (name,email,phoneno) VALUES (?,?,?)"
    cursor=dbconn.cursor()

    try:
      #cursor.execute(query,(phonecontact.getName(),phonecontact.getEmail(),phonecontact.getPhoneno()))
      cursor.execute(query,(name,email,phoneno))
      print("Contact saved to database")
    except Error as e:
      print(e)

    dbconn.commit()
    cursor.close()

  """ Edit contact and update database with changes """
  def editPhoneContact(self,name,email,phoneno):
    pn=self._checkPhoneNum(phoneno)
    print(f'editPhoneContact->phoneno = {phoneno}')
    query="SELECT * FROM tblphonecontact WHERE phoneno = ?"
    pass

  """ Delete unwanted contact and update database with changes """
  def deletePhoneContact(self,phonecontact):
    query="SELECT * FROM tblphonecontact WHERE phoneno = ?"
    pass

  """ Display All contacts in database or only specified contact """
  def showPhoneContact(self,name):
    queryAll="SELECT * FROM tblphonecontact"
    query="SELECT * FROM tblphonecontact WHERE name = ?"
    cursor=dbconn.cursor()

    if (name=="All"):
      for row in cursor.execute(queryAll):
        print(row)
    else:
      #print(f'name = {name}')
      
      """
      sqlite3.ProgrammingError: Incorrect number of bindings supplied. 
      The current statement uses 1, and there are 3 supplied.

      This error occurs when a string parameter is passed to cursor.execute()
      instead of a list or tuple.

      Solution is to put the string a bracket and add comma to it to make
      it a tuple e.g. (name,)
      """
      #for row in cursor.execute(query,name):
      for row in cursor.execute(query,(name,)):
        print(row)

    cursor.close()

  """ Load contacts in database to computer memory """
  def _loadDatabase(self,mode):
    pass

  """ Check if contact's phone number exists in database """
  def _checkPhoneNum(self,phoneno):
    query="SELECT * FROM tblphonecontact WHERE phoneno = ?"
    cursor=dbconn.cursor()
    cursor.execute(query,(phoneno,))
    rows=cursor.fetchone()
    cursor.close()

    return rows

  """ Check if contact's name exists in database """
  def _checkName(self,name):
    query="SELECT * FROM tblphonecontact WHERE name = ?"
    cursor=dbconn.cursor()
    cursor.execute(query,(name,))
    rows=cursor.fetchAll()
    cursor.close()

    return rows

  """ Prompt for changes to be made while editing phone contact """
  def _makeChanges(self,name,email,phoneno):
    pass

  """ Save changes made to phone contact while editing """
  def _saveChanges(self,pba,new_pba):
    pass