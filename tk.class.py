from tkinter import *

class rishi:
    def __init__(self,master):
         frame=Frame(master)
         frame.pack()

         self.printbutton=Button(frame,text='print message',command=self.printmymessage)

         self.printbutton.pack()

         self.quitbutton=Button(frame,text='quit',command=frame.quit)

         self.quitbutton.pack()
         
    def printmymessage(self):
        print('this is rishi ')
root=Tk()
o=rishi(root)
root.mainloop()
