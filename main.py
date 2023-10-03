from phonecontact import PhoneContact
import sys

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

  # SyntaxError: unexpected EOF while parsing -> when Enter key pressed alone
  contact=eval(input(" Enter selection (1, 2, 3, 4 or 5): ")) 

  return contact

""" Manages execution of selected actions for app """
def PhoneBookApp(choice):
  contact=choice
  pba=PhoneContact()

  add_msg="""
    ###################################################################################
    #  Enter contact's name, email and phone number on a line when prompted.          #
    #  Each information should be separated by space(" ") or comma(",").              #
    #  See below example:                                                             #
    #      "john" "john@abc.xyz" 08012345678                                          #
    #   or "john", "john@abc.xyz", 08012345678                                        #
    ###################################################################################\n"""

  edit_del_msg="""
    ###################################################################################
    #                1. Enter contact's name to edit or delete                        #
    ###################################################################################\n"""

  show_msg="""
    ###################################################################################
    #                1. Enter contact's name to display                               #
    #                2. Enter "All" to display all contact (without the quotes)       #
    ###################################################################################\n"""

  if (contact>0 and contact<4):
    if (contact==1):
      print(add_msg)

      # eval not needed here because string input expected
      prompt=input(" Enter contact's details: ")
      prompt=splitInput(prompt.strip())

      if (len(prompt)==3):
        pba.addAttribute(prompt[0], prompt[1], prompt[2])
        print(f'PhoneBookApp->pba = {pba.toString()}')
        pba.savePhoneContact(pba.getName(),pba.getEmail(),pba.getPhoneno())
      else:
        print("Wrong input data or input data format")
    elif (contact==2):
      print(edit_del_msg)
      prompt=input(" Enter contact's name: ")
      prompt=splitInput(prompt.strip())

      if (len(prompt)==1):
        pba.editPhoneContact(prompt[0])
      else:
        pass
    elif (contact==3):
      print(edit_del_msg)
      prompt=input(" Enter contact's name: ")
      prompt=splitInput(prompt.strip())

      if (len(prompt)==1):
        pba.deletePhoneContact(prompt[0])
      else:
        pass
  elif (contact==4):
    print(show_msg)
    cname=input(" Enter contact's name: ")
    cname=cname.strip()
    pba.showPhoneContact(cname)


""" App's entry point """
if __name__ == "__main__":
  choice=userInput()
  while (choice!=5):
    PhoneBookApp(choice)
    choice=userInput()
