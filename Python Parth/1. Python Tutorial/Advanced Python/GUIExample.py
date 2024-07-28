from tkinter import *
root = Tk()


w = Label(root, text='Hello to my GUI').grid(row=0, sticky=W)

button = Button(root, text='Stop', width=25, command=root.destroy).grid(row=1,sticky=W)


var1 = IntVar()
Checkbutton(root, text='male', variable=var1).grid(row=2, sticky=W)
var2 = IntVar()
Checkbutton(root, text='female', variable=var2).grid(row=3, sticky=W)

Label(root, text='First Name').grid(row=4)
Label(root, text='Last Name').grid(row=5)
e1 = Entry(root).grid(row=4,column=1)
e2 = Entry(root).grid(row=5,column=1)

'''
widgets are added here
'''
mainloop()
