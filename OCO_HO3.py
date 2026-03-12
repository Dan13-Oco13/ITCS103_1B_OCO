import tkinter as dano

window = dano.Tk()

window.title("Calcu ni dan")
window.geometry("300x200")
window.resizable(True, True)
window.configure(bg = "grey", cursor = "hand2")

label = dano.Label(window, text = "Calculator", bg = "white", font = ("Poppins", 20))
label.pack(pady= 20)

label1 = dano.Label(window, text = "Enter 1st Number:")
label1.place(x = 10, y = 50)

entry1 = dano.Entry(window)
entry1.place(x = 120, y = 50)

label2 = dano.Label(window, text = "Enter 2nd Number:")
label2.place(x = 10, y = 80)

entry2 = dano.Entry(window)
entry2.place(x = 120, y = 80)

def kups():
    plus = int(entry1.get())
    plus2 = int(entry2.get())
    result = plus + plus2
    label['text'] = f"🐼 {plus} + {plus2} = {result} 🐼"

button = dano.Button(window, text = "Addition", command = kups)
button.place(x = 150, y = 200)

def kups2():
    minus = int(entry1.get())
    minus2 = int(entry2.get())
    result = minus - minus2
    label['text'] = f"🐼 {minus} + {minus2} = {result} 🐼"

button = dano.Button(window, text = "Subtract", command = kups2)
button.place(x = 250, y = 200)

def kups3():
    mul = int(entry1.get())
    mult = int(entry2.get())
    result = mul * mult
    label['text'] = f"🐼 {mul} + {mult} = {result} 🐼"

button = dano.Button(window, text = "Multiply", command = kups3)
button.place(x = 150, y = 250)

def kups4():
    div = int(entry1.get())
    divi = int(entry2.get())
    result = div / divi
    label['text'] = f"🐼 {div} + {divi} = {result} 🐼"

button = dano.Button(window, text = "Division", command = kups4)
button.place(x = 250, y = 250)

window.mainloop()
