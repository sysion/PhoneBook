import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
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
		elif (action_name=="Clear"):
			action=self.clearRecord

		button=tk.Button(parent,text=name,width=width,command=action)
		button.grid(row=row,column=col,columnspan=colspan,padx=px,pady=py)
		
		return button

	def createList(self,parent,align,fill,expand):
		self.__list=tk.Listbox(parent,listvariable=self.__listvar,selectmode=tk.SINGLE,exportselection=False)
		self.__list.pack(side=align,fill=fill,expand=expand)
		self.__list.bind("<<ListboxSelect>>",self.listItemSelected) # required 'event' parameter provided by "<<ListboxSelect>>"
				
		return self.__list

	def createList2(self,parent,align,fill,expand):
		list_header = ['Id','Name','Email','PhoneNo']
		self.__list=ttk.Treeview(columns=list_header,show="headings",selectmode=tk.BROWSE) # only SINGLE selection allowed
		ysb=ttk.Scrollbar(orient="vertical",command=self.__list.yview)
		xsb=ttk.Scrollbar(orient="horizontal",command=self.__list.xview)
		ysb.pack(side="right",fill=fill,in_=parent)
		xsb.pack(side="bottom",fill=fill,in_=parent)
		self.__list.configure(yscrollcommand=ysb.set,xscrollcommand=xsb.set)
		self.__list.bind("<<TreeviewSelect>>",self.listItemSelected)
		#self.__list.grid(in_=parent)
		self.__list.pack(in_=parent,side=align,fill=fill,expand=expand)
		self.__list.bind("<Motion>","break")   # prevent resizing of column headers
		
		'''colwidth=30
		for col in list_header:
			self.__list.heading(col,text=col.title())
			self.__list.column(col,minwidth=colwidth,width=colwidth,anchor='center',stretch=False)
			#if col=='Id':
			#	colwidth=3
			#self.__list.column(col,width=colwidth,anchor="center")'''

		
		for col in list_header:
			self.__list.heading(col,text=col.title())
			self.__list.column(col,width=tkFont.Font().measure(col.title()),anchor="center")
		

		'''#self.__list.pack() # run this first, else winfo_reqwidth()/winfo_reqheight() returns 1
		size=self.__list.winfo_reqwidth()
		#print(f'tree-width = {size}')
		#print('tree-width = ', size/4)
		header_width = [40,110,110,110]
		for i,col in enumerate(list_header):
			#print(f'index = {i}, column = {col}')
			self.__list.heading(col,text=col.title())
			self.__list.column(col,minwidth=header_width[i],width=header_width[i],anchor='center',stretch=False)'''
			
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
		self.__current_record_id=-1
		self.__vent[0].focus()

	def clearEntryTest(self,index):
		self.__vent[index].delete(0,tk.END)
		self.__vent[index].focus()

	def clearList(self):
		#if self.__list.size()>0:               						# for tk.Listbox
		#	self.__list.delete(0,tk.END)          						# for tk.Listbox
		self.__list.delete(*self.__list.get_children())	  	# for ttk.Treeview

	def listItemSelected(self,event):
		'''
		index=self.__list.curselection()										# for tk.Listbox

		if len(index)==1:
			selection=self.__list.get(index)
			self.__current_record_id=selection[0]
			
			i=1
			for ent in self.__vent:
				ent.delete(0,tk.END)
				ent.insert(0,selection[i])
				i+=1
		'''
		auto_id=self.__list.selection()														# for ttk.Treeview
		item=self.__list.item(auto_id)
		#print(f"listItemSelected->item = {item}")
		selection=item['values']
		#print(f"listItemSelected->selection = {selection}")
		if len(selection)==4:
			self.__current_record_id=selection[0]
				
			i=1
			for ent in self.__vent:
				ent.delete(0,tk.END)
				if i==3:
					ent.insert(0,"0"+str(selection[i]))
				else:
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

		#self.clearData()
		self.clearRecord()

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

		#self.clearData()
		self.clearRecord()

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
				#self.__list.insert(i,row)                 # for tk.Listbox
				#i+=1
				self.__list.insert('',tk.END,value=row)    # for ttk.Treeview
			
		self.clearData()

	def deleteContact(self):
		self.clearList()
		#print(f"self.__current_record_id = {self.__current_record_id}")

		if self.__current_record_id==-1:
			msg.showinfo("Information","Phone contact not in database, nothing to delete")
		else:
			pc=PhoneContact()
			status=pc.deletePhoneContact(self.__current_record_id)

			if status==1:
				msg.showinfo("Success","Contact deleted from database")
			elif status==-2:
				msg.showinfo("Failure","Error deleting contact")

		#self.clearData()
		self.clearRecord()

	def clearRecord(self):
		self.clearList()
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
			if len(phoneno)>=11 and len(phoneno)<=14:
				return phoneno
			else:
				#msg.showinfo("Invalid Number","Invalid Phone number")
				self.clearEntryTest(2)