import tkinter as tk
window = tk.Tk()

window.title("Dan's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="beige",cursor="hand2")

label = tk.Label(window,text="MY PROFILE",font=("Poppins",35,"italic"),fg="pink",bg="beige",anchor="center")
label.pack(padx=5,pady=20)

label = tk.Label(window,text="name : Daniel oco ",font=("serif",12,"italic"),fg="pink",bg="beige")
label.pack(anchor="w")

label = tk.Label(window,text="Age : 19",font=("serif",12,"italic"),fg="pink",bg="beige")
label.pack(anchor="w")

label = tk.Label(window,text="Course : BSIT",font=("serif",12,"italic"),fg="pink",bg="beige")
label.pack(anchor="w")

label = tk.Label(window,text="Birth Day : December 1, 2006",font=("serif",12,"Italic"),fg="pink",bg="beige")
label.pack(anchor="w")

label = tk.Label(window,text="Motto: Continue your dreams keep sleeping.",font=("serif",12,"Italic"),fg="pink",bg="beige")
label.pack(anchor="w")

window.mainloop()
