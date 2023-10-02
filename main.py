from phonecontact import PhoneContact, ManagePhoneContact
import sys

""" Creates and return PhoneContact object instance """
def createPhoneBook(name, email, phoneno):
  pba = PhoneContact()
  pba.addAttribute(name, email, phoneno)

  return pba

""" Convert user input into a list """
def splitInput(prompt):
  if ("," in prompt):
    return prompt.split(",")
  else:
    return prompt.split()

""" App starting Menu """
def userInput():
  menu_msg="""
    ###################################################################################
    #                          Phone Book (ver 1.0)                                   #
    ###################################################################################
    #                                                                                 #
    #                         1. Add Contact                                          #
    #                         2. Edit Contact                                         #
    #                         3. Delete Contact                                       #
    #                         4. Show Contact                                         #
    #                         5. Quit                                                 #
    #                                                                                 #
    ###################################################################################\n"""
  print(menu_msg)
  contact=eval(input(" Enter selection (1, 2, 3, 4 or 5): ")) 

  return contact

""" Manages execution of selected actions for app """
def PhoneBookApp(choice):
  contact=choice
  mpc=ManagePhoneContact()

  input_msg="""
    ###################################################################################
    #  Enter contact's name, email and phone number on a line when prompted.          #
    #  Each information should be separated by space(" ") or comma(",").              #
    #  See below example:                                                             #
    #      "john" "john@abc.xyz" 08012345678                                          #
    #   or "john", "john@abc.xyz", 08012345678                                        #
    ###################################################################################\n"""

  show_msg="""
    ###################################################################################
    #                1. Enter contact's name to display                               #
    #                2. Enter "All" to display all contact (without the quotes)       #
    ###################################################################################\n"""

  if (contact>0 and contact<4):
    print(input_msg)

    # eval not needed here because string input expected
    prompt=input(" Enter contact's details: ")
    prompt=splitInput(prompt.strip())
    
    pba=None

    if (len(prompt)==3):
      pba=createPhoneBook(prompt[0], prompt[1], prompt[2])
    else:
      print("Wrong input data or input not following required format")

    if (contact==1):
      mpc.savePhoneContact(pba)
    elif (contact==2):
      mpc.editPhoneContact(pba)
    elif (contact==3):
      mpc.deletePhoneContact(pba)
  elif (contact==4):
    print(show_msg)
    display=input(" Enter contact's details: ")
    display=display.strip()
    mpc.showPhoneContact(display)


""" App's entry point """
if __name__ == "__main__":
  choice=userInput()
  while (choice!=5):
    PhoneBookApp(choice)
    choice=userInput()
