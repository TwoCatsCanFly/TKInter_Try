from tkinter import *
root = Tk()
# create vidget
myLabel = Label(root, text='hello world')
myLabel2 = Label(root, text='hello world')
myLabel3 = Label(root, text='hello world')
# showing
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=0)
# главный While True программы
root.mainloop()