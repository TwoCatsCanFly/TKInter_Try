from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('TKInter Tips')

def loclick():
    myLabel4 = Label(root, text='loclick Function Clicked')
    myLabel4.grid(row=1, column=5)
def pquit():
    quit()
def input_click():
    input_Label = Label(root, text='Entered text: ' + input_box.get())
    input_Label.grid(row=2, column=3)

# Текст
myLabel = Label(root, text='Hello world')
myLabel2 = Label(root, text='TKInter')
myLabel3 = Label(root, text='hello mr. Freeman')

# Кнопки
button = Button(root, text='Doubt')
button1 = Button(root, text='disabled',state='disabled')
button2 = Button(root, text='padx=50',padx=50)
button3 = Button(root, text='padx=50, pady=50',padx=50, pady=50).grid(row=1, column=3)
button4 = Button(root, text='loclick Function', command=loclick).grid(row=1, column=4)
button5 = Button(root, text='Quit Function', command=pquit).grid(row=1, column=6)
button6 = Button(root, text='fg=\'red\',bg=\'black\'', fg='red',bg='black').grid(row=2, column=0)
button7 = Button(root, text='root.quit',command = root.quit).grid(row=3, column=0)

# Ввод
input_box = Entry(root,width=50,borderwidth='10')
input_box.insert(0,'input_box')
input_box.grid(row=2, column=1)
input_button = Button(root, text='Enter Text', fg='black',bg='orange',command=input_click).grid(row=2, column=2)

# Отображение созданных обьектов, можно по другому
myLabel.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=2)
button.grid(row=1, column=0)
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)

# Статус
status = Label(root,
               text='Wtf 1 of 10, columnspan = 6, bd = 1, relief = SUNKEN, sticky = W+E, anchor = E',
               bd = 1,
               relief = SUNKEN,
               anchor = E)
status.grid(row=10, column=0, columnspan = 7, sticky = W+E)

# Рамка
frame = LabelFrame(root, text='Frame,  padx=5, pady=5', padx=15, pady=15)
frame.grid(row=4, column=0, padx=10, pady=10)
button_f = Button(frame, text = 'Im in a frame!!11').grid()

# картинки. поддержка gif встроенная
root.iconbitmap('Windows.ico')
myImg = ImageTk.PhotoImage(Image.open('Test_img.jpg'))
my_Label = Label(frame, image=myImg).grid()

# главный While True программы)))
root.mainloop()

