import tkinter as tk
import tkinter.messagebox as msg
from phonecontact import PhoneContact


class Gui(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Phonebook v1.0")
		self.resizable(0,0)
		self.__name=""
		self.__email=""
		self.__phoneno=""
		self.__var_entry=[]
		self.__vent=[]
		self.__current_record_id=-1
		self.__list=None
		self.__listvar=[]
		self.__scroll=None

		#self.mainloop()      # for debugging

	def getName(self):
		return self.__name

	def getEmail(self):
		return self.__email

	def getPhoneNo(self):
		return self.__phoneno

	def getVarEntry(self):
		data=[]
		for var in self.__var_entry:
			data.append(var.get())
		return data

	def getVent(self):
		data=[]
		for var in self.__vent:
			data.append(var.get())
		return data

	def setName(self,name):
		self.__name=name

	def setEmail(self,email):
		self.__email=email

	def setPhoneNo(self,phoneno):
		self.__phoneno=phoneno

	def setVarEntry(self,ventry):
		self.__var_entry.append(ventry)

	def setVent(self,vent):
		self.__vent.append(vent)

	def createFrame(self,parent,row,col,px,py,align):
		frame=tk.Frame(parent)
		frame.grid(row=row,column=col,ipadx=px,ipady=py,sticky=align)
		return frame

	def createLabel(self,parent,name,row,col,colspan,px,py):
		label=tk.Label(parent,text=name)
		label.grid(row=row,column=col,columnspan=colspan,padx=px,pady=py)
		return label

	def createText(self,parent,row,col,colspan,px,py,align,text_var):
		self.setVarEntry(text_var)
		entry=tk.Entry(parent,textvariable=text_var)
		entry.grid(row=row,column=col,columnspan=colspan,padx=px,pady=py,sticky=align)
		self.__vent.append(entry)
		return entry

	def createButton(self,parent,name,width,row,col,colspan,px,py,action_name):
		action=None

		if (action_name=="Add"):
			action=self.saveContact
		elif (action_name=="Edit"):
			action=self.editContact
		elif (action_name=="Show"):
			action=self.showContact
		elif (action_name=="Delete"):
			action=self.deleteContact

		button=tk.Button(parent,text=name,width=width,command=action)
		button.grid(row=row,column=col,columnspan=colspan,padx=px,pady=py)
		
		return button

	def createList(self,parent,align,fill,expand):
		self.__list=tk.Listbox(parent,listvariable=self.__listvar,selectmode=tk.SINGLE,exportselection=False)
		self.__list.pack(side=align,fill=fill,expand=expand)
		self.__list.bind("<<ListboxSelect>>",self.listItemSelected) # required 'event' parameter provided by "<<ListboxSelect>>"
				
		return self.__list

	def createScroll(self,parent,orient,align,fill):
		self.__scroll=tk.Scrollbar(parent,orient=orient,command=self.__list.yview)
		self.__scroll.pack(side=align,fill=fill)
		self.__list['yscrollcommand']=self.__scroll.set
		return self.__scroll

	def centerWindow(self):
		self.update_idletasks()
		w=self.winfo_reqwidth()
		h=self.winfo_reqheight()
		ws=self.winfo_screenwidth()
		hs=self.winfo_screenheight()
		x=(ws//2)-(w//2)
		y=(hs//2)-(h//2)
		self.geometry('+%d+%d'%(x,y))

	def getData(self):
		#return self.getVarEntry()			# ok
		#return self.getVent()          # ok
		sdata=[]
		contact=self.getVent()
		sname=self.__sanitizeName(contact[0])
		semail=self.__sanitizeEmail(contact[1])
		sphoneno=self.__sanitizePhoneNo(contact[2])
		sdata.append(sname)
		sdata.append(semail)
		sdata.append(sphoneno)
		return sdata

	def clearData(self):
		for ent in self.__vent:
			ent.delete(0,tk.END)
		self.__vent[0].focus()

	def clearList(self):
		if self.__list.size()>0:
			self.__list.delete(0,tk.END)

	def listItemSelected(self,event):
		index=self.__list.curselection()
		selection=self.__list.get(index)
		self.__current_record_id=selection[0]
		
		i=1
		for ent in self.__vent:
			ent.delete(0,tk.END)
			ent.insert(0,selection[i])
			i+=1

		self.__vent[0].focus()

	def saveContact(self):
		self.clearList()
		contact=self.getData()

		pc=PhoneContact()
		status=pc.savePhoneContact(contact[0],contact[1],contact[2])
		if status==1:
			msg.showinfo("Success","Contact saved to database")
		elif status==-1:
			msg.showinfo("Information","Phone number already in database, nothing to save")
		elif status==-2:
			msg.showinfo("Information","Email already in database, nothing to save")
		elif status==-3:
			msg.showinfo("Failure","Unknown error when saving contact")
		elif status==-4:
			msg.showinfo("Failure","Incomplete contact Information")

		self.clearData()

	def editContact(self):
		self.clearList()
		contact=self.getData()
		pc=PhoneContact()
		status=pc.editPhoneContact(contact,self.__current_record_id)

		if status==1:
			msg.showinfo("Success","Contact updated in database")
		elif status==-1:
			msg.showinfo("Information","Changes not made, nothing to update")
		elif status==-2:
			msg.showinfo("Information","Phone number already in database, nothing to update")
		elif status==-3:
			msg.showinfo("Information","Email already in database, nothing to update")
		elif status==-4:
			msg.showinfo("Failure","Unknown error when updating contact")
		elif status==-5:
			msg.showinfo("Information","Phone contact not in database, nothing to edit")

		self.clearData()

	def showContact(self):
		self.clearList()
		contact=self.getData()
		option=None
		
		if contact[0]==None and contact[1]==None and contact[2]==None:
			option="All"
		elif contact[0]!=None and contact[0]!="":
			option=contact[0]
		else:
			msg.showerror("Invalid Inputs","Enter a name or leave all fields blank to query all contacts")
		
		if option!=None:
			pc=PhoneContact()
			rows=pc.showPhoneContact(option)
			i=0
			for row in rows:
				self.__list.insert(i,row)
				i+=1
			
		self.clearData()

	def deleteContact(self):
		self.clearList()
		#contact=self.getData()

		if self.__current_record_id==-1:
			msg.showinfo("Information","Phone contact not in database, nothing to delete")
			return

		pc=PhoneContact()
		status=pc.deletePhoneContact(self.__current_record_id)

		if status==1:
			msg.showinfo("Success","Contact deleted from database")
		elif status==-2:
			msg.showinfo("Failure","Error deleting contact")

		self.clearData()

	def __sanitizeName(self,name):
		if name.strip()!="":
			name=name.strip()
			return name

	def __sanitizeEmail(self,email):
		if email.strip()!="":
			email=email.strip()
			return email

	def __sanitizePhoneNo(self,phoneno):
		if phoneno.strip()!="":
			phoneno=phoneno.strip()
			return phoneno