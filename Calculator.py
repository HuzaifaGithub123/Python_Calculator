from cProfile import label
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN

def button_press(num):

      global equation_text
      equation_text = equation_text + str(num)
      equation_label.set(equation_text)


def equals():
    
    global equation_text

    try:

       total = str (eval(equation_text))
       equation_label.set(total)
       equation_text = total

    except SyntaxError:

        equation_label.set("SYNTAX ERROR")

    except ZeroDivisionError:

        equation_label.set("ARITHMETIC ERROR")

def clear():
    
    equation_label.set("")
    global equation_text 
    equation_text =  ""

window = Tk()
window.title("Calculator program")
window.geometry("500x500")


equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=36, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3,column=0)



buttonplus = Button(frame, text="+", height=4, width=7,font=35,background="red", command=lambda: button_press('+'))
buttonplus.grid(row=0,column=3)

buttonminus = Button(frame,text="-",height=4,width=7,font=35,background="red",command=lambda:button_press('-'))
buttonminus.grid(row=1,column=3)

buttonmultiply = Button(frame,text="*",height=4,width=7,font=35,background="red",command=lambda:button_press('*'))
buttonmultiply.grid(row=2,column=3)

buttondivide = Button(frame,text="/",height=4,width=7,font=35,background="red",command=lambda: button_press('/'))
buttondivide.grid(row=3,column=3)


buttonclear = Button(frame,text="C",height=4,width=9,font=35,background="red",command=clear)
buttonclear.grid(row=3,column=2)

buttonequals = Button(frame,text="=",height=4,width=9,font=35,background="red",command=equals)
buttonequals.grid(row=3,column=1) 


window.mainloop()


 

