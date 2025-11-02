'''
1. 윈도우의 제목은 “중간고사 4번” 으로 한다.
2. 윈도우 크기는 420×440 으로 설정한다.
3. 배경이 흰색(bg="white")인 Canvas(400×320) 를 생성한다.
4. 아래 네 개의 버튼을 가로로 배치(Frame 사용) 한다.
사각형, 원, 그림, 지우기
- 각 버튼은 다음 기능을 수행해야 한다.
- 사각형 버튼: Canvas 전체를 지우고, 빨간 사각형을 그린다.
- 원 버튼: Canvas 전체를 지우고, 파란색 원(oval) 을 그린다.
- 그림 버튼: Canvas 전체를 지우고, mid_exam/duksung.png 이미지를 출력한다.
- 이미지는 Canvas의 좌측 상단(20, 20) 위치에 표시한다.
- 이미지가 사라지지 않도록 전역 변수(global) 로 관리해야 한다.
- 지우기 버튼: Canvas의 모든 도형과 이미지를 삭제한다.(canvas.delete("all") 사용)
5. Canvas 아래에는 "버튼을 눌러 도형을 선택하세요." 라는 안내 문구를 Label로 표시한다.
'''
from tkinter import *

def draw_rect():
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 150, 150, fill="red", outline="")

def draw_oval():
    canvas.delete("all")
    canvas.create_oval(200, 80, 300, 180, fill="blue", outline="")

def draw_text():
    canvas.delete("all")
    canvas.create_text(200, 150, text="Hello Tkinter", fill="blue", font=("Helvetica", 20, "bold"))

def draw_image():
    canvas.delete("all")
    global img   # 이미지가 사라지지 않도록 전역 변수로 유지
    img = PhotoImage(file="mid_exam\duksung.png")   # ⚠️ 실제 PNG 경로로 변경
    canvas.create_image(20, 20, anchor=NW, image=img)

def clear_canvas():
    canvas.delete("all")

root = Tk()
root.title("중간고사 7번")
root.geometry("420x440")

canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()

btns = Frame(root)
btns.pack(pady=8)
Button(btns, text="사각형", command=draw_rect).pack(side="left", padx=6)
Button(btns, text="원", command=draw_oval).pack(side="left", padx=6)
Button(btns, text="그림", command=draw_image).pack(side="left", padx=6)
Button(btns, text="지우기", command=clear_canvas).pack(side="left", padx=6)

Label(root, text="버튼을 눌러 도형을 선택하세요.").pack()

root.mainloop()
