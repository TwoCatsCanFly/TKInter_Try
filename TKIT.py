from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
root = Tk()
root.title('TKInter Tips')
#root.geometry('2000x1000')

def loclick():
    mylabel4 = Label(root, text='loclick Function Clicked')
    mylabel4.grid(row=1, column=5)
def pquit():
    quit()
def input_click():
    input_label = Label(root, text='Entered text: ' + input_box.get())
    input_label.grid(row=2, column=3)

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

# Радио кнопки))
frame_for_radio = LabelFrame(root, text='Радио кнопки', padx=15, pady=15)
frame_for_radio.grid(row=4, column=1, padx=10, pady=10)
r = IntVar()
r.set('2')

def rclicked(value):
    Label(frame_for_radio, text=value).pack()

rButton = Radiobutton(frame_for_radio, text='Radiobutton 1', variable =r, value=1, command= lambda: rclicked(r.get())).pack()
rButton1 = Radiobutton(frame_for_radio, text='Radiobutton 2', variable =r, value=2, command= lambda: rclicked(r.get())).pack()
rButton2 = Radiobutton(frame_for_radio, text='Radiobutton 3', variable =r, value=3, command= lambda: rclicked(r.get())).pack()
rButton3 = Radiobutton(frame_for_radio, text='Radiobutton 4', variable =r, value=4, command= lambda: rclicked(r.get())).pack()

# Popup
frame_for_Popup = LabelFrame(root, text='Popup', padx=15, pady=15)
frame_for_Popup.grid(row=4, column=2, padx=10, pady=10)
def popup1(): messagebox.showinfo('messagebox.showinfo ','Текст Информация')
def popup2(): messagebox.showwarning('messagebox.showwarning ','Текст Предупреждение')
def popup3(): messagebox.showerror('messagebox.showerror ','Текст Ошибка')
def popup4():
    responce = messagebox.askquestion('messagebox.askquestion ','Текст Вопрос')
    Label(frame_for_Popup, text='ОТВЕТ ДА').pack() if responce == 'yes' else Label(frame_for_Popup, text='ОТВЕТ НЕТ').pack()
def popup5():
    responce = messagebox.askokcancel('messagebox.askokcancel ','Текст Отмена?')
    Label(frame_for_Popup, text='ОТВЕТ OK').pack() if responce == 1 else Label(frame_for_Popup,
                                                                                   text='ОТВЕТ CANCEL').pack()
def popup6():
    responce = messagebox.askyesno('messagebox.askyesno ','Текст Да или Нет')
    Label(frame_for_Popup, text='ОТВЕТ ДА').pack() if responce == 1 else Label(frame_for_Popup,
                                                                                   text='ОТВЕТ НЕТ').pack()
pButton = Button(frame_for_Popup, text='showinfo', command=popup1).pack()
pButton = Button(frame_for_Popup, text='showwarning', command=popup2).pack()
pButton = Button(frame_for_Popup, text='showerror', command=popup3).pack()
pButton = Button(frame_for_Popup, text='askquestion', command=popup4).pack()
pButton = Button(frame_for_Popup, text='askokcancel', command=popup5).pack()
pButton = Button(frame_for_Popup, text='askyesno', command=popup6).pack()

# Дополнительное окно
def nw_open():
    global my_Img
    nw = Toplevel() # Дополнительное окно вызывается именно так
    nw.title('Second Window')
    my_Img = ImageTk.PhotoImage(Image.open('Test_img.jpg'))
    Label(nw, image=my_Img).grid()
    Button(nw,text='DESTROY WINDOW!!!11', command=nw.destroy).grid()
nw_btn = Button(root,text='New Window', command= nw_open).grid(row=4, column=3)

# Открытие файлов
def f_open():
    global f_image
    root.filename = filedialog.askopenfilename(initialdir='G:\Projects\TKInter_Try',
                                               filetypes=(('png files', '*.png'),
                                                          ('ico files', '*.ico'),
                                                          ('jpg files', '*.jpg'),
                                                          ('all files', '*.*')))
    if root.filename:
        f_image = ImageTk.PhotoImage(Image.open(root.filename))
        Label(frame_for_file, image=f_image).pack()

frame_for_file = LabelFrame(root, text='File', padx=15, pady=15)
frame_for_file.grid(row=4, column=4, padx=10, pady=10)
f_button = Button(frame_for_file, text='Open File',command=f_open).pack()

# Слайдеры
def slide(x=None):
    Label(frame_for_slider,text='vertical: '+ str(vertical.get())).grid(row=2, column=0)
    Label(frame_for_slider,text='horizontal: '+ str(horizontal.get())).grid(row=2, column=1)
