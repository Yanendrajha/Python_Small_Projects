import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✓"
        check_marks.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = str(f"0{min}")
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    print(count)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)
# Top title label

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50,))
title_label.grid(column=1, row=0)

# start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check marks

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# Canvas Descriptions

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
