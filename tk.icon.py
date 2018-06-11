# adding icon to your tk file

icon = PhotoImage(file='YourImageName.gif')
root.tk.call('wm', 'iconphoto', root._w, icon)
