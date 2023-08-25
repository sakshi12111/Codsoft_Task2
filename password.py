import random
import tkinter
import pyperclip
from tkinter import ttk
from tkinter import messagebox

root=tkinter.Tk()
root.title("PASSWORD GENERATOR")
root.geometry("550x470")
root.configure(bg="white")

def generate_pw():
    password="ABCDEFGHIJKLMNOPQRSTUVWXYZ123467890abcdefghijklmnopqrstuvwxyz()!@#$%^&*?/][+-_~`"
    len_password=int(enter_len.get())
    a="".join(random.sample(password,len_password))
    enter_gp.insert(0,a)
    
def accept_pw():
    random_p=enter_gp.get()
    pyperclip.copy(random_p)
    tkinter.messagebox.showinfo(title="SUCCESS",message="Password copied to clipboard!")

def reset_pw():
    enter_gp.delete(0,'end')

text=tkinter.Label(text="Welcome to Password Generator!",font=("Times New Roman",20,"bold","underline"),fg="darkblue")
text.place(x=70,y=10)

text2=tkinter.Label(text="Enter your name:",font=("Times New Roman",15),fg="black")
text2.place(x=15,y=90)

enter_name=tkinter.Entry(root,width=20,font=("Times New Roman",15))
enter_name.place(x=200,y=90)

text3=tkinter.Label(text="Enter password length:",font=("Times New Roman",15),fg="black")
text3.place(x=15,y=130)

enter_len=tkinter.Entry(root,width=20,font=("Times New Roman",15))
enter_len.place(x=200,y=130)

text4=tkinter.Label(text="Generated Password:",font=("Times New Roman",15),fg="black")
text4.place(x=15,y=170)

enter_gp=tkinter.Entry(root,text="{a}",width=20,font=("Times New Roman",15))
enter_gp.place(x=200,y=170)

button_gp=tkinter.Button(root,text="GENERATE PASSWORD",width=25,height=1,bg="darkblue",fg="white",font=("Times New Roman",12,"bold"),command=generate_pw)
button_gp.place(x=170,y=230)

button_accept=tkinter.Button(root,text="ACCEPT",width=15,height=1,fg="darkblue",font=("Times New Roman",12,"bold"),command=accept_pw)
button_accept.place(x=210,y=300)

button_reset=tkinter.Button(root,text="RESET",width=15,height=1,fg="darkblue",font=("Times New Roman",12,"bold"),command=reset_pw)
button_reset.place(x=210,y=370)

root.mainloop()