from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import sys,fileinput
from tkinter.messagebox import *
root=Tk()
root.geometry("1200x720")
root.title("Описание машин")

tabs=ttk.Notebook(root)




def image_A6():
    global img
    img=PhotoImage(file="A6.png").subsample(1)
    can.create_image(10,10,image=img,anchor=NW)


def image_rsq3():
    global img
    img=PhotoImage(file="rsq3.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)
    


def image_f90():
    global img
    img=PhotoImage(file="f90.png").subsample(4)
    can.create_image(10,10,image=img,anchor=NW)

def image_e60():
    global img
    img=PhotoImage(file="e60.png").subsample(2)
    can.create_image(10,10,image=img,anchor=NW)

def image_bmw():
    global img
    img=PhotoImage(file="bmw.png").subsample (1)
    can.create_image(10,15,image=img,anchor=NW)

def image_bmw1():
    global img
    img=PhotoImage(file="bmw1.png").subsample (1)
    can.create_image(10,15,image=img,anchor=NW)

def image_audi():
    global img
    img=PhotoImage(file="audi.png").subsample (1)
    can.create_image(10,15,image=img,anchor=NW)

def image_audi1():
    global img
    img=PhotoImage(file="audi1.png").subsample (1)
    can.create_image(10,15,image=img,anchor=NW)






tab1=Frame(tabs)
tabs.add(tab1,text="Автомобили")
tabs.pack()

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Audi",menu=m1)
m1.add_command(label="A6",command=lambda:image_A6())
m1.add_command(label="RSQ3",command=lambda:image_rsq3())




m2=Menu(M,tearoff=2)
M.add_cascade(label="Bmw",menu=m2)
m2.add_command(label="M5F90",command=lambda:image_f90())
m2.add_command(label="E60",command=lambda:image_e60())

m3=Menu(M,tearoff=2)
M.add_cascade(label="Характеристики",menu=m3)
m3.add_command(label="M5F90",command=lambda:image_bmw())
m3.add_command(label="E60",command=lambda:image_bmw1())
m3.add_command(label="audi A6",command=lambda:image_audi())
m3.add_command(label="Audi rsq3",command=lambda:image_audi1())





can=Canvas(tab1,width=1200,height=720)
can.pack()







tabs.pack(fill="both")

root.mainloop()
