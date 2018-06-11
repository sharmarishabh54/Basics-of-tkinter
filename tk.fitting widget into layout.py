from tkinter import *

root = Tk()

one=Label(root,text='hello',fg='red',bg='yellow')
two=Label(root,text='welcome',fg='red',bg='pink')
three=Label(root,text='this is harley',fg='red',bg='green')

one.pack()
two.pack(fill=X)
three.pack(side=LEFT,fill=Y)

root.mainloop()
