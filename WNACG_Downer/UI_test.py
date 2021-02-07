import tkinter as tk
import time

window = tk.Tk()
window.title("a")
window.geometry('800x500')

canvas = tk.Canvas(window, width=500, height=300, bg='grey')
canvas.place(x=0, y=0)

canvas.create_rectangle(5,5,105,25,outline='blue',width=1)

def add_some(prec):
    canvas.create_rectangle(5,5,1.05*int(prec),25,width=0,fill='red')

def move_r():
    global e
    e=en_b.get()

en_b=tk.Entry(window)
en_b.place(y=300,x=0)

e=tk.StringVar()



btn=tk.Button(window,width=20,command=lambda:add_some(e),text="add_some")
btn.place(x=0,y=350)

btn_1=tk.Button(window,width=20,command=move_r,text="get")
btn_1.place(x=0,y=380)


window.mainloop()
