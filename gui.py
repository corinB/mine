from tkinter import*
import tkinter as tkr
#생성
tk = Tk()
tk.geometry("1000x100")
tk.title("어따보낼껀데?")
glabel = Label(tk, text="이메일을 적어라")
glabel.place(x =400, y = 10 )

entry = Entry(tk) #입력창 생성
entry.place(x=400,y=30)# 입력창 배치


tk.mainloop()
