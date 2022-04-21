from tkinter import*
from tkinter import messagebox

root = Tk()
root.title('Login Screen')
root.geometry('500x200+200+200')

def login() :
    if username.get()=='admin' and password.get()=='admin' :
        messagebox.showinfo(title='Login status', message='Log in successful!')
    else :
        messagebox.showerror(title='Error! ', message='Username/Password incorrect')

def cancel() :
    cl = messagebox.askquestion(title='Exit', message='Do you want to exit?')
    if cl == 'yes' :
        root.destroy()

l1 = Label(root, text = 'USERNAME :')
l2 = Label(root, text = 'PASSWORD :')
l1.grid(row=0,column=0,padx=10,pady=10)
l2.grid(row=1,column=0,padx=10,pady=10)

username = StringVar()
password = StringVar()

t1 = Entry(root, text = username)
t2 = Entry(root, text = password, show = '*')
t1.grid(row=0, column=1)
t2.grid(row=1,column=1)

btn1 = Button(root, text='Login', fg='blue', width=5, command=login)
btn2 = Button(root, text='Cancel', fg = 'red', width=5, command=cancel)
btn1.grid(row=2, column=1, sticky=W)
btn2.grid(row=2, column=1, sticky=E)


root.mainloop()