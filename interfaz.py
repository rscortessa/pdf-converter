from tkinter import *

window=Tk()
#Labels
l1=Label(window,text="Número de imagenes")
l1.grid(row=0,column=0)
l1=Label(window,text="Dirección")
l1.grid(row=0,column=2)
l1=Label(window,text="Dirección de salida")
l1.grid(row=1,column=0)
#Entries
numeropags_text=StringVar()
numero=Entry(window,textvariable=numeropags_text)
numero.grid(row=0,column=1)

direccion_text=StringVar()
direccion=Entry(window,textvariable=direccion_text)
numero.grid(row=0,column=3)

direccionsal_text=StringVar()
direccionsal=Entry(window,textvariable=direccionsal_text)
numero.grid(row=1,column=2)

#Define list_box
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
#Attach scrollbar to the list
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
#Define buttons
b1=Button(window,text="View all",width=12)
b1.grid(row=2,column=3)
b1=Button(window,text="Search entry",width=12)
b1.grid(row=3,column=3)
window.mainloop()
#https://www.youtube.com/watch?v=ddoPYppcppc
