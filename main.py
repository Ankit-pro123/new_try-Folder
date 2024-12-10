from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'abc@gmail.com' and password == '1234':
        messagebox.showinfo('Login Successful')
    else:
        messagebox.showerror('Login Failed')


root = Tk()

# build in function...

root.title("Welcome! investment department ")
root.iconbitmap('ipo.ico')

# Menuplate size of window
# root.minsize(30,30)
# root.maxsize(400,400)
root.geometry('350x500')

# manipulate background colour 
root.configure(background= '#0096DC') ##a88165

# add image
# img = ImageTk.PhotoImage(Image.open('Project - 1/ipo.png'))

# manipulate size of photo :
img = Image.open('ipo.png')
resize_img = img.resize((100,100))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image=img)
img_label.pack(pady=(30,10))

# add text
txt_label = Label(root,text='Ipo chart',fg='white',bg='#0096DC')
txt_label.pack()
txt_label.config(font=('verdana',24))

# login form
email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=39)
email_input.pack(ipady=6,pady=(1,14))

password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root,width=39)
password_input.pack(ipady=6,pady=(1,15))

# add button

login_btn = Button(root,text='Login',fg='black',bg='white',width =10,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',12))


root.mainloop()