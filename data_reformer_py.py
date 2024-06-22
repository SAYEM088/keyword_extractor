import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Product version btncl#2e8b57sam-1
STATIC_EMAIL = ""
STATIC_PASSWORD = ""

#as it was a business project main function is omitted.
#Example of uses ;
#  let "mid3333journey_Indian_Rogan_Josh_Lamb_Quesadilla_a120edf9-e864-4533-b617-921e8374d3dd_1.jpg" 
#   this is our data
#   we will refine and able to extract name : output : "Indian Rogan Josh Lamb Quesadilla"
#"\codeblack92_Mango_Pineapple_Cupcake_Creation_21c76fb6-9f38-44fa-bfb3-5cbf6a7f2344_block_1_1.jpg"
# output : "Mango Pineapple Cupcake Creation"
#That means there is no pattern of the data

def select_input_file():
    input_file_path.set(filedialog.askopenfilename())

def select_output_file():
    output_file_path.set(filedialog.asksaveasfilename(defaultextension=".txt"))

def login():
    email = email_entry.get()
    password = password_entry.get()
    if email == STATIC_EMAIL and password == STATIC_PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome {email}!")
        login_frame.pack_forget()
        main_frame.pack()
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")

def set_window_size():
    app.geometry("800x800")

app = tk.Tk()
app.resizable(True, True)
set_window_size()
app.title("SayIT Data Reformer")

button_color = "#2e8b57"
label_color = "#1d2951"
sp1_color = "#cfcfc4"
sp2_color = "#b22222"
sp3_color = "#002147"
sp4_color = "#000080"
label_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
select_font = ("Arial", 8, "bold")

login_frame = tk.Frame(app)
tk.Label(login_frame, text="Email:", fg=sp4_color, font=button_font).grid(row=0, column=0, padx=(10, 3), pady=(100, 0))
email_entry = tk.Entry(login_frame, bg=sp1_color, fg="black", font=label_font)
email_entry.grid(row=0, column=1, padx=0, pady=(100, 0))
tk.Label(login_frame, text="Password:", fg=sp4_color, font=button_font).grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_frame, show='*', bg=sp1_color, fg="black", font=label_font)
password_entry.grid(row=1, column=1, padx=0, pady=0)
tk.Button(login_frame, text="Login", command=login, bg=button_color, font=button_font, fg="white").grid(row=2, column=1, pady=10)
sub_info_label = tk.Label(login_frame, text="Powered by SayIT", fg=sp2_color, font=button_font)
sub_info_label.grid(row=7, column=1, pady=(30, 0))
sub_info_label = tk.Label(login_frame, text="Email : sayit.solution880@gmail.com", font=button_font, fg=sp3_color)
sub_info_label.grid(row=8, column=1)
sub_info_label = tk.Label(login_frame, text="Number: +8801775-876544", font=button_font, fg=sp3_color)
sub_info_label.grid(row=9, column=1)
login_frame.pack()

main_frame = tk.Frame(app)
input_file_path = tk.StringVar()
output_file_path = tk.StringVar()
erase_keyword = tk.StringVar()

tk.Label(main_frame, text="Select Input File", fg=sp4_color, font=button_font).grid(row=1, column=0, padx=10, pady=(100, 10))
tk.Entry(main_frame, textvariable=input_file_path, width=50, bg=sp1_color, fg="black", font=label_font).grid(row=1, column=1, padx=10, pady=(100, 10))
tk.Button(main_frame, text="Select", bg="#367588", font=select_font, fg="white", command=select_input_file).grid(row=1, column=2, padx=10, pady=(100, 10))

tk.Label(main_frame, text="Select Output File", fg=sp4_color, font=button_font).grid(row=2, column=0, padx=10, pady=10)
tk.Entry(main_frame, textvariable=output_file_path, width=50, bg=sp1_color, fg="black", font=label_font).grid(row=2, column=1, padx=10, pady=10)
tk.Button(main_frame, text="Select", bg="#367588", font=select_font, fg="white", command=select_output_file).grid(row=2, column=2, padx=10, pady=10)

tk.Label(main_frame, text="Keyword to Erase", fg=sp4_color, font=button_font).grid(row=3, column=0, padx=10, pady=10)
tk.Entry(main_frame, textvariable=erase_keyword, width=50, bg=sp1_color, fg="black", font=label_font).grid(row=3, column=1, padx=10, pady=10)

tk.Button(main_frame, text="Clean Data", bg=button_color, font=button_font, fg="white", command=lambda: clean_data(input_file_path.get(), output_file_path.get(), erase_keyword.get())).grid(row=4, column=1, pady=20)

company_info_label = tk.Label(main_frame, text="Powered by SayIT", font=button_font, fg=sp2_color)
company_info_label.grid(row=5, column=1, pady=(30, 0))
company_info_label = tk.Label(main_frame, text="Email : sayit.solution880@gmail.com", font=button_font, fg=sp3_color)
company_info_label.grid(row=6, column=1)
company_info_label = tk.Label(main_frame, text="Number: +8801775-876544", font=button_font, fg=sp3_color)
company_info_label.grid(row=7, column=1)
app.mainloop()
