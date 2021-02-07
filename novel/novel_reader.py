from tkinter import *
from tkinter.scrolledtext import ScrolledText


def load():
    if filename.get() != '':
        with open(filename.get()) as file:
            contents.delete('1.0', END)
            contents.insert(INSERT, file.read())
    else:
        print('路径错误!')


def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))


top = Tk()
top.title("Novel_Reader")

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)

top.mainloop()