from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")

root = Tk()
root.title("Employee Management Systems")
root.geometry("500x500+300+50")
root.config(bg="pink")

# text-variable
name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame in Title Frame
entries_frame = Frame(root, bg="#a398a2")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="EMPLOYEE MANAGEMENT SYSTEMS", font=("Arial", 24, "bold"), bg="#a398a2", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20)

# Label Frame
lblName = Label(entries_frame, text="Name", font=("arial", 18), bg='#a398a2', fg='white')
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="W")
txtName = Entry(entries_frame, textvariable=name, font=("arial", 18), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="W")

lblAge = Label(entries_frame, text="Age", font=("arial", 18), bg='#a398a2', fg='white')
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="W")
txtAge = Entry(entries_frame, textvariable=age, font=("arial", 18), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="W")

lblDoj = Label(entries_frame, text="DOJ", font=("arial", 18), bg='#a398a2', fg='white')
lblDoj.grid(row=2, column=0, padx=10, pady=10, sticky="W")
txtDoj = Entry(entries_frame, textvariable=doj, font=("arial", 18), width=30)
txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="W")

lblEmail = Label(entries_frame, text="Email", font=("arial", 18), bg='#a398a2', fg='white')
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="W")
txtEmail = Entry(entries_frame, textvariable=email, font=("arial", 18), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="W")

lblGender = Label(entries_frame, text="Gender", font=("arial", 18), bg='#a398a2', fg='white')
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="W")
comboGender = ttk.Combobox(entries_frame, font=("arial", 18), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ('Male', 'Female', 'Others')
comboGender.grid(row=3, column=1, padx=10, sticky="W")

lblContact = Label(entries_frame, text="Contact", font=("arial", 18), bg='#a398a2', fg='white')
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="W")
txtContact = Entry(entries_frame, textvariable=contact, font=("arial", 18), width=30)
txtContact.grid(row=3, column=3, padx=10, pady=10, sticky="W")

lblAddress = Label(entries_frame, text="Address", font=("arial", 18), bg='#a398a2', fg='white')
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="W")
txtAddress = Text(entries_frame, width=85, height=5, font=("arial", 18))
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky='W')


# Functions

def displayAll():
    # tv.delete(*tv.get_children()) - stop the loading duplicates in the Db
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def clearAll():
    pass


def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get(
    ) == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Error", "Please fill the details")
        return
    db.insert(txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(
    ), txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Data Inserted")
    clearAll()
    displayAll()


def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get(
    ) == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Error", "Please fill the details")
        return
    db.update(row[0], txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(
    ), txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Data Updated Successfully")
    clearAll()
    displayAll()


def getData(event):  # for update functions
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    # if u print the row the db opens and click the data the same data will reflected on the print page
    # print(row)
    name.set(row[1])  # selected 1 by integer
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)  # incase any address is there, it deleted and insert the new one
    txtAddress.insert(END, row[7])


def delete_employee():
    db.delete(row[0])
    clearAll()
    displayAll()


def clear_employee():
    # by using variable name
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)


# Button-Frame

btn_frame = Frame(entries_frame, bg='#a398a2')
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky='W')
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("arial", 18), bg='#1696e0',
                fg='white', border=0).grid(row=0, column=0)

btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("arial", 18), bg='#1fe609',
                 fg='white', border=0).grid(row=0, column=1, padx=10)

btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("arial", 18),
                   bg='#ed3e64',
                   fg='white', border=0).grid(row=0, column=2, padx=10)

btnClear = Button(btn_frame, command=clear_employee, text="Clear Details", width=15, font=("arial", 18), bg='#e81c15',
                  fg='white', border=0).grid(row=0, column=3, padx=10)

# Table-Frame

tree_frame = Frame(root, bg='white')
tree_frame.place(x=0, y=495, width=1536, height=520)
# to style the treeview
style = ttk.Style()
# Modify the font of the body
style.configure('mystyle.Treeview', font=('Arial', 18))
# Modify the font of the headings
style.configure('mystyle.Treeview.Heading', font=('Arial', 18))
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview", padding=10)
tv.heading('1', text="ID")
tv.column('1', width=5)
tv.heading('2', text="Name")
tv.heading('3', text="Age")
tv.column('3', width=5)
tv.heading('4', text="D.O.J")
tv.column('4', width=10)
tv.heading('5', text="Email")
tv.heading('6', text="Gender")
tv.column('6', width=10)
tv.heading('7', text="Contact")
tv.heading('8', text="Address")
tv['show'] = 'headings'
# Button Clicking function
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

# root.state("zoomed")
displayAll()
root.mainloop()
