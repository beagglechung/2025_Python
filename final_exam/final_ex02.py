import tkinter as tk

# ------------------- 클래스 정의 -------------------
class Person:
    def __init__(self, name: str):
        self.name = name

class HobbyPerson(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.hobbies = []  # 선택 결과를 리스트로 저장 (일관성 유지)

    def add_hobby(self, h: str):
        self.hobbies = [h]   # 라디오 버튼이므로 1개만 저장

    def clear_hobbies(self):
        self.hobbies.clear()

# ------------------- Tkinter GUI -------------------
root = tk.Tk()
root.title("문제 2")
root.geometry("380x200")

hp = HobbyPerson("김덕성")

title = tk.Label(root, text=f"이름: {hp.name}", font=("맑은 고딕", 11, "bold"))
title.pack(pady=6)

frm = tk.Frame(root)
frm.pack(pady=8)

# ------------------- RadioButton 변수 -------------------
# 선택된 취미를 저장하는 변수 (문자열 변수)
selected_hobby = tk.StringVar(value="none")  

# Radiobutton 3개  
rb1 = tk.Radiobutton(frm, text="게임",  value="게임",  variable=selected_hobby)
rb2 = tk.Radiobutton(frm, text="독서",  value="독서",  variable=selected_hobby)
rb3 = tk.Radiobutton(frm, text="운동",  value="운동",  variable=selected_hobby)

rb1.grid(row=0, column=0, padx=10, pady=4)
rb2.grid(row=0, column=1, padx=10, pady=4)
rb3.grid(row=0, column=2, padx=10, pady=4)

# 결과 표시 라벨
msg = tk.StringVar(value="취미를 선택하고 [등록하기]를 누르세요.")
lb = tk.Label(root, textvariable=msg, wraplength=340, justify="left")
lb.pack(pady=8)

# ------------------- 동작 함수 -------------------
def register_hobby():
    hp.clear_hobbies()

    hobby = selected_hobby.get()

    if hobby:
        hp.add_hobby(hobby)
        msg.set(f"현재 선택된 취미: {hobby}")
    else:
        msg.set("선택된 취미가 없습니다.")


def reset_all():
    selected_hobby.set("")   # 라디오버튼 선택 해제
    hp.clear_hobbies()
    msg.set("모든 선택을 해제했습니다.")


# 버튼 영역
btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

tk.Button(btn_frame, text="등록하기", command=register_hobby).pack(side="left", padx=8)
tk.Button(btn_frame, text="초기화",   command=reset_all).pack(side="left", padx=8)

root.mainloop()
