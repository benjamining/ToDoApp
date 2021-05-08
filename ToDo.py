import tkinter as tkinter
from tkinter import messagebox

#Fundtions for Todo List App

#Takes string from entrybox and inserts it into the listbox and flashes a infobox and has a small validation on it
def AddItem() :
    ItemA = TodoEntry.get()
    if ItemA != '' :
        todoList.insert(tkinter.END,ItemA)
        messagebox.showinfo('Info',f'{ItemA} Added')
    else :
        messagebox.showerror('Entry Error','There must be a value entered')

#Takes a cursor selection from the listbox and deletes it from the listbox and flashes a infobox
def DeleteItem():
    ItemD = todoList.curselection()
    messagebox.showinfo('Deleted!',f'{ItemD} Deleted')
    todoList.delete(ItemD)

def EditItem():
    ItemE = todoList.curselection()
    EIndex = todoList.index()
    messagebox.showinfo('Position',f'{ItemE} is at position {EIndex}')


#Install tkinter GUI as Main; give it a title and then set the size of the GUI 
Main = tkinter.Tk()
Main.title('To Do List')
Main.geometry('300x400')

#initilise empty List called todo 
todo = []

#title heading
todoTitle = tkinter.Label(Main, text='To Do List')
todoTitle.pack()

#Entry box for the todo list.
TodoEntry = tkinter.Entry(Main, text='Enter an item')
TodoEntry.pack()

#Add Button for the todo list
todoAdd = tkinter.Button(Main, text='Add Item', command=AddItem)
todoAdd.pack()

#Delete Button for the todo list
todoDelete = tkinter.Button(Main, text='Delete Item', command=DeleteItem)
todoDelete.pack()

#Edit Button for the todo list
todoEdit = tkinter.Button(Main, text='Edit Item', command=EditItem)
todoEdit.pack()

#Listbox for the todo list
todoList = tkinter.Listbox(Main)
todoList.pack()

Main.mainloop()
