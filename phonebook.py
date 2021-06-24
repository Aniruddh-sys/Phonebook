from tkinter import *
box = Tk()
box.title('Phonebook')
box.geometry('500x500')
box.config(bg = 'black')
box.resizable(0,0)
contactlist = [
['Shaunak Biswas', '9638527445'],
['Shreyansh Malewar', '74563245885']
]
Name = StringVar()
Number = StringVar()
frame = Frame(box)
frame.pack(side = RIGHT)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=99)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)
def Selected():
return int(select.curselection()[0])
def AddContact():
contactlist.append([Name.get(), Number.get()])
Select_set()def EDIT():
contactlist[Selected()] = [Name.get(), Number.get()]
Select_set()
def DELETE():
del contactlist[Selected()]
Select_set()
def VIEW():
NAME, PHONE = contactlist[Selected()]
Name.set(NAME)
Number.set(PHONE)
def EXIT():
box.destroy()
def RESET():
Name.set('')
Number.set('')
def Select_set() :
contactlist.sort()
select.delete(0,END)
for name,phone in contactlist :
select.insert (END, name)
Select_set()
Label(box, text = 'NAME', font='calabri 12 bold', bg = 'white').place(x= 30, y=20)
Entry(box, textvariable = Name).place(x= 100, y=20)
Label(box, text = 'PHONE NO.', font='calabri 12 bold',bg = 'white').place(x= 30, y=70)
Entry(box, textvariable = Number).place(x= 130, y=70)
Button(box,text=" ADD", font='calabri 12 bold',bg='green', command = AddContact).place(x= 50,
y=110)
Button(box,text="DELETE", font='calabri 12 bold',bg='red',command = EDIT).place(x= 50, y=260)
Button(box,text="EDIT", font='calabri 12 bold',bg='green',command = DELETE).place(x= 50, y=210)Button(box,text="VIEW", font='calabri 12 bold',bg='green', command = VIEW).place(x= 50, y=160)
Button(box,text="EXIT", font='calabri 12 bold',bg='tomato', command = EXIT).place(x= 300, y=320)
Button(box,text="RESET", font='calabri 12 bold',bg='tomato', command = RESET).place(x= 50, y=310)
box.mainloop()
