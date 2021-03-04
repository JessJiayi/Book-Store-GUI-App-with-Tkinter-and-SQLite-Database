from tkinter import *
import backend
window=Tk()

window.wm_title("BookStore")

def view_command():
    lsOutput.delete(0,END)
    for row in backend.view():
        lsOutput.insert(END,row)

def search_command():
    lsOutput.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lsOutput.insert(END,row)

def insert_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lsOutput.delete(0,END)
    for row in backend.view():
        lsOutput.insert(END,row)

def get_selected_row(event):
    global selected_tuple
    index=lsOutput.curselection()[0]
    selected_tuple=lsOutput.get(index)
    eTitle.delete(0,END)
    eTitle.insert(END,selected_tuple[1])
    eAuthor.delete(0,END)
    eAuthor.insert(END,selected_tuple[2])
    eYear.delete(0,END)
    eYear.insert(END,selected_tuple[3])
    eISBN.delete(0,END)
    eISBN.insert(END,selected_tuple[4])

def update_command():
    lsOutput.delete(0,END)
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lsOutput.delete(0,END)
    for row in backend.view():
        lsOutput.insert(END,row)

def delete_command():
    lsOutput.delete(0,END)
    backend.delete(selected_tuple[0])
    for row in backend.view():
        lsOutput.insert(END,row)

lbTitle=Label(window,text="Title")
lbTitle.grid(row=0,column=0)

title_text=StringVar()
eTitle=Entry(window,textvariable=title_text)
eTitle.grid(row=0,column=1)

lbAuthor=Label(window,text="Author")
lbAuthor.grid(row=0,column=2)

author_text=StringVar()
eAuthor=Entry(window,textvariable=author_text)
eAuthor.grid(row=0,column=3)

lbYear=Label(window,text="Year")
lbYear.grid(row=1,column=0)

year_text=StringVar()
eYear=Entry(window,textvariable=year_text)
eYear.grid(row=1,column=1)

lbISBN=Label(window,text="ISBN")
lbISBN.grid(row=1,column=2)

isbn_text=StringVar()
eISBN=Entry(window,textvariable=isbn_text)
eISBN.grid(row=1,column=3)

lsOutput=Listbox(window,height=6,width=35)
lsOutput.grid(row=2,column=0,columnspan=2,rowspan=6)

lsOutput.bind('<<ListboxSelect>>',get_selected_row)

sbOutput=Scrollbar(window)
sbOutput.grid(row=2,column=2,rowspan=6)
lsOutput.configure(yscrollcommand=sbOutput.set)
sbOutput.configure(command=lsOutput.yview)

btViewAll=Button(window,text='View All',width=12,command=view_command)
btViewAll.grid(row=2,column=3)

btSearch=Button(window,text='Search Entry',width=12,command=search_command)
btSearch.grid(row=3,column=3)

btAdd=Button(window,text='Add Entry',width=12,command=insert_command)
btAdd.grid(row=4,column=3)

btUpdate=Button(window,text='Update',width=12,command=update_command)
btUpdate.grid(row=5,column=3)

btDelete=Button(window,text='Delete',width=12,command=delete_command)
btDelete.grid(row=6,column=3)

btClose=Button(window,text='Close',width=12,command=window.destroy)
btClose.grid(row=7,column=3)

window.mainloop()
