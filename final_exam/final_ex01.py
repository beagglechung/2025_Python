import tkinter as tk
import random
class DrawableShape:
    def __init__(self, canvas):
        self.canvas = canvas
        self.shape_id = None

    def draw(self):
        raise NotImplementedError("draw() must be overridden.")

class Square(DrawableShape):
    def __init__(self, canvas, x, y, size):
        super().__init__(canvas)
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.size
        y2 = self.y + self.size
        self.shape_id = self.canvas.create_rectangle(x1, y1, x2, y2)

class Circle(DrawableShape):
    def __init__(self, canvas, x, y, radius):
        super().__init__(canvas)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        x1 = self.x - self.radius
        y1 = self.y - self.radius
        x2 = self.x + self.radius
        y2 = self.y + self.radius
        self.shape_id = self.canvas.create_oval(x1, y1, x2, y2)

# 도형 리스트
shapes = []

def update_info_label():
    """현재까지 생성된 도형 정보를 왼쪽 위에 표시."""
    info_text = "생성된 도형 목록:\n"
    for idx, s in enumerate(shapes, start=1):
        if isinstance(s, Square):
            info_text += f"{idx}. Square - x:{s.x}, y:{s.y}, size:{s.size}\n"
        elif isinstance(s, Circle):
            info_text += f"{idx}. Circle - x:{s.x}, y:{s.y}, radius:{s.radius}\n"

    info_label.config(text=info_text)

def add_square():
    size = random.randint(20, 80)
    x = random.randint(0, 400 - size)
    y = random.randint(0, 300 - size)
    square = Square(canvas, x, y, size)
    shapes.append(square)
    update_info_label()

def add_circle():
    radius = random.randint(10, 40)
    x = random.randint(radius, 400 - radius)
    y = random.randint(radius, 300 - radius)
    circle = Circle(canvas, x, y, radius)
    shapes.append(circle)
    update_info_label()

def draw_all():
    for s in shapes:
        s.draw()

# GUI 구성
root = tk.Tk()
root.title("문제 1")

frame_left = tk.Frame(root)
frame_left.pack(side="left", padx=10, pady=10)

info_label = tk.Label(frame_left, text="생성된 도형 목록:\n", justify="left")
info_label.pack()

frame_right = tk.Frame(root)
frame_right.pack(side="right", padx=10, pady=10)

canvas = tk.Canvas(frame_right, width=400, height=300, bg="white")
canvas.pack(pady=10)

btn_frame = tk.Frame(frame_right)
btn_frame.pack()

btn_add_square = tk.Button(btn_frame, text="사각형 추가", command=add_square)
btn_add_square.pack(side="left", padx=5)

btn_add_circle = tk.Button(btn_frame, text="원 추가", command=add_circle)
btn_add_circle.pack(side="left", padx=5)

btn_draw_all = tk.Button(btn_frame, text="모두 그리기", command=draw_all)
btn_draw_all.pack(side="left", padx=5)

root.mainloop()
