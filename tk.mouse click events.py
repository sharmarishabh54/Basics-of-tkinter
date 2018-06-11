from tkinter import *

# mouse click events
def leftclick(event):
    print("THIS IS LEFT CLICK")
def middleclick(event):
    print('THIS IS MIDDLE CLICK')
def rightclick(event):
    print('THIS IS RIGH CLICK')

root=Tk()


frame1=Frame(root,width=400,height=400,bg='cyan')
frame1.bind("<Button-1>",leftclick)
frame1.bind("<Button-2>",middleclick)
frame1.bind("<Button-3>",rightclick)
frame1.pack()

root.mainloop()

