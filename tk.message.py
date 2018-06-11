# message box

from tkinter import *
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo('warning!','this is going good')


# if you wanna put condition in messagebox

var=tkinter.messagebox.askquestion('warning!','this is going good')

if(var=='yes'):
    print('you done it')
else:
    print('oops')



    
# let's try something new

var=tkinter.messagebox.askquestion('warning!','this is going good')

if(var=='yes'):
    tkinter.messagebox.showinfo('warning!','you nailed it')
    
else:
    tkinter.messagebox.showinfo('warning!','try something new')



    

root.mainloop()
