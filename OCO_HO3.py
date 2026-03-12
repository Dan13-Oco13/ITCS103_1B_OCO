import tkinter as dano

window = dano.Tk()

window.title("Calcu ni dan")
window.geometry("300x200")
window.resizable(True, True)
window.configure(bg = "grey", cursor = "hand2")

label = dano.Label(window, text = "Calculator", bg = "white", font = ("Poppins", 20))
label.pack(pady= 10)

label1 = dano.Label(window, text = "Enter the 1st Number:")
label1.place(x = 10, y = 70)

entry1 = dano.Entry(window)
entry1.place(x = 150, y = 70)

label2 = dano.Label(window, text = "Enter the 2nd Number:")
label2.place(x = 10, y = 100)

entry2 = dano.Entry(window)
entry2.place(x = 150, y = 100)

def kups():
    add = int(entry1.get())
    adds = int(entry2.get())
    result = add + adds
    label['text'] = f"Addition = {result}"

button = dano.Button(window, text = "Addition", command = kups)
button.place(x = 10, y = 150)

def kups2():
    sub = int(entry1.get())
    subs = int(entry2.get())
    result = sub - subs
    label['text'] = f"Subtract = {result}"

button = dano.Button(window, text = "Subtract", command = kups2)
button.place(x = 80, y = 150)

def kups3():
    multiply = int(entry1.get())
    mul = int(entry2.get())
    result = multiply * mul
    label['text'] = f"Multiply = {result}"

button = dano.Button(window, text = "Multiply", command = kups3)
button.place(x = 150, y = 150)

def kups4():
    divide = int(entry1.get())
    div = int(entry2.get())
    result = divide / div
    label['text'] = f"Divide = {result}"

button = dano.Button(window, text = "Division", command = kups4)
button.place(x = 220, y = 150)

window.mainloop()
