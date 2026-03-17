import tkinter as tk
from tkinter import PhotoImage
from datetime import datetime

# Main window
root = tk.Tk()
root.title("Student Profile Builder")
root.geometry("400x500")

# Function to compute age
def compute_age(event):
    try:
        birth_year = int(entry_birth.get())
        current_year = datetime.now().year
        age = current_year - birth_year
        age_label.config(text="Age: " + str(age))
    except:
        age_label.config(text="Invalid Year")

# Function to change background based on gender
def set_gender_color():
    gender = gender_var.get()
    if gender == "Male":
        root.config(bg="lightblue")
    elif gender == "Female":
        root.config(bg="lightpink")

# Hover effect for button
def on_enter(e):
    submit_btn.config(bg="gray")

def on_leave(e):
    submit_btn.config(bg="SystemButtonFace")

# Function to generate ID card
def generate_id():
    id_window = tk.Toplevel(root)
    id_window.title("Student ID")
    id_window.geometry("300x200")

    frame = tk.Frame(id_window, bd=2, relief="solid")
    frame.pack(padx=10, pady=10, fill="both", expand=True)

    full_name = entry_fname.get() + " " + entry_mname.get() + " " + entry_lname.get()

    tk.Label(frame, text="STUDENT ID", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(frame, text="Name: " + full_name).pack()
    tk.Label(frame, text="Gender: " + gender_var.get()).pack()
    tk.Label(frame, text=age_label.cget("text")).pack()

# Frame
frame_main = tk.Frame(root)
frame_main.pack(pady=20)

# Labels and Entries
tk.Label(frame_main, text="First Name").grid(row=0, column=0)
entry_fname = tk.Entry(frame_main)
entry_fname.grid(row=0, column=1)

tk.Label(frame_main, text="Middle Name").grid(row=1, column=0)
entry_mname = tk.Entry(frame_main)
entry_mname.grid(row=1, column=1)

tk.Label(frame_main, text="Last Name").grid(row=2, column=0)
entry_lname = tk.Entry(frame_main)
entry_lname.grid(row=2, column=1)

tk.Label(frame_main, text="Birth Year").grid(row=3, column=0)
entry_birth = tk.Entry(frame_main)
entry_birth.grid(row=3, column=1)

entry_birth.bind("<Return>", compute_age)

# Age Label
age_label = tk.Label(root, text="Age: ")
age_label.pack()

# Gender Selection
gender_var = tk.StringVar()

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male",
               command=set_gender_color).pack()

tk.Radiobutton(root, text="Female", variable=gender_var, value="Female",
               command=set_gender_color).pack()

# Image (optional - make sure may file ka)
try:
    img = PhotoImage(file="profile.png")  # lagay ka ng image file
    img_label = tk.Label(root, image=img)
    img_label.pack(pady=10)
except:
    tk.Label(root, text="No Image").pack()

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=generate_id)
submit_btn.pack(pady=20)

submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

root.mainloop()
