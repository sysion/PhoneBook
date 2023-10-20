from gui import Gui
import tkinter as tk

# RuntimeError: Too early to create variable: no default root window
#name=tk.StringVar()
#or name=tk.Variable(value="")

name=""
email=""
phoneno=""

def showGui():
  maingui=Gui()
  name=tk.StringVar()
  email=tk.StringVar()
  phoneno=tk.StringVar()
  entry_frame=maingui.createFrame(maingui,0,0,5,5,tk.W)
  lblName=maingui.createLabel(entry_frame,"Name",0,0,1,2,2)
  entName=maingui.createText(entry_frame,0,1,3,2,2,(tk.N,tk.W,tk.S,tk.E),name)

  lblEmail=maingui.createLabel(entry_frame,"Email",1,0,1,2,2)
  entEmail=maingui.createText(entry_frame,1,1,3,2,2,(tk.N,tk.W,tk.S,tk.E),email)

  lblPhone=maingui.createLabel(entry_frame,"Phone",2,0,1,2,2)
  entPhone=maingui.createText(entry_frame,2,1,3,2,2,(tk.N,tk.W,tk.S,tk.E),phoneno)

  btnAdd=maingui.createButton(entry_frame,"Add",5,3,0,1,(5,2),2,"Add")
  btnEdit=maingui.createButton(entry_frame,"Edit",5,3,1,1,2,2,"Edit")
  btnShow=maingui.createButton(entry_frame,"Show",5,3,2,1,2,2,"Show")
  btnDelete=maingui.createButton(entry_frame,"Delete",5,3,3,1,2,2,"Delete")
  btnClear=maingui.createButton(entry_frame,"Clear",5,3,4,1,2,2,"Clear")

  result_frame=maingui.createFrame(maingui,1,0,5,5,(tk.N,tk.W,tk.S,tk.E))
  result_frame['height']=150
  #result_frame['background']="#0000ff"

  #lstResult=maingui.createList(result_frame,"left","both",True)
  #yScroll=maingui.createScroll(result_frame,tk.VERTICAL,"right","y")
  lstResult=maingui.createList2(result_frame,"left","both",True)

  maingui.centerWindow()
  return maingui


""" App's entry point """
if __name__ == "__main__":
  appgui=showGui()

  appgui.mainloop()