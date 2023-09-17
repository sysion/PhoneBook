"""
phonebook module containing PhoneContact and ManagePhoneContact
classes used for phonebook command line application
"""

import os

# get database file name in one step
dbfilepath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'db/phonebookfile.db')

# get database file name in three steps for understanding purpose
#thisfilepath=os.path.abspath(__file__)        # returns absolute path for this file i.e. phonecontact.py
#thisfiledirname=os.path.dirname(thisfilepath)
#dbfilepath=os.path.join(thisfiledirname,'db/phonebookfile.db')


class PhoneContact:
  # function or method overloading NOT supported in python
  def __init__(self):
  #  self.root={}   # ok also
    pass

  #def __init__(self,name,email,phoneno):
  #  self.name=name
  #  self.email=email
  #  self.phoneno=phoneno

  #def __init__(self, *args, **kwargs):
  #  if (len(args) != 3):
  #    print("parameters should be: name, email,phoneno")
  #  else:
  #    self.name=args[0]
  #    self.email=args[1]
  #    self.phoneno=args[2]

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
    self.name=name
    self.email=email
    self.phoneno=phoneno

  def showContact(self):
    #print("Contact's name: {self.name}, email: {self.email}, phone number: {self.phoneno}")
    print("Contact's name: "+self.name+", email: "+self.email+", phone number: "+self.phoneno)

  def toString(self):
    return self.name+","+self.email+","+self.phoneno+"\n"

class ManagePhoneContact:
  def __init__(self):
    self.root={}

  def savePhoneContact(self,phonecontact,editflag=False):
    f=self._loadDatabase('a')
    #self._checkPhoneNum(phonecontact.phoneno)
    print(self._checkPhoneNum(phonecontact.phoneno))
    if not (self._checkPhoneNum(phonecontact.phoneno)):
      f.write(phonecontact.toString())
      f.close()
      print("Record saved to file.")
      #print("Record saved to file: "+phonecontact.name)
      #print(f"Database file is: {dbfilepath}")   # debugging purpose
    else:
      if not (editflag):
        print("Phone number already exists in database, aborting save . . .")
      else:
        f.write(phonecontact.toString())
        f.close()
        print("Record updated")

  def editPhoneContact(self,name,email,phoneno):
    print("Editing record")
    lines=self._checkName(name)
    if (len(lines)==1):
      info=lines.split(",")
      self.savePhoneContact(info[0],info[1],info[2],True)
    elif (len(lines)>1):
      for line in lines:
        info=line.split(",")
        if (info[2]==phoneno):
          self.savePhoneContact(info[0],info[1],info[2],True)
          break
    else:
      print("Phone contact not in database, nothing to edit")

  def deletePhoneContact(self,name,email,phoneno):
    lines=self._checkName(name)
    if (len(lines)==1):
      pass 
    elif (len(lines)>1):
      for line in lines:
        info=line.split(",")
        if (info[2]==phoneno):
          pass
          break
      print("Record deleted")
    else:
      print("Phone contact not in database, nothing to delete")

  def showPhoneContact(self):
    print("Records displayed")

  def _loadDatabase(self,mode):          # the preceeding underscore makes the function protected
    print("Loading database . . .")
    return open(dbfilepath,mode)

  def _checkPhoneNum(self,phoneno):
    phonedata=[]
    print(f"Checking if {phoneno} exists in database")
    #with open(dbfilepath,'r') as f:
    #  #phonedata.append(f.read().split(",")[2])
    #  #phonedata.append([line.strip().split(",")[2] for line in f])
    #  phonedata.append(line.strip().split(",")[2] for line in f)
    #print(phonedata)
    f=self._loadDatabase('r')
    for line in f:
      phonedata.append(line.strip().split(",")[2])
    f.close()
    print(phonedata)

    return(phoneno in phonedata)

  def _checkName(self,name):
    lines=[]
    print(f"Checking if {name} exists in database")
    f=self._loadDatabase('r')
    for line in f:
      tmp=line
      if (tmp.strip().split(",")[0]==name):
        lines.append(line)
    f.close()
    print(lines)

    return lines
