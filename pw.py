import tkinter
import customtkinter
from functions import *

choices = ["5", "10", "20", "40"]

# root 
root = tkinter.Tk()
root.configure(bg = "black")
root.title("pw generator")

bool_small = tkinter.BooleanVar()
bool_big = tkinter.BooleanVar()
bool_special = tkinter.BooleanVar()
bool_nums = tkinter.BooleanVar()

# frame 
button_frame = customtkinter.CTkFrame(master=root, corner_radius=20, bg_color="yellow", width=400, height=100)
button_frame.grid(row=0)
button_frame.grid_propagate(False)

pw_frame = customtkinter.CTkFrame(master=root, corner_radius=20, bg_color="blue", width=400, height=20)
pw_frame.grid(row=1, pady=20)
pw_frame.grid_propagate(False)


# label
pw = customtkinter.CTkEntry(master=pw_frame, width=400, height=20, bg_color="gray55")
pw.grid(row = 0, column=1)


# buttons
check_small = customtkinter.CTkCheckBox(master=button_frame, text="small", width=10, height=10, variable=bool_small, onvalue=True, offvalue=False)
check_small.grid(row=1, column = 0, padx=10, pady=10)

check_big = customtkinter.CTkCheckBox(master=button_frame, text="big", width=10, height=10, variable=bool_big, onvalue=True, offvalue=False)
check_big.grid(row=1, column = 1, padx=10, pady=10)

check_special = customtkinter.CTkCheckBox(master=button_frame, text="special", width=10, height=10, variable=bool_special, onvalue=True, offvalue=False)
check_special.grid(row=1, column=2, padx=10, pady=10)

check_nums = customtkinter.CTkCheckBox(master=button_frame, text="nums", width=10, height=10, variable=bool_nums, onvalue=True, offvalue=False)
check_nums.grid(row=1, column=3, padx=10, pady=10)

button_generatepw = customtkinter.CTkButton(master=button_frame, text="generate pw", width=10, height=10, command=lambda:generate(int(box_length.get()), bool_small.get(),
                                                                                                                    bool_special.get(),
                                                                                                                    bool_nums.get(),
                                                                                                                    bool_big.get(),
                                                                                                                    pw))
button_generatepw.grid(row=2, column = 0, padx=10, pady=20)

box_length = customtkinter.CTkComboBox(master=button_frame, values=choices, width=50, height=10, text_color="orchid1")
box_length.grid(row=2, column = 1, padx=10, pady=10)


root.mainloop()


