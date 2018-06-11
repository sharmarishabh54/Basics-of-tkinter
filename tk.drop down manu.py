from tkinter import *

def doit():
    print('HELLO')

root=Tk()

# create main menu

menubar=Menu(root)
root.config(menu=menubar)
submenu=Menu(menubar)

menubar.add_cascade(label='File',menu=submenu)
submenu.add_command(label='new',command=doit)
submenu.add_command(label='save as',command=doit)

submenu.add_separator()
submenu.add_command(label='exit',command=doit)

editmenu=Menu(menubar)
menubar.add_cascade(label='edit',menu=editmenu)
editmenu.add_command(label='redo',command=doit)

# create toolbar

toolbar=Frame(root,bg='cyan')
insertbutt=Button(toolbar,text="insert image",command=doit)
insertbutt.pack(side=LEFT,padx=2,pady=2)

printbutt=Button(toolbar,text="print",command=doit)
printbutt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)

# status bar

status=Label(root,text="let's do nothing",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()
