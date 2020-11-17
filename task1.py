"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *
win=tk.Tk()
eoutput=StringVar()


def madlib():
    Holiday=a1.get()
    Noun=a2.get()
    Place=a3.get()
    Person=a4.get()
    Adjective=a5.get()
    Body=a6.get()
    Verb=a7.get()
    Adjective2=a8.get()
    Noun2=a9.get()
    Food=a10.get()
    Plural=a11.get()
    
    story ="Im going to the "+ Noun + "!\nI can't wait to put on my "+Noun+" and swim in the "+Place+".\nThis year I got extra "+ noun+" with " + Adjective+" for my skin"+Body part+".\n Before I "+ Verb+" I make sure to grab my "+Adjective2+" "+Noun+" to hold all of my "+Food+"\nThis day should be lots of "+adjective+"
   "
    eoutput.set(story)
    
l1=Label(win,text="Enter a Holiday",)
a1=Entry(win,width=80)
l2=Label(win,text="Enter a Noun")
a2=Entry(win,width=80)
l3=Label(win,text="Enter a Place")
a3=Entry(win,width=80)
l4=Label(win,text="Enter a Person")
a4=Entry(win,width=80) 
l5=Label(win,text="Enter a Adjective")
a5=Entry(win,width=80)
l6=Label(win,text="Enter a Body Part")
a6=Entry(win,width=80)
l7=Label(win,text="Enter a Verb")
a7=Entry(win,width=80)
l8=Label(win,text="Enter another Adjective")
a8=Entry(win,width=80)
l9=Label(win,text="Enter another Noun")
a9=Entry(win,width=80)
l10=Label(win,text="Enter a type of Food")
a10=Entry(win,width=80)
l11=Label(win,text="Enter a Plural Noun")
a11=Entry(win,width=80)
b1=Button(win,text="Finalise Madlib",command=madlib)
f1=Label(win,textvariable=eoutput,width=80)

l1.grid(row=1,column=1)
a1.grid(row=1,column=2)
l2.grid(row=2,column=1)
a2.grid(row=2,column=2)
l3.grid(row=3,column=1)
a3.grid(row=3,column=2)
l4.grid(row=4,column=1)
a4.grid(row=4,column=2)
l5.grid(row=5,column=1)
a5.grid(row=5,column=2)
l6.grid(row=6,column=1)
a6.grid(row=6,column=2)
l7.grid(row=7,column=1)
a7.grid(row=7,column=2)
l8.grid(row=8,column=1)
a8.grid(row=8,column=2)
l9.grid(row=9,column=1)
a9.grid(row=9,column=2)
l10.grid(row=10,column=1)
a10.grid(row=10,column=2)
l11.grid(row=11,column=1)
a11.grid(row=11,column=2)
b1.grid(row=12,column=1)
f1.grid(row=13,column=1,columnspan=5)



win.mainloop()
