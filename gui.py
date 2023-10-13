import tkinter as tk


class Gui(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Phonebook v1.0")
		self.resizable(0,0)
		self._name=""
		self._email=""
		self._phoneno=""

		#self.mainloop()      # for debugging

	def getName():
		return self.name

	def getEmail():
		return self.email

	def getPhoneNoText():
		return self.phoneno

	def setName(name):
		self.name=name

	def setEmail(email):
		self.email=email

	def setPhoneNo(phoneno):
		self.phoneno=phoneno

	def createFrame(self,parent,row,col,px,py,align):
		frame=tk.Frame(parent)
		frame.grid(row=row,column=col,ipadx=px,ipady=py,sticky=align)
		return frame

	def createLabel(self,parent,name,row,col,colspan,px,py):
		label=tk.Label(parent,text=name)
		label.grid(row=row,column=col,columnspan=colspan,padx=px,pady=py)
		return label

	def createText(self,parent,row,col,colspan,px,py,align):
		entry=tk.Entry(parent,textvariable=tk.StringVar())
		entry.grid(row=row,column=col,columnspan=colspan,padx=px,pady=py,sticky=align)
		return entry

	def createButton(self,parent,name,width,row,col,colspan,px,py):
		button=tk.Button(parent,text=name,width=width)
		button.grid(row=row,column=col,columnspan=colspan,padx=px,pady=py)
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

	def getNameText():
		self.name=""

	def getEmailText():
		self.email=""

	def getPhoneNoText():
		self.phoneno=""