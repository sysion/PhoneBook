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
    #print(f"Contact's name: {self.name}, email: {self.email}, phone number: {self.phoneno}")
    print("Contact's name: "+self.name+", email: "+self.email+", phone number: "+self.phoneno)

  def toString(self):
    return self.name+","+self.email+","+self.phoneno+"\n"

class ManagePhoneContact:
  def __init__(self):
    self.root={}

  def savePhoneContact(self,phonecontact,editflag=False):
    f=self._loadDatabase('a')
    
    if not (self._checkPhoneNum(phonecontact.phoneno)):
      f.write(phonecontact.toString())
      f.close()
      print("Record saved to file.")
    else:
      if not (editflag):
        print("Phone number already exists in database, aborting save . . .")
      else:
        f.write(phonecontact.toString())
        f.close()
        print("Record updated")

  def editPhoneContact(self,phonecontact):
    print("Editing record . . .")
    lines=self._checkName(phonecontact.name)
    if (len(lines)==1):
      info=lines.split(",")
      changes=self._makeChanges(info[0],info[1],info[2])
      #self.savePhoneContact(info[0],info[1],info[2],True)
      #self.savePhoneContact(changes[0],changes[1],changes[2],True)
      print(changes)
    elif (len(lines)>1):
      for line in lines:
        info=line.strip().split(",")
        if (info[2]==phonecontact.phoneno):
          changes=self._makeChanges(info[0],info[1],info[2])
          #self.savePhoneContact(info[0],info[1],info[2],True)
          #self.savePhoneContact(changes[0],changes[1],changes[2],True)
          print(changes)
          break
    else:
      print("Phone contact not in database, nothing to edit")

  def deletePhoneContact(self,phonecontact):
    lines=self._checkName(phonecontact.name)
    print(lines)
    if (len(lines)==1):
      #self._writeLineToFile(lines[0])        # ok       
      #self._writeLineToFile2(lines[0])       # ok
      self._writeLineToFile3(lines[0])
      print("Record deleted")
    elif (len(lines)>1):
      for line in lines:
        print(line)
        info=line.strip().split(",")
        print(f'db.phoneno={info[2]},user.phoneno={phonecontact.phoneno}')
        if (info[2]==phonecontact.phoneno):
          #self._writeLineToFile(line)
          #self._writeLineToFile2(line)
          self._writeLineToFile3(line)
          break
      print("Record deleted")
    else:
      print("Phone contact not in database, nothing to delete")

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
        [print(line.strip()) for line in f]  # ok but put blank line between output - strip() removes '\n'

  def _loadDatabase(self,mode):          # the preceeding underscore makes the function protected
    print("Loading database . . .")
    return open(dbfilepath,mode)

  def _checkPhoneNum(self,phoneno):      # the preceeding underscore makes the function protected
    phonedata=[]
    print(f"Checking if {phoneno} exists in database")
    f=self._loadDatabase('r')

    for line in f:
      phonedata.append(line.strip().split(",")[2])
    f.close()

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
    #print(lines)

    return lines

  def _makeChanges(self,name,email,phoneno):
    n_prompt=input("Type new name {name}: ")
    if (n_prompt=="\n"):
      n_prompt=name
    else:
      n_prompt=n_prompt.strip()

    e_prompt=input("Type new email {email}: ")
    if (e_prompt=="\n"):
      e_prompt=name
    else:
      e_prompt=e_prompt.strip()

    p_prompt=input("Type new phoneno {phoneno}: ")
    if (p_prompt=="\n"):
      p_prompt=name
    else:
      p_prompt=p_prompt.strip()

    return "good"

  def _writeLineToFile(self,dline):
    with open(dbfilepath,'r+') as f:    # open file for read/write
      lines=f.readlines()               # not good for large files in terms of RAM usage
      f.seek(0)                         # reset file index to start of file

      for line in lines:
        if line != dline:
          f.write(line)
      f.truncate()                      # delete end of the file
  
  def _writeLineToFile2(self,dline):
    with open(dbfilepath,'r+') as f:    # open file for read/write
      lines=f.readlines()               # not good for large files in terms of RAM usage
      f.seek(0)
      index=lines.index(dline)
      lines.pop(index)
      f.truncate()
      f.writelines(lines)

  def _writeLineToFile3(self,dline):
    with open(dbfilepath,"r") as f:     # open file for read
      with open("/tmp/phonebookfile.db","w") as nf:
        for line in f:                  # read one line per time, best for large files in terms of RAM usage
          if (line != dline):
            nf.write(line)
    os.replace("/tmp/phonebookfile.db",dbfilepath)