from phonecontact import PhoneContact, ManagePhoneContact
import sys

def phonebookApp(name, email, phoneno):
  #pba = PhoneContact("john","john@abc.xyz","08012345678")
  #print(pba.name,pba.email,pba.phoneno)
  pba = PhoneContact()
  pba.addAttribute(name, email, phoneno)
  #pba.showContact()
  mpc=ManagePhoneContact()
  mpc.savePhoneContact(pba)

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
  input_msg="""
               Enter contact's name, email and phone number on a line when prompted.
               Each information should be separated by space(" ") or comma(",").
               See below example:
                      "john" "john@abc.xyz" 08012345678
                   or "john", "john@abc.xyz", 08012345678
            """
  print(input_msg)
  #contact=input()
  contact=input("Enter contact's details: ")
  
  if ("," in contact):
    return contact.split(",")
  else:
    return conatct.split()
 
if __name__ == "__main__":
  #print("argv is :"+sys.argv)    # can't concatenate list to string
  #print(sys.argv)
  #{name, email, phoneno} = userInput()
  nep = userInput()
  #print(nep)
  
  phonebookApp(nep[0], nep[1], nep[2])
