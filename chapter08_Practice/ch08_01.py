import tkinter as tk
import random

def move_shape(dx, dy):
    canvas.move(shape, dx, dy)

def move_up(event):
    move_shape(0, -10)

def move_down(event):
    move_shape(0, 10)

def move_left(event):
    move_shape(-10, 0)

def move_right(event):
    move_shape(10, 0)

def change_color(event):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    color = random.choice(colors)
    canvas.itemconfig(shape, fill=color)

# 애플리케이션 초기 설정
root = tk.Tk()
root.title("Moving Shape App")

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

shape = canvas.create_oval(100, 100, 200, 200, fill="blue")  # 초기 원 생성

# 키보드 이벤트 처리
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# 마우스 이벤트 처리
canvas.bind("<B1-Motion>", change_color)

# 애플리케이션 실행
root.mainloop()
