from Tkinter import *

root = Tk()
root.geometry('200x200')

box = Entry(root,bg = 'red',justify = RIGHT)
box.insert(END,"nitin:\ti am nitin\n")

box.insert(END,"\ti am nitin2\n")
box.pack(fill = BOTH)

root.mainloop()