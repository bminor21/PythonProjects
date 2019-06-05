from tkinter import *
from DB import DB

db = DB()


def get_selected():
    index = listBox.curselection()[0]
    selected_tuple = listBox.get(index)
    return selected_tuple


def clear_entry_fields() -> None:
    titleEntry.delete(0, END)
    authorEntry.delete(0, END)
    yearEntry.delete(0, END)
    isbnEntry.delete(0, END)


def update_entry_fields(selected_tuple) -> None:
    titleEntry.insert(0, selected_tuple[1])
    authorEntry.insert(0, selected_tuple[2])
    yearEntry.insert(0, selected_tuple[3])
    isbnEntry.insert(0, selected_tuple[4])


def get_selected_row(event) -> None:
    clear_entry_fields()
    update_entry_fields(get_selected())


def viewall() -> None:
    listBox.delete(0, END)
    for entry in db.fetchall():
        listBox.insert(END, entry)


def search() -> None:
    listBox.delete(0, END)
    for row in db.search(titleInput.get(), authorInput.get(), yearInput.get(), isbnInput.get()):
        listBox.insert(END, row)


def add() -> None:
    db.insert(titleInput.get(), authorInput.get(), yearInput.get(), isbnInput.get())
    viewall()


def update() -> None:
    selected_tuple = get_selected()
    db.update(selected_tuple[0], titleInput.get(), authorInput.get(), yearInput.get(), isbnInput.get())
    viewall()


def delete() -> None:
    db.delete(get_selected()[0])
    viewall()


# Main Window
window = Tk()
window.wm_title("Bookstore")

# Variables
titleInput = StringVar()
yearInput = StringVar()
authorInput = StringVar()
isbnInput = StringVar()

# Components
titleLabel = Label(window, text='Title')
yearLabel = Label(window, text='Year')
authorLabel = Label(window, text='Author')
isbnLabel = Label(window, text='ISBN')

titleEntry = Entry(window, textvariable=titleInput)
yearEntry = Entry(window, textvariable=yearInput)
authorEntry = Entry(window, textvariable=authorInput)
isbnEntry = Entry(window, textvariable=isbnInput)

listBox = Listbox(window, height=6, width=35)
scrollbar = Scrollbar(window)

listBox.bind('<<ListboxSelect>>', get_selected_row)
listBox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listBox.yview)

viewAllBtn = Button(window, text='View All', command=viewall, width=12)
searchBtn = Button(window, text='Search Entry', command=search, width=12)
addBtn = Button(window, text='Add Entry', command=add, width=12)
updateBtn = Button(window, text='Update Selected', command=update, width=12)
deleteBtn = Button(window, text='Delete Selected', command=delete, width=12)
closeBtn = Button(window, text='Close', command=window.destroy, width=12)

# Placement
titleLabel.grid(row=0, column=0)
titleEntry.grid(row=0, column=1)
authorLabel.grid(row=0, column=2)
authorEntry.grid(row=0, column=3)

yearLabel.grid(row=1, column=0)
yearEntry.grid(row=1, column=1)
isbnLabel.grid(row=1, column=2)
isbnEntry.grid(row=1, column=3)

listBox.grid(row=2, column=0, rowspan=6, columnspan=2)
scrollbar.grid(row=2, column=2, rowspan=6)

viewAllBtn.grid(row=2, column=3)
searchBtn.grid(row=3, column=3)
addBtn.grid(row=4, column=3)
updateBtn.grid(row=5, column=3)
deleteBtn.grid(row=6, column=3)
closeBtn.grid(row=7, column=3)

window.mainloop()
