"""
phonebook module containing PhoneContact and ManagePhoneContact
classes used for phonebook command line application
"""

import os

# get database file name in one step
dbfilepath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'db/phonebookfile.db')


""" PhoneContact class and its methods """
class PhoneContact:
  def __init__(self):
    pass

  def getName(self):
    return self.name

  def getEmail(self):
    return self.email

  def getPhoneno(self):
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
    f=self._loadDatabase('a')
    
    if not (self._checkPhoneNum(phonecontact.phoneno)):
      f.write(phonecontact.toString())
      f.close()
      print("Record saved to file.")
    else:
      print("Phone number already exists in database, aborting save . . .")

  """ Edit contact and update database with changes """
  def editPhoneContact(self,phonecontact):
    print("Editing record . . .")
    lines=self._checkName(phonecontact.name)
    if (len(lines)==1):
      info=lines[0].strip().split(",")
      changes=self._makeChanges(info[0],info[1],info[2])
      self._saveChanges(phonecontact,changes)
    elif (len(lines)>1):
      for line in lines:
        info=line.strip().split(",")
        if (info[2]==phonecontact.phoneno):
          changes=self._makeChanges(info[0],info[1],info[2])
          self._saveChanges(phonecontact,changes)
          break
    else:
      print("Phone contact not in database, nothing to edit")

  """ Delete unwanted contact and update database with changes """
  def deletePhoneContact(self,phonecontact):
    lines=self._checkName(phonecontact.name)
    print(lines)
    if (len(lines)==1):
      self._writeLineToFile(lines[0])        
      print("Record deleted")
    elif (len(lines)>1):
      for line in lines:
        print(line)
        info=line.strip().split(",")
        print(f'db.phoneno={info[2]},user.phoneno={phonecontact.phoneno}')
        if (info[2]==phonecontact.phoneno):
          self._writeLineToFile(line)
          break
      print("Record deleted")
    else:
      print("Phone contact not in database, nothing to delete")

  """ Display All contacts in database or only specified contact """
  def showPhoneContact(self,option):
    if not (option=="All"):
      lines=self._checkName(option)
      if (len(lines)>0):
        for line in lines:
          print(line.strip())
      else:
        print("Phone contact not in database, nothing to show")
    else:
      with open(dbfilepath,'r') as f:
        [print(line.strip()) for line in f]

  """ Load contacts in database to computer memory """
  def _loadDatabase(self,mode):
    return open(dbfilepath,mode)

  """ Check if contact's phone number exists in database """
  def _checkPhoneNum(self,phoneno):
    phonedata=[]
    print(f"Checking if {phoneno} exists in database\n")
    f=self._loadDatabase('r')

    for line in f:
      phonedata.append(line.strip().split(",")[2])
    f.close()

    return(phoneno in phonedata)

  """ Check if contact's name exists in database """
  def _checkName(self,name):
    lines=[]
    print(f"Checking if {name} exists in database\n")
    f=self._loadDatabase('r')

    for line in f:
      tmp=line
      if (tmp.strip().split(",")[0]==name):
        lines.append(line)
    f.close()

    return lines

  """ Prompt for changes to be made while editing phone contact """
  def _makeChanges(self,name,email,phoneno):
    changes=[]
    n_prompt=input("Type new name {name}: ")
    n_prompt=n_prompt.strip()
    if (n_prompt==""):
      n_prompt=name
    else:
      n_prompt=n_prompt.strip()
    changes.append(n_prompt)

    e_prompt=input("Type new email {email}: ")
    e_prompt=e_prompt.strip()
    if (e_prompt==""):
      e_prompt=email
    else:
      e_prompt=e_prompt.strip()
    changes.append(e_prompt)

    p_prompt=input("Type new phoneno {phoneno}: ")
    p_prompt=p_prompt.strip()
    print(p_prompt)
    if (p_prompt==""):
      p_prompt=phoneno
    else:
      p_prompt=p_prompt.strip()
    changes.append(p_prompt)

    return changes

  """ Save changes made to phone contact while editing """
  def _saveChanges(self,pba,new_pba):
    if not (pba.name == new_pba[0] and pba.email == new_pba[1] and pba.phoneno.strip() == new_pba[2]):
      with open(dbfilepath,"r") as f:
        with open("/tmp/phonebookfile.db","w") as nf:
          for line in f:
            if not (pba.phoneno in line):
              nf.write(line)
            else:
              line=new_pba[0]+","+new_pba[1]+","+new_pba[2]+"\n"
              nf.write(line)
      os.replace("/tmp/phonebookfile.db",dbfilepath)
      print("Phone contact updated")
    else:
      print("User made no changes, nothing to update")

  """ Save changes to file """
  def _writeLineToFile(self,dline):
    with open(dbfilepath,"r") as f:
      with open("/tmp/phonebookfile.db","w") as nf:
        for line in f:
          if (line != dline):
            nf.write(line)
    os.replace("/tmp/phonebookfile.db",dbfilepath)