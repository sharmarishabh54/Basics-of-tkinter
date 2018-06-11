from tkinter import *
""" now we gonna bind the function to the layout"""


def printmyname():
    print('hello this is rishi')
root = Tk()
button1=Button(root,text='print my name',fg='black',command=printmyname)

button2=Button(root,text='quit',fg='black',command= root.quit)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)

root.mainloop()
