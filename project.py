import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("500x600")
root.title("S.A.Calculator")
def click(event):
    global calculator
    text = event.widget.cget("text")

    if text == "=":
        if calculator.get().isdigit():
            value = int(calculator.get())
        else:
            value = eval(calculator.get())
        calculator.set(value)
    elif text == "C":
        calculator.set("")
    else:
        calculator.set(calculator.get() + text)

calculator = tk.StringVar()
calculator.set("")
Screen = tk.Entry(root,textvar=calculator, font = "Calibri 35 bold")
Screen.pack(fill='x', ipadx=15, ipady=15, padx=15, pady=15)
Frame = tk.Frame (root, bg = "grey")
Button = tk.Button(Frame, text='9', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)


Button = tk.Button(Frame, text='8', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='7', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Frame.pack(side="top",anchor="ne")

Frame = tk.Frame (root, bg = "grey")
Button = tk.Button(Frame, text='6', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='5', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='4', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Frame.pack(side="top",anchor="ne")

Frame = tk.Frame (root, bg = "grey")
Button = tk.Button(Frame, text='3', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='2', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='1', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Frame.pack(side="top",anchor="ne")


Frame = tk.Frame (root, bg = "grey")
Button = tk.Button(Frame, text='00', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=18, pady=18)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='=', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=10, pady=10)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='+', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "left", padx=10, pady=10)
Button.bind("<Button-1>", click)

Frame.pack(side="top",anchor="ne")

Frame = tk.Frame (root, bg = "grey")
Button = tk.Button(Frame, text='-', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "right", padx=25, pady=25)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='*', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "right", padx=25, pady=25)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='/', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "right", padx=25, pady=25)
Button.bind("<Button-1>", click)

Button = tk.Button(Frame, text='C', font = "Calibri 18 bold", padx=18, pady=18)
Button.pack(side = "right", padx=25, pady=25)
Button.bind("<Button-1>", click)

Frame.pack(side="top",anchor="nw")




root.mainloop()
