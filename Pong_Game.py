from tkinter import *
import Display

root = Tk()
root.title("Pong Game")
root.configure(bg='black')
root.geometry("500x320")

frame = LabelFrame(root, padx=20,pady=30, background='Black')
frame.pack(padx=20,pady=20)
my_label = Label(frame , text="Welcome \n Let's play Pong!!",font=("Courier",20),anchor='center',bg='black',fg='cyan',padx=20,pady=40)
my_label.grid(row=0,column=1)
b = Button(frame,text="Start",bg='black',font=("Courier",16),fg='white',padx=20,pady=20,command=Display.pong)
#b1 = Button(frame,text="Dont click this")

b.grid(row=2,column=1)
#b1.grid(row=2,column=2)

root.mainloop()