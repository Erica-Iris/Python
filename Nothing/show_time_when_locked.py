from datetime import datetime
import tkinter as tk



dt=datetime.now()

# print(dt.strftime('%H:%M'))

time_shower=tk.Tk()
h=time_shower.winfo_screenheight()
w=time_shower.winfo_screenwidth()


time_shower.geometry('%dx%d' % (w,h))
time_label=tk.Label(time_shower,text=dt.strftime('%H:%M'),font=('A'))
time_label.pack()
time_shower.mainloop()