frame_for_slider = LabelFrame(root, text='Slider', padx=15, pady=15)
frame_for_slider.grid(row=4, column=5, padx=10, pady=10)
vertical = Scale(frame_for_slider, from_=0, to=100,command=slide)
horizontal = Scale(frame_for_slider, from_=0, to=100, orient=HORIZONTAL,command=slide)
slide()
vertical.grid(row=0, column=0)
horizontal.grid(row=1, column=0)

# Чекбоксы
frame_for_checkbox = LabelFrame(root, text='Чекбоксы', padx=15, pady=15)
frame_for_checkbox.grid(row=4, column=6, padx=10, pady=10)
def chck(val):
    Label(frame_for_checkbox, text=val.get()).pack()
chck_var = StringVar()
chck_btn = Checkbutton(frame_for_checkbox, text='First box', variable=chck_var, onvalue='ON',offvalue='OFF',command=lambda: chck(chck_var))
chck_btn.deselect()
chck_btn.pack()

# Выпадающий список
frame_for_droplist = LabelFrame(root, text='Дроплист', padx=15, pady=15)
frame_for_droplist.grid(row=4, column=7, padx=10, pady=10)
def drop_lst(x):
    Label(frame_for_droplist, text=choosenone.get()).pack()
options = ['one','two','three','OMG, 2020 WKUA']
choosenone = StringVar()
choosenone.set(options[0])
drop = OptionMenu(frame_for_droplist, choosenone, *options,command=drop_lst).pack()

# База данных
dbase = 'address_book.db'
frame_for_database = LabelFrame(root, text='Дроплист', padx=15, pady=15)
frame_for_database.grid(row=4, column=8, padx=10, pady=10)
conn = sqlite3.connect(dbase) # create database + connect to it
c = conn.cursor() # create cursor

c.execute('''CREATE TABLE IF NOT EXISTS addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer)''')

f_name = Entry(frame_for_database, width=30)
l_name = Entry(frame_for_database, width=30)
address = Entry(frame_for_database, width=30)
city = Entry(frame_for_database, width=30)
state = Entry(frame_for_database, width=30)
zip_code = Entry(frame_for_database, width=30)
f_name.grid(row=0, column=1)
l_name.grid(row=1, column=1)
address.grid(row=2, column=1)
city.grid(row=3, column=1)
state.grid(row=4, column=1)
zip_code.grid(row=5, column=1)

f_name_lbl = Label(frame_for_database, text='Имя')
l_name_lbl = Label(frame_for_database, text='Фамилия')
address_lbl = Label(frame_for_database, text='Адрес')
city_lbl = Label(frame_for_database, text='Город')
state_lbl = Label(frame_for_database, text='Штат')
zip_code_lbl = Label(frame_for_database, text='Индекс')
f_name_lbl.grid(row=0, column=0)
l_name_lbl.grid(row=1, column=0)
address_lbl.grid(row=2, column=0)
city_lbl.grid(row=3, column=0)
state_lbl.grid(row=4, column=0)
zip_code_lbl.grid(row=5, column=0)

def submit():
    conn = sqlite3.connect(dbase)  # create database + connect to it
    c = conn.cursor()  # create cursor
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_code)',
        {'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zip_code': zip_code.get()})
    conn.commit()  # commit changes to database
    conn.close()  # close connection
    # clear texboxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zip_code.delete(0,END)
def query():
    conn = sqlite3.connect(dbase)  # create database + connect to it
    c = conn.cursor()  # create cursor
    c.execute('SELECT *,oid FROM addresses')
    records = c.fetchall()# сколько записей взять
    for id, record in enumerate(records):
        rid=9+id
        Label(frame_for_database,text=record).grid(row=rid,column=0)
    conn.commit()  # commit changes to database
    conn.close()  # close connection
def destr_database():
    conn = sqlite3.connect(dbase)  # create database + connect to it
    c = conn.cursor()  # create cursor
    c.execute('DELETE FROM addresses')
    conn.commit()  # commit changes to database
    conn.close()  # close connection


submit_btn = Button(frame_for_database, text='Submit to Database',command=submit).grid(row=6,column=0, columnspan =2,pady=10,padx=10,ipadx=50)
query_btn = Button(frame_for_database, text='Show from Database',command=query).grid(row=7,column=0, columnspan =2,ipadx=50)
clear_btn = Button(frame_for_database, text='DESTROY Database',command=destr_database).grid(row=8,column=0, columnspan =2,ipadx=50)


conn.commit()  #commit changes to database
conn.close()  #close connection







# главный While True программы)))
root.mainloop()

