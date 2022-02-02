from tkinter import *
import sys
def clear():
    expentry.delete(0,END)
    resentry.delete(0,END)
def zero():
    expentry.insert(END, "0")
def dot():
    expentry.insert(END, ".")
def one():
    expentry.insert(END, "1")
def two():
    expentry.insert(END, "2")
def three():
    expentry.insert(END, "3")
def plus():
    expentry.insert(END, "+")
def four():
    expentry.insert(END, "4")
def five():
    expentry.insert(END, "5")
def six():
    expentry.insert(END, "6")
def minus():
    expentry.insert(END, "-")
def mul():
    expentry.insert(END, "*")
def seven():
    expentry.insert(END, "7")
def eight():
    expentry.insert(END, "8")
def nine():
    expentry.insert(END, "9")
def div():
    expentry.insert(END, "/")
def leftpar():
    expentry.insert(END, "(")
def rightpar():
    expentry.insert(END, ")")
def delete():
    expentry.delete(len(expentry.get())-1, END)
def equal():
    expression=expentry.get()
    try:
        result=eval(expression)
        resentry.delete(0,END)
        resentry.insert(0,result)
    except ZeroDivisionError:
        resentry.insert(0, "Math Error")
    except:
        if(sys.exc_info()[0].__name__)=="SyntaxError":
            resentry.insert(0, "Syntax Error")

window=Tk()
window.geometry("335x470")
window.title("Calculator")
expentry=Entry(window,
                font=("Arial", 20),
                width=19)
expentry.place(x=22,y=10)
resentry=Entry(window,
                font=("Arial",30),
                width=13)
resentry.place(x=22, y=55)
clearbutton=Button(window,
                    text="C",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=clear)
clearbutton.place(x=25, y=390)
zerobutton=Button(window,
                    text="0",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=zero)
zerobutton.place(x=100, y=390)
dotbutton=Button(window,
                    text=".",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=dot)
dotbutton.place(x=175, y=390)
plusbutton=Button(window,
                    text="+",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=plus)
plusbutton.place(x=250, y=390)
onebutton=Button(window,
                    text="1",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=one)
onebutton.place(x=25, y=320)
twobutton=Button(window,
                    text="2",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=two)
twobutton.place(x=100, y=320)
threebutton=Button(window,
                    text="3",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=three)
threebutton.place(x=175, y=320)
minusbutton=Button(window,
                    text="-",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=minus)
minusbutton.place(x=250, y=320)
fourbutton=Button(window,
                    text="4",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=four)
fourbutton.place(x=25, y=250)
fivebutton=Button(window,
                    text="5",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=five)
fivebutton.place(x=100, y=250)
sixbutton=Button(window,
                    text="6",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=six)
sixbutton.place(x=175, y=250)
multbutton=Button(window,
                    text="*",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=mul)
multbutton.place(x=250, y=250)
sevenbutton=Button(window,
                    text="7",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=seven)
sevenbutton.place(x=25, y=180)
eightbutton=Button(window,
                    text="8",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=eight)
eightbutton.place(x=100, y=180)
ninebutton=Button(window,
                    text="9",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=nine)
ninebutton.place(x=175, y=180)
divbutton=Button(window,
                    text="/",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=div)
divbutton.place(x=250, y=180)
equalbutton=Button(window,
                    text="=",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=equal)
equalbutton.place(x=25, y=110)
leftparbutton=Button(window,
                    text="(",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=leftpar)
leftparbutton.place(x=100, y=110)
rightparbutton=Button(window,
                    text=")",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=rightpar)
rightparbutton.place(x=175, y=110)
delbutton=Button(window,
                    text="Del",
                    font=("Arial",20),
                    height=1,
                    width=3,
                    command=delete)
delbutton.place(x=250, y=110)
window.mainloop()
