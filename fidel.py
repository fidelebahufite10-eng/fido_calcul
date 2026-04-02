import tkinter as tk

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except:
            screen.set("Error")

    elif text == "C":
        screen.set("")

    elif text == "CE":
        screen.set(screen.get()[:-1])

    elif text == "+/-":
        value = screen.get()
        if value:
            if value[0] == "-":
                screen.set(value[1:])

    else:
        screen.set(screen.get() + text)


root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.config(bg="#5fb3b3")

screen = tk.StringVar()

entry = tk.Entry(root, textvar=screen, font=("Arial", 20),
                 bd=8, relief=tk.RIDGE, justify="right",
                 bg="#e8f6f6")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

btn_bg = "#a8dcdc"
btn_active = "#7ec8c8"

buttons = [
    ["CE", "C", "+/-", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

for row in buttons:
    frame = tk.Frame(root, bg="#5fb3b3")
    frame.pack(expand=True, fill="both", padx=5, pady=5)

    for btn in row:
        b = tk.Button(frame, text=btn,
                      font=("Arial", 14, "bold"),
                      bg=btn_bg,
                      activebackground=btn_active,
                      relief="raised",
                      bd=4)
        b.pack(side="left", expand=True, fill="both", padx=3, pady=3)
        b.bind("<Button-1>", click)

root.mainloop()