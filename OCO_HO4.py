import tkinter as dan

window = dan.Tk()

window.title("Profile Builder")
window.geometry("570x320")
window.resizable(True, True)
window.configure(bg = "beige", cursor = "hand2")

label = dan.Label(window, text = "Profile Builder", bg = "beige", font = ("poppins", 20))
label.pack(padx = 10)

frame = dan.Frame(window, bd = 2, bg = "Light Blue", width = 675, height = 150)
frame.place(x = 1, y = 40)

label1 = dan.Label(window, text = "First Name", bg = "Light Blue", font = ("Agency", 11))
label1.place(x = 35, y = 70)

entry1 = dan.Entry(window)
entry1.place(x = 10, y = 50)

label2 = dan.Label(window, text = "Middle Name", bg = "Light Blue", font = ("Agency", 11))
label2.place(x = 245, y = 70)

entry2 = dan.Entry(window)
entry2.place(x = 225, y = 50)

label3 = dan.Label(window, text = "Last Name", bg = "Light Blue", font = ("Agency", 11))
label3.place(x = 445, y = 70)

entry3 = dan.Entry(window)
entry3.place(x = 420, y = 50)

label4 = dan.Label(window, text = "Birth Year", bg = "Light Blue", font = ("Agency", 11))
label4.place(x = 35, y = 130)

entry4 = dan.Entry(window)
entry4.place(x = 10, y = 110)

label4 = dan.Label(window, text = "Gender", bg = "Light Blue", font = ("Agency", 11))
label4.place(x = 40, y = 160)

label4 = dan.Label(window, text = "Male", bg = "Light Blue", font = ("Agency", 11))
label4.place(x = 260, y = 160)

radio_btn = dan.Radiobutton(window, bg = "Light Blue")
radio_btn.place(x = 230, y = 160)

label5 = dan.Label(window, text = "Female", bg = "Light Blue", font = ("Agency", 11))
label5.place(x = 370, y = 160)

radio_btn = dan.Radiobutton(window, bg = "Light Blue")
radio_btn.place(x = 340, y = 160)

label5 = dan.Label(window, text = "Submit", bg = "Light Blue", font = ("Agency", 20))
label5.place(x = 250, y = 230)

window.mainloop()
