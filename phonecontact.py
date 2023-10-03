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
    #return self.getName()+","+self.getEmail()+","+self.getPhoneno()         # ok
    return ",".join([self.getName(),self.getEmail(),self.getPhoneno()])

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
      dbconn.commit()
      cursor.close()
      print("Contact saved to database")
    except Error as e:
      #print(type(e))
      #print(e)
      #print(str(e))

      # sqlite3.IntegrityError: UNIQUE constraint failed: tblphonecontact.phoneno
      # sqlite3.IntegrityError: UNIQUE constraint failed: tblphonecontact.email
      if ('UNIQUE constraint' in str(e) and 'tblphonecontact.phoneno' in str(e)):
        print('Phone number already in database, nothing to save')
        return
      elif ('UNIQUE constraint' in str(e) and 'tblphonecontact.email' in str(e)):
        print('Email already in database, nothing to save')
        return
      else:
        print('Unknown error when saving contact')
        return

  """ Edit contact and update database with changes """
  #def editPhoneContact(self,name,email,phoneno):
  def editPhoneContact(self,name):
    #phonenum=self._checkPhoneNum(phoneno)
    #print(f'editPhoneContact->phoneno = {phonenum}')

    rows=self._checkName(name)

    print(f'editPhoneContact->names = {rows}')
    print(f'editPhoneContact->num_names = {len(rows)}')
    """
    editPhoneContact->names = 
    [(2, 'joy', 'joy@fcmb.com', '08023456789'), 
    (9, 'joy', 'joy@inter.org', '07023456789'), 
    (13, 'joy', 'joy@akt.net', '09034567891')]
    editPhoneContact->num_names = 3
    """

    if (len(rows)==1):
      #contact=rows[0].split(",")    # tuple object has no attribute split()
      #ncontact=self._getChanges(contact[1],contact[2],contact[3])
      cid=rows[0][0]
      print(f'editPhoneContact->ncontact_id = {cid}')

      ncontact=self._getChanges(rows[0][1],rows[0][2],rows[0][3])
      print(f'editPhoneContact->ncontact = {ncontact}')
      
      query="UPDATE tblphonecontact SET name=?,email=?,phoneno=? WHERE _id=?"
      cursor=dbconn.cursor()
      try:
        cursor.execute(query,(ncontact[0],ncontact[1],ncontact[2],cid))
        dbconn.commit()
        cursor.close()
        print("Contact updated in database")
      except Error as e:
        #print(e)
        if ('UNIQUE constraint' in str(e) and 'tblphonecontact.phoneno' in str(e)):
          print('Phone number already in database, nothing to update')
          return
        elif ('UNIQUE constraint' in str(e) and 'tblphonecontact.email' in str(e)):
          print('Email already in database, nothing to update')
          return
        else:
          print('Unknown error when updating contact')
          return
    elif (len(rows)>1):
      nrow=self._selectContact(rows)
      print(f'editPhoneContact->nrow = {nrow}')

      cid=nrow[0]
      print(f'editPhoneContact->ncontact_id = {cid}')

      ncontact=self._getChanges(nrow[1],nrow[2],nrow[3])
      print(f'editPhoneContact->ncontact = {ncontact}')
      
      query="UPDATE tblphonecontact SET name=?,email=?,phoneno=? WHERE _id=?"
      cursor=dbconn.cursor()
      try:
        cursor.execute(query,(ncontact[0],ncontact[1],ncontact[2],cid))
        dbconn.commit()
        cursor.close()
        print("Contact updated in database")
      except Error as e:
        #print(e)
        if ('UNIQUE constraint' in str(e) and 'tblphonecontact.phoneno' in str(e)):
          print('Phone number already in database, nothing to update')
          return
        elif ('UNIQUE constraint' in str(e) and 'tblphonecontact.email' in str(e)):
          print('Email already in database, nothing to update')
          return
        else:
          print('Unknown error when updating contact')
          return
    else:
      print("Phone contact not in database, nothing to edit")

  """ Delete unwanted contact and update database with changes """
  def deletePhoneContact(self,name):
    cid=-1
    rows=self._checkName(name)

    if (len(rows)==1):
      cid=rows[0][0]
    elif (len(rows)>1):
      nrow=self._selectContact(rows)
      cid=nrow[0]
    else:
      print("Phone contact not in database, nothing to delete")
      return
    
    query="DELETE FROM tblphonecontact WHERE _id=?"
    cursor=dbconn.cursor()
    try:
      cursor.execute(query,(cid,))
      dbconn.commit()
      cursor.close()
      print("Contact deleted from database")
    except Error as e:
      #print(e)
      print(str(e))
      return

  """ Display All contacts in database or only specified contact """
  def showPhoneContact(self,name):
    queryAll="SELECT * FROM tblphonecontact"
    query="SELECT * FROM tblphonecontact WHERE name=?"
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

      Solution is to put the string in bracket and add comma to it to make
      it a tuple e.g. (name,)
      """
      #for row in cursor.execute(query,name):    # sqlite3.ProgrammingError: Incorrect number of bindings supplied
      for row in cursor.execute(query,(name,)):
        print(row)

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

  """ Prompt for changes to be made while editing phone contact """
  def _getChanges(self,name,email,phoneno):
    input_msg="""
    ###################################################################################
    #  Type contact's name, email and phone number on a line when prompted.           #
    #                                                                                 #
    #  Accept displayed option by pressing Enter key.                                 #
    ###################################################################################\n"""
    print(input_msg)
   
    cname=input(f" Enter contact's name [{name}]: ")
    if (cname.strip()==""):
      cname=name
    else:
      cname=cname.strip()

    cemail=input(f" Enter contact's email [{email}]: ")
    if (cemail.strip()==""):
      cemail=email
    else:
      cemail=cemail.strip()

    cphoneno=input(f" Enter contact's phoneno [{phoneno}]: ")
    if (cphoneno.strip()==""):
      cphoneno=phoneno
    else:
      cphoneno=cphoneno.strip()

    return (cname,cemail,cphoneno)

  """ Enables user to select the phone contact to edit or delete """
  def _selectContact(self,contacts):
    select_msg="""
    ###################################################################################
    #           Select phone contact e.g. 1, 2 or 3 . . .                             #
    ###################################################################################\n"""

    e_msg="    ###################################################################################\n"

    count=0

    for contact in contacts:
      count+=1
      row_msg=f"    #         {count}. {contact[1],contact[2],contact[3]}\n" 
      select_msg+=row_msg
    
    select_msg+=e_msg
    print(select_msg)

    choice=-1
    while (choice<0 or choice>count):
      try:
        #choice=eval(input("Enter choice: "))
        choice=input("Enter choice: ")
        choice=choice.strip()
        if (choice==""):
          choice=-1
          print('Invalid choice . . .\n')
        else:
          choice=eval(choice)
      except Error as e:
        print(str(e))
        #print(e)
    
    #print(f'_selectContact->choice = {choice}')

    choice-=1
    return (contacts[choice])

    
    
    