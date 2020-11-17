"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
from tkinter import *
import math

win=tk.Tk()
win.title("Factoring Trinomials")
eoutput =StringVar()
variable1 =StringVar()
variable2 =StringVar()
factor1 =StringVar()
factor2 =StringVar()

def factor():
    a =1
    b =a1.get()
    c =a2.get()
    b =int(b)
    c =int(c)
    d =variable1.get()
    e =variable2.get()
    if d =="+":
        b =b*1
    elif d =="-":
        b =b*-1
    if e =="+":
        c =c*1
    elif e =="-":
        c =c*-1
    x=(((b*-1) + math.sqrt(b**2 -(4 *c)))/2)
    y=(((b*-1) - math.sqrt(b**2 -(4 * c)))/2)
    if x<0:
        factor1.set("(x + "+str(abs(x))+')')
    if y<0:
        factor2.set('(x + '+str(abs(y))+')')
    if x==0:
        factor1.set('(0)')
    if y==0:
        factor2.set('(0)')
    if x>0:
        factor1.set('(x - '+str(abs(x))+')')
    if y>0:
        factor2.set('(x - '+str(abs(y))+')')
    eoutput.set(str(factor1.get())+str(factor2.get()))

l1=Label(win,text="bx value")
l2=Label(win,text="c value")
l3=Label(win,text="ax value is always equal to 1")
a1=Entry(win,width=40)
a2=Entry(win,width=40)
x1=OptionMenu(win,variable1,"+","-")
x2=OptionMenu(win,variable2,"+","-")
b1=Button(win,text="Factor",command=factor)
f1=Label(win,textvariable=eoutput)

l1.grid(row=1,column=1,sticky=E)
a1.grid(row=1,column=2,sticky=W)
l2.grid(row=2,column=1,sticky=E)
a2.grid(row=2,column=2,sticky=W)
x1.grid(row=1,column=3,)
x2.grid(row=2,column=3,)
b1.grid(row=3,column=1)
f1.grid(row=4,column=1)
win.mainloop()
