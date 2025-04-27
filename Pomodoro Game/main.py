from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 5
reps = 0
mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer, reps, mark
    window.after_cancel(timer)
    timer_label.config(text="TIMER", fg=GREEN)
    canva.itemconfig(counter, text="00:00")
    reps = 0
    mark = ""
    checkmark.config(text=mark)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=RED)
     

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global mark, timer

    count_min = math.floor(count / 60)
    count_sec = int(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canva.itemconfig(counter, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            mark += "✅"
        checkmark.config(text=mark)
        start()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canva = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
canva_img = PhotoImage(file="tomato.png")
canva.create_image(105, 112, image=canva_img, )
counter = canva.create_text(105, 130, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canva.grid(row=1 , column=1)

start_btn = Button(text="Start", command=start, font=(FONT_NAME, 10, "normal"), fg=RED, borderwidth=0, bg=GREEN)
start_btn.grid(row=2 , column=0)

reset_btn = Button(text="Reset", command=reset, font=(FONT_NAME, 10, "normal"), fg=RED, borderwidth=0, bg=GREEN)
reset_btn.grid(row=2 , column=2)

checkmark = Label(fg=GREEN, bg=YELLOW,pady=20)
checkmark.grid(row=2, column=1)


window.mainloop()