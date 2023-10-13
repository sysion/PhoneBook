from gui import Gui
import tkinter as tk


""" App's entry point """
if __name__ == "__main__":
  maingui=Gui()
  entry_frame=maingui.createFrame(maingui,0,0,5,5,tk.W)
  lblName=maingui.createLabel(entry_frame,"Name",0,0,1,2,2)
  entName=maingui.createText(entry_frame,0,1,3,2,2,(tk.N,tk.W,tk.S,tk.E))

  lblEmail=maingui.createLabel(entry_frame,"Email",1,0,1,2,2)
  entEmail=maingui.createText(entry_frame,1,1,3,2,2,(tk.N,tk.W,tk.S,tk.E))

  lblPhone=maingui.createLabel(entry_frame,"Phone",2,0,1,2,2)
  entPhone=maingui.createText(entry_frame,2,1,3,2,2,(tk.N,tk.W,tk.S,tk.E))

  lblPhone=maingui.createLabel(entry_frame,"Phone",2,0,1,2,2)
  entPhone=maingui.createText(entry_frame,2,1,3,2,2,(tk.N,tk.W,tk.S,tk.E))

  btnAdd=maingui.createButton(entry_frame,"Add",6,3,0,1,(5,2),2)
  btnEdit=maingui.createButton(entry_frame,"Edit",6,3,1,1,2,2)
  btnShow=maingui.createButton(entry_frame,"Show",6,3,2,1,2,2)
  btnDelete=maingui.createButton(entry_frame,"Delete",6,3,3,1,2,2)

  result_frame=maingui.createFrame(maingui,1,0,5,5,(tk.N,tk.W,tk.S,tk.E))
  result_frame['height']=150
  result_frame['background']="#0000ff"

  lstResult=maingui.createList(result_frame,"left","both",True)
  yScroll=maingui.createScroll(result_frame,tk.VERTICAL,"right","y")

  maingui.centerWindow()
  

  maingui.mainloop()