import tkinter as tk


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
		'''
		# nok - TypeError: saveContact() takes 1 positional argument but 2 were given
		if (action_name=="Add"):
			button.bind("<Button>",self.saveContact)
			button.bind("<Return>",self.saveContact)
		elif (action_name=="Edit"):
			button.bind("<Button>",self.editContact)
		elif (action_name=="Show"):
			button.bind(self.showContact)
		elif (action_name=="Delete"):
			button.bind(self.deleteContact)
		'''
		return button

	def createList(self,parent,align,fill,expand):
		list=tk.Listbox(parent)
		list.pack(side=align,fill=fill,expand=expand)
		return list

	def createScroll(self,parent,orient,align,fill):
		scroll=tk.Scrollbar(parent,orient=orient)
		scroll.pack(side=align,fill=fill)
		return scroll

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
		return self.getVent()          # ok

	def clearData(self):
		for ent in self.__vent:
			ent.delete(0,tk.END)
		self.__vent[0].focus()

	def saveContact(self):
		contact=self.getData()
		print(f"Contact added: name={contact[0]},email={contact[1]},phoneno={contact[2]}")
		self.clearData()

	def editContact(self):
		print(f"Contact updated")

	def showContact(self):
		self.phoneno=""

	def deleteContact(self):
		self.phoneno=""

	def __sanitizeName(self,name):
		if (name.strip()!=""):
			pass

	def __sanitizeEmail(self,email):
		if (email.strip()!=""):
			pass

	def __sanitizePhoneNo(self,phoneno):
		if (phoneno.strip()!=""):
			pass