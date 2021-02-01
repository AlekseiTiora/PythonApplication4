from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import sys,fileinput
from tkinter.messagebox import *
root=Tk()
root.geometry("400x300")
root.title("Описание машин")

tabs=ttk.Notebook(root)

texts=["Esimene","Teine","Kolmas","Neljas"]



def image_A6():
    global img
    img=PhotoImage(file="A6.png").subsample(2)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()

def image_rsq3():
    global img
    img=PhotoImage(file="rsq3.png").subsample(8)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 12", bd=5,text="Описание")
    btn.pack()

def image_Q5():
    global img
    img=PhotoImage(file="Q5.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()

def image_A7():
    global img
    img=PhotoImage(file="A7.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()

def image_f90():
    global img
    img=PhotoImage(file="f90.png").subsample(7)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()

def image_e60():
    global img
    img=PhotoImage(file="e60.png").subsample(3)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()

def image_m4():
    global img
    img=PhotoImage(file="m4.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()

def image_e():
    global img
    img=PhotoImage(file="e.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()

def image_c():
    global img

    img=PhotoImage(file="c.png").subsample(5)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()

def image_s():
    global img

    img=PhotoImage(file="s.png").subsample(2)
    can.create_image(10,10,image=img,anchor=NW)
    btn=Button(root, font="Arial 13", bd=5,text="Описание")
    btn.pack()


 
#for i in range(4): #len(text)
#    tab1=Frame(tabs)
#    tabs.add(tab1,text=texts[i])
tab1=Frame(tabs)
tabs.add(tab1,text="Автомобили")
tabs.pack()

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Audi",menu=m1)
m1.add_command(label="A6",command=lambda:image_A6())
m1.add_command(label="RSQ3",command=lambda:image_rsq3())
m1.add_command(label="Q5",command=lambda:image_Q5())
m1.add_command(label="A7",command=lambda:image_A7())
m1.add_separator()


m2=Menu(M,tearoff=2)
M.add_cascade(label="Bmw",menu=m2)
m2.add_command(label="M5F90",command=lambda:image_f90())
m2.add_command(label="E60",command=lambda:image_e60())
m2.add_command(label="M4",command=lambda:image_m4())



can=Canvas(tab1,width=300,height=200)
can.pack()

m3=Menu(M,tearoff=3)
M.add_cascade(label="Mercedes",menu=m3)
m3.add_command(label="e-class",command=lambda:image_e())
m3.add_command(label="c-class",command=lambda:image_c())
m3.add_command(label="s-class",command=lambda:image_s())

btn=Button




tabs.pack(fill="both")

root.mainloop()
