import tkinter as tk
from tkinter import messagebox
from InitializeButton import InitializeButton

main_window = tk.Tk()
main_window.title("Tennis Ladder")
main_window.state("zoomed")  # Opens the window in fullscreen mode

# Create a scrollable frame
canvas = tk.Canvas(main_window)
scrollbar = tk.Scrollbar(main_window, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

# Configure the canvas and scrollbar
scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create a frame at the top to hold the buttons
top_frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
top_frame.pack(side="top", fill="x", pady=10)

# Function to exit the application linked to btn_exit
def exit_application():
    main_window.destroy()
btn_exit = tk.Button(
    top_frame,
    text="Exit",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=20,
    height=2,
    bd=0,
    relief="solid",
    activebackground="#d32f2f",
    activeforeground="white",
    command=exit_application,
)
btn_exit.pack(side="left", padx=10)

#gets button initialize from InitializeButton.py
initialize_button = InitializeButton(top_frame)
initialize_button.get_button().pack(side="left", padx=10)

btn_challenge = tk.Button(
    top_frame,
    text="Challenge",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    height=2,
    bd=0,
    relief="solid",
    activebackground="#45a049",
    activeforeground="white",
)

btn_manage = tk.Button(
    top_frame,
    text="Manage",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    height=2,
    bd=0,
    relief="solid",
    activebackground="#45a049",
    activeforeground="white",
)

btn_statistics = tk.Button(
    top_frame,
    text="Statistics",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    height=2,
    bd=0,
    relief="solid",
    activebackground="#45a049",
    activeforeground="white",
)


# Pack the buttons horizontally in the top frame
btn_challenge.pack(side="left", padx=10)
btn_manage.pack(side="left", padx=10)
btn_statistics.pack(side="left", padx=10)

main_window.mainloop()