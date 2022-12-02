# 라이브러리 import
from tkinter import*
import os #운영체체기능쓰는 라이브러리


#끄기
def logout():
    return os.system("shutdown -l")
#재시작
def restart():
    return os.system("shutdown /r /t 1")
#사용자 로그아웃
def shutdown():
    return os.system("shutdown /s /t 1")

tk = Tk()
tk.geometry("100x100")  # GUI 화면 크기 지정

# 버튼을 통해 해당 버튼 클릭시 함수 실행
Button(tk, text = "강제종료", command = logout).place(x = 20, y = 10)
Button(tk, text = "다시시작", command = restart).place(x = 25, y = 40)
Button(tk, text = "로그아웃", command = shutdown).place(x = 20, y = 70)

mainloop()