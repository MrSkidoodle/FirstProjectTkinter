import tkinter as tk

form = tk.Tk()
form.title("mama")
fullStringVar = tk.StringVar()

def setfullname():
    f_name = firstEntry.get()
    s_name = secondEntry.get()
    fullStringVar.set(f_name + " " + s_name)


firstLabel = tk.Label(form, text="First Name:")
firstLabel.grid(row=0,
                column=0,
                padx=15,
                pady=15)
firstEntry = tk.Entry(form)
firstEntry.grid(row=0,
                column=1,
                padx=15,
                pady=15)
secondLabel = tk.Label(form, text="Surname:")
secondLabel.grid(row=1,
                 column=0,
                 padx=15,
                 pady=15)
secondEntry = tk.Entry(form)
secondEntry.grid(row=1,
                 column=1,
                 padx=15,
                 pady=15)

btnFullName = tk.Button(form, text="Full Name", command=setfullname)

fullnameLabel = tk.Label(form, text="Fullname:")
fullnameLabel.grid(row=2,
                 column=0,
                 padx=15,
                 pady=15)
fullNameEntry = tk.Entry(form,textvariable=fullStringVar)
fullNameEntry.grid(row=2,
                 column=1,
                 padx=15,
                 pady=15)
btnFullName.grid(columnspan=2,
                 padx=15,
                 pady=15)

form.mainloop()
