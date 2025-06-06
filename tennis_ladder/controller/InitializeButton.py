import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from DBInit import DBInit

class InitializeButton:
    """
    Class to create and manage the Initialize button for the Tennis Ladder application.
    """

    def __init__(self, parent_frame):
        """
        Initialize the InitializeButton class and create the button.
        :param parent_frame: The frame where the button will be placed.
        """
        self.parent_frame = parent_frame
        self.button = tk.Button(
            self.parent_frame,
            text="Initialize",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            height=2,
            bd=0,
            relief="solid",
            activebackground="#45a049",
            activeforeground="white",
            command=self.initialize_database,
        )

    def initialize_database(self):
        """
        Function to initialize the database and display a success or error message.
        """
        db_init = DBInit()
        try:
            db_init.initialize_db()
            messagebox.showinfo("Tennis Ladder Initialized!",
                                "Tennis ladder is now Open!\nThere are 20 players in the ladder")
        except RuntimeError as e:
            messagebox.showerror("Initialization Failed", str(e))

    def get_button(self):
        """
        Return the button instance.
        :return: The Initialize button instance.
        """
        return self.button