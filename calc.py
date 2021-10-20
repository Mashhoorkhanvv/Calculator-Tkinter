from tkinter import *

window = Tk()
window.title("CALCULATOR")
window.geometry('291x399')

def btn_clicked(item):
    global expression
    expression = expression + (str(item))
    input_text.set(expression)

def btn_clear(): 
    global expression 
    expression = "" 
    input_text.set("")

def btn_equal():
      global expression
      try:
          result = str(eval(expression))
          input_text.set(result)
          expression = ""
      except:
            input_text.set("ERROR")
            expression = ""
expression = ""

input_text = StringVar()

txt = Entry(window,border=20,textvariable=input_text)
txt.grid(row=0,column=0,ipadx=60,ipady=20,columnspan=30)

window.iconbitmap(r'D:\web\python\calculator\calc1.ico')

button7 = Button(window,text="7",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(7))
button7.grid(row=1,column=1)
button8 = Button(window,text="8",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(8))
button8.grid(row=1,column=2)
button9 = Button(window,text="9",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(9))
button9.grid(row=1,column=3)
button_div = Button(window,text="/",padx=25,pady=15,border=5,bg='#6e6c69',fg='black',command=lambda:btn_clicked('/'))
button_div.grid(row=1,column=4)

button4 = Button(window,text="4",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(4))
button4.grid(row=2,column=1)
button5 = Button(window,text="5",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(5))
button5.grid(row=2,column=2)
button6 = Button(window,text="6",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(6))
button6.grid(row=2,column=3)
button_mul = Button(window,text="X",padx=25,pady=15,border=5,bg='#6e6c69',fg='black',command=lambda:btn_clicked('*'))
button_mul.grid(row=2,column=4)

button1 = Button(window,text="1",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(1))
button1.grid(row=3,column=1)
button2 = Button(window,text="2",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(2))
button2.grid(row=3,column=2)
button3 = Button(window,text="3",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(3))
button3.grid(row=3,column=3)
button_sub = Button(window,text="-",padx=25,pady=15,border=5,bg='#6e6c69',fg='black',command=lambda:btn_clicked('-'))
button_sub.grid(row=3,column=4)

button_dot = Button(window,text=".",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked('.'))
button_dot.grid(row=4,column=1)
button0 = Button(window,text="0",padx=25,pady=15,border=5,bg='#a19f99',fg='black',command=lambda:btn_clicked(0))
button0.grid(row=4,column=2)
button_mod = Button(window,text="%",padx=25,pady=15,border=5,bg='#6e6c69',fg='black',command=lambda:btn_clicked('%'))
button_mod.grid(row=4,column=3)
button_add = Button(window,text="+",padx=25,pady=15,border=5,bg='#6e6c69',fg='black',command=lambda:btn_clicked('+'))
button_add.grid(row=4,column=4)



button_clr = Button(window,text="Clear",padx=15,pady=15,border=5,bg='#8ee698',fg='black',command=btn_clear)
button_clr.grid(row=5,column=1,columnspan=2,ipadx=37)

button_equal = Button(window,text="=",padx=25,pady=15,border=5,bg='#6e6c69',fg='black',command=btn_equal)
button_equal.grid(row=5,column=3,columnspan=2,ipadx=37)


mainloop()
