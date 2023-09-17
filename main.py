from phonecontact import PhoneContact, ManagePhoneContact
import sys

#def phonebookApp(name, email, phoneno):
def createPhoneBook(name, email, phoneno):
  #pba = PhoneContact("john","john@abc.xyz","08012345678")
  #print(pba.name,pba.email,pba.phoneno)
  pba = PhoneContact()
  pba.addAttribute(name, email, phoneno)
  #pba.showContact()
  #mpc=ManagePhoneContact()
  #mpc.savePhoneContact(pba)
  return pba

def splitInput(prompt):
  if ("," in prompt):
    return prompt.split(",")
  else:
    return prompt.split()

def userInput():
  #if (len(sys.argv) < 3):
  #  #userInput()
  #  exit(0)
  #else:
  #  #{name, email, phoneno} = sys.argv
  #  name = sys.argv[1]
  #  email = sys.argv[2]
  #  phoneno = sys.argv[3]
  #  return {name, email, phoneno}
  menu_msg="""
    ###################################################################################
    #                          Phone Book (ver 1.0)                                   #
    ###################################################################################
    #                                                                                 #
    #                         1. Add Contact                                          #
    #                         2. Edit Contact                                         #
    #                         3. Delete Contact                                       #
    #                         4. Show Contact                                         #
    #                                                                                 #
    ###################################################################################\n"""
  print(menu_msg)

  # eval added because integer input expected
  contact=eval(input("Enter selection (1, 2, 3 or 4): ")) 
  #contact=contact.strip()  # error: int does not have attribute 'strip()'
  #contact=input()
  return contact

def PhoneBookApp():
  contact=userInput()

  input_msg="""
    ###################################################################################
    #  Enter contact's name, email and phone number on a line when prompted.          #
    #  Each information should be separated by space(" ") or comma(",").              #
    #  See below example:                                                             #
    #      "john" "john@abc.xyz" 08012345678                                          #
    #   or "john", "john@abc.xyz", 08012345678                                        #
    ###################################################################################\n"""
  print(input_msg)

  # eval not needed here because string input expected
  prompt=input("Enter contact's details: ")
  prompt=splitInput(prompt.strip())

  pba=createPhoneBook(prompt[0], prompt[1], prompt[2])
  mpc=ManagePhoneContact()

  if (contact==1):
    mpc.savePhoneContact(pba)
  elif (contact==2):
    mpc.editPhoneContact(pba)
  elif (contact==3):
    mpc.deletePhoneContact(pba)
  elif (contact==4):
    mpc.showPhoneContact(pba)


if __name__ == "__main__":
  #print("argv is :"+sys.argv)    # error: can't concatenate list to string
  #print(sys.argv)
  #{name, email, phoneno} = userInput()

  #nep = userInput()
  #print(nep)
  #phonebookApp(nep[0], nep[1], nep[2])
  PhoneBookApp()
