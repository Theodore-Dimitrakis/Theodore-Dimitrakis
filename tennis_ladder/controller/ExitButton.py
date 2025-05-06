import tkinter as tk

def create_exit_button(parent_frame, main_window):
    """
    Create and return an Exit button for the Tennis Ladder application.
    :param parent_frame: The frame where the button will be placed.
    :param main_window: The main Tkinter window to close.
    :return: The Exit button instance.
    """
    def exit_application():
        """
        Function to exit the application.
        """
        main_window.destroy()

    exit_button = tk.Button(
        parent_frame,
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
    return exit_button