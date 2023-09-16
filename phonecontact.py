
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

class ManagePhoneContact:
  def __init__(self):
    self.root={}

  def savePhoneContact(self,phonecontact):
    print("Record saved to file: "+phonecontact.name)

  def editPhoneContact(self,phonecontact):
    print("Record editted")

  def deletePhoneContact(self,phonecontact):
    print("Record deleted")

  def showPhoneContact(self):
    print("Records displayed")
