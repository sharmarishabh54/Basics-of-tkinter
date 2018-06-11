from tkinter import *
root = Tk()
topframe=Frame(root)
bottomframe=Frame(root)
topframe.pack()
bottomframe.pack(side=BOTTOM)
button1=Button(topframe,fg='blue',bg='white',text='click me')
button2=Button(topframe,fg='pink',bg='white',text='button2')
button3=Button(topframe,fg='purple',bg='white',text='button3')
button4=Button(bottomframe,fg='green',bg='white',text='button4')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=TOP)
button4.pack(side=BOTTOM)

root.mainloop()
