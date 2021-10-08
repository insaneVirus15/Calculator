from tkinter import *

win = Tk()
win.geometry("425x278")
win.title("myCalc")
win.resizable(0,0)
win.configure(background="black")

a = StringVar()
def show(c):
    a.set(a.get()+c)

def equ():
    try:
        eq = a.get()
        a.set(eval(eq))
    except:
        a.set("Error ")

def clear():
    a.set("")
    #screen["state"]="normal"
    #ex = screen.get()
    #ex = ex[0:len(ex) - 1]
    #screen.delete(0,END)
    #screen.insert(0,ex)
    #screen["state"]="disabled"

screen = Entry(win,font=("",30),justify="right",bg="light blue",textvariable=a,state="disabled")
screen.place(x=5,y=5,width=414,height=50)

b1 = Button(win,text="7",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b1.place(x=5,y=60,width=100,height=50)
b1.configure(command=lambda:show("7"))

b2 = Button(win,text="8",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b2.place(x=110,y=60,width=100,height=50)
b2.configure(command=lambda:show("8"))

b3 = Button(win,text="9",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b3.place(x=215,y=60,width=100,height=50)
b3.configure(command=lambda:show("9"))

b4 = Button(win,text="+",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b4.place(x=320,y=60,width=100,height=50)
b4.configure(command=lambda:show("+"))


b5 = Button(win,text="4",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b5.place(x=5,y=115,width=100,height=50)
b5.configure(command=lambda:show("4"))

b6 = Button(win,text="5",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b6.place(x=110,y=115,width=100,height=50)
b6.configure(command=lambda:show("5"))

b7 = Button(win,text="6",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b7.place(x=215,y=115,width=100,height=50)
b7.configure(command=lambda:show("6"))

b8 = Button(win,text="-",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b8.place(x=320,y=115,width=100,height=50)
b8.configure(command=lambda:show("-"))


b9 = Button(win,text="1",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b9.place(x=5,y=170,width=100,height=50)
b9.configure(command=lambda:show("1"))

b10 = Button(win,text="2",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b10.place(x=110,y=170,width=100,height=50)
b10.configure(command=lambda:show("2"))

b11 = Button(win,text="3",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b11.place(x=215,y=170,width=100,height=50)
b11.configure(command=lambda:show("3"))

b12 = Button(win,text="*",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b12.place(x=320,y=170,width=100,height=50)
b12.configure(command=lambda:show("*"))


b13 = Button(win,text="C",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b13.place(x=5,y=225,width=100,height=50)
b13.configure(command=clear)

b14 = Button(win,text="0",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b14.place(x=110,y=225,width=100,height=50)
b14.configure(command=lambda:show("0"))

b15 = Button(win,text="=",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b15.place(x=215,y=225,width=100,height=50)
b15.configure(command=equ)

b16 = Button(win,text="/",font=("",25),bg="grey",fg="white",activebackground="white",activeforeground="black")
b16.place(x=320,y=225,width=100,height=50)
b16.configure(command=lambda:show("/"))

win.mainloop()