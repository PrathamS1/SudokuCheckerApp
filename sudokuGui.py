import tkinter as tk
from tkinter import messagebox
import sudokuChecker

root = tk.Tk()
root.title("Sudoku Checker")
root.configure(bg="#ffffff")

# Function to send data to main program
def submit_data():
    data = []
    for row in rows:
        row_data = []
        for cell in row:
            cell_value = cell.get()
            if cell_value.isdigit() and 1 <= int(cell_value) <= 9:
                row_data.append(int(cell_value))
            else:
                messagebox.showerror("Invalid Input", "Please enter numbers between 1 and 9")
                return
        data.append(row_data)
    result = sudokuChecker.sudoku_checker(data)
    if result == 1:
        result_label.config(text='Sudoku is correct', fg="#4CAF50")
    else:
        result_label.config(text='Sudoku is incorrect', fg="#F44336")

# Check if all input fields are filled
def check_input():
    is_filled = True
    for i in range(9):
        for j in range(9):
            if rows[i][j].get() == "":
                is_filled = False
                break
        if not is_filled:
            break
    return is_filled

# Show the output message
def show_output():
    if check_input():
        submit_data()
    else:
        messagebox.showwarning("Incomplete Input", "Please fill all input fields!")

# Reset all input fields
def reset_grid():
    for row in rows:
        for cell in row:
            cell.delete(0, tk.END)
    result_label.config(text="")

# Function to create the input grid
def create_input_grid():
    for i in range(9):
        for j in range(9):
            entry = tk.Entry(input_frame, width=5, font=("Helvetica", 14), bg="#e6f7ff", relief="solid", bd=1, justify="center")
            entry.grid(row=i, column=j, padx=2, pady=2, ipady=5)
            if (i // 3 + j // 3) % 2 == 0:
                entry.config(bg="#ffffff")
            rows[i].append(entry)

# Creating the GUI layout
title_label = tk.Label(root, text="Sudoku Checker", font=("Helvetica", 24), bg="#ffffff", fg="#333333")
title_label.pack(pady=(20, 10))

instructions_label = tk.Label(root, text="Enter the Sudoku puzzle below and click 'Submit' to check.", font=("Helvetica", 14), bg="#ffffff", fg="#555555")
instructions_label.pack(pady=(0, 20))

input_frame = tk.Frame(root, bg="#ffffff")
input_frame.pack()

rows = [[] for _ in range(9)]
create_input_grid()

button_frame = tk.Frame(root, bg="#ffffff")
button_frame.pack(pady=(20, 0))

submit_button = tk.Button(button_frame, text="Submit", command=show_output, font=("Helvetica", 14), bg="#4CAF50", fg="#ffffff", relief="raised", bd=3)
submit_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset_grid, font=("Helvetica", 14), bg="#F44336", fg="#ffffff", relief="raised", bd=3)
reset_button.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#ffffff")
result_label.pack(pady=(20, 0))

root.mainloop()
