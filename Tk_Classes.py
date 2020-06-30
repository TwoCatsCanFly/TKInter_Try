from tkinter import *
root = Tk()
root.title('TKInter Tips')
root.iconbitmap('Portal.ico')

class Elder:
    def __init__(self,master):
        my_frame = Frame(master)
        my_frame.pack()

        self.my_button = Button(master, text="Click", command=self.clicker)
        self.my_button.pack(pady=20)

    def clicker(self):
        print("Clicked!")

e = Elder(root)

root.mainloop()