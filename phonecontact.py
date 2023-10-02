"""
phonecontact module containing PhoneContact and ManagePhoneContact
classes used for phonebook command line application
"""

import os
from db.phonebookdb import create_connection

# get full path to the database file phonebook.db
dbfilepath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'db/phonebook.db')

# get connection to database phonebook.db
dbconn=create_connection(dbfilepath)


""" PhoneContact class and its methods """
class PhoneContact:
  def __init__(self):
    pass

  def getName(self,name):
    return self.name

  def getEmail(self,email):
    return self.email

  def getPhoneno(self,phoneno):
    pass

  def setName(self,name):
    self.name=name

  def setEmail(self,email):
    self.email=email

  def setPhoneno(self,phoneno):
    self.phoneno=phoneno

  def addAttribute(self, name, email, phoneno):
    self.name=name.strip()
    self.email=email.strip()
    self.phoneno=phoneno.strip()

  def showContact(self):
    print("Contact's name: "+self.name+", email: "+self.email+", phone number: "+self.phoneno)

  def toString(self):
    return self.name+","+self.email+","+self.phoneno+"\n"

""" ManagePhoneContact class and its methods """
class ManagePhoneContact:
  def __init__(self):
    self.root={}

  """ Save new contact to database """
  def savePhoneContact(self,phonecontact):
    pass

  """ Edit contact and update database with changes """
  def editPhoneContact(self,phonecontact):
    pass

  """ Delete unwanted contact and update database with changes """
  def deletePhoneContact(self,phonecontact):
    pass

  """ Display All contacts in database or only specified contact """
  def showPhoneContact(self,option):
    pass

  """ Load contacts in database to computer memory """
  def _loadDatabase(self,mode):
    pass

  """ Check if contact's phone number exists in database """
  def _checkPhoneNum(self,phoneno):
    pass

  """ Check if contact's name exists in database """
  def _checkName(self,name):
    pass

  """ Prompt for changes to be made while editing phone contact """
  def _makeChanges(self,name,email,phoneno):
    pass

  """ Save changes made to phone contact while editing """
  def _saveChanges(self,pba,new_pba):
    pass