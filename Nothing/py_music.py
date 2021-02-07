import pygame
import time
import os
import tkinter
import tkinter.filedialog
import threading

root = tkinter.Tk()
root.title('音乐播放器 v0.0.1')
root.geometry('400x600+500+100')
root.resizable(False, False)

bottonchoose = tkinter.Button(root, text='添加')
bottonchoose.place(x=50,y=50,width=50,height=50)

pause_resum=tkinter.StringVar(root,value="播放")
bottonplay=tkinter.Button(root,textvariable=pause_resum)

bottonplay.place(x=100,y=100,width=100,height=100)

root.mainloop()