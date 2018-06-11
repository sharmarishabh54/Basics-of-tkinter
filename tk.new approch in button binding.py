from tkinter import *
# create a function which you want to bind with the button

def printmyname(event):
    print("hello there this is rishi ")

root=Tk()    

button1=Button(root,text='print my name')
button1.bind('<Button-1>',printmyname)
button1.pack()

root.mainloop()
