from tkinter import *

# first we'll use grid function 
root = Tk()
label1=Label(root,text='NAME')
label2=Label(root,text='PASSWORD')
entry1=Entry(root)
entry2=Entry(root)

"""now we'll use sticky function which will let us organise the stuff in a manner it
works on the basis of directions  where east stands for right, west for left
north stands for up and south stands for down """

label1.grid(row=0,sticky=E)
label2.grid(row=1,sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

""" now let's add a checkbox """

c=Checkbutton(root,text='keep me logged in')
c.grid(columnspan=2)
""" here columnspan function use whe you want to exceed your text more than one column """

root.mainloop()
