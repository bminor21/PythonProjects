from tkinter import Entry, Button, Listbox, Scrollbar, END, StringVar, Label
from typing import Union, Any
from DB import DB

db = DB("books.db")


class Window:

    def __init__(self, window):

        self.window = window

        self.window.wm_title("Bookstore")

        # Variables
        self.titleInput = StringVar()
        self.yearInput = StringVar()
        self.authorInput = StringVar()
        self.isbnInput = StringVar()

        # Components
        self.titleLabel = Label(window, text='Title')
        self.yearLabel = Label(window, text='Year')
        self.authorLabel = Label(window, text='Author')
        self.isbnLabel = Label(window, text='ISBN')

        self.titleEntry = Entry(window, textvariable=self.titleInput)
        self.yearEntry = Entry(window, textvariable=self.yearInput)
        self.authorEntry = Entry(window, textvariable=self.authorInput)
        self.isbnEntry = Entry(window, textvariable=self.isbnInput)

        self.listBox = Listbox(window, height=6, width=35)
        scrollbar = Scrollbar(window)

        self.listBox.bind('<<ListboxSelect>>', self.get_selected_row)
        self.listBox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.listBox.yview)

        viewAllBtn = Button(window, text='View All', command=self.viewall, width=12)
        searchBtn = Button(window, text='Search Entry', command=self.search, width=12)
        addBtn = Button(window, text='Add Entry', command=self.add, width=12)
        updateBtn = Button(window, text='Update Selected', command=self.update, width=12)
        deleteBtn = Button(window, text='Delete Selected', command=self.delete, width=12)
        closeBtn = Button(window, text='Close', command=window.destroy, width=12)

        # Placement
        self.titleLabel.grid(row=0, column=0)
        self.titleEntry.grid(row=0, column=1)
        self.authorLabel.grid(row=0, column=2)
        self.authorEntry.grid(row=0, column=3)

        self.yearLabel.grid(row=1, column=0)
        self.yearEntry.grid(row=1, column=1)
        self.isbnLabel.grid(row=1, column=2)
        self.isbnEntry.grid(row=1, column=3)

        self.listBox.grid(row=2, column=0, rowspan=6, columnspan=2)
        scrollbar.grid(row=2, column=2, rowspan=6)

        viewAllBtn.grid(row=2, column=3)
        searchBtn.grid(row=3, column=3)
        addBtn.grid(row=4, column=3)
        updateBtn.grid(row=5, column=3)
        deleteBtn.grid(row=6, column=3)
        closeBtn.grid(row=7, column=3)

    def get_selected(self) -> Union[Any, None]:
        selected_tuple = None
        try:
            index = self.listBox.curselection()[0]
            selected_tuple = self.listBox.get(index)
        except IndexError:
            pass

        return selected_tuple

    def clear_entry_fields(self) -> None:
        self.titleEntry.delete(0, END)
        self.authorEntry.delete(0, END)
        self.yearEntry.delete(0, END)
        self.isbnEntry.delete(0, END)

    def update_entry_fields(self, selected_tuple) -> None:
        self.titleEntry.insert(0, selected_tuple[1])
        self.authorEntry.insert(0, selected_tuple[2])
        self.yearEntry.insert(0, selected_tuple[3])
        self.isbnEntry.insert(0, selected_tuple[4])

    def get_selected_row(self, event) -> None:
        selected_tuple = self.get_selected()
        self.clear_entry_fields()
        if selected_tuple is not None:
            self.update_entry_fields(selected_tuple)

    def viewall(self) -> None:
        self.listBox.delete(0, END)
        for entry in db.fetchall():
            self.listBox.insert(END, entry)

    def search(self) -> None:
        self.listBox.delete(0, END)
        for row in db.search(self.titleInput.get(), self.authorInput.get(), self.yearInput.get(), self.isbnInput.get()):
            self.listBox.insert(END, row)

    def add(self) -> None:
        db.insert(self.titleInput.get(), self.authorInput.get(), self.yearInput.get(), self.isbnInput.get())
        self.viewall()

    def update(self) -> None:
        selected_tuple = self.get_selected()
        if selected_tuple is not None:
            db.update(selected_tuple[0], self.titleInput.get(), self.authorInput.get(),
                      self.yearInput.get(), self.isbnInput.get())
            self.viewall()

    def delete(self) -> None:
        selected_tuple = self.get_selected()
        if selected_tuple is not None:
            db.delete(selected_tuple[0])
            self.viewall()