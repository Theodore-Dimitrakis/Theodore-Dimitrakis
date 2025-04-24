import tkinter as tk
from tkinter import messagebox

class StatisticsButton:
    """
    Class to create and manage the Statistics button for the Tennis Ladder application.
    """

    def __init__(self, parent_frame):
        """
        Initialize the StatisticsButton class and create the button.
        :param parent_frame: The frame where the button will be placed.
        """
        self.parent_frame = parent_frame
        self.button = tk.Button(
            self.parent_frame,
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
            command=self.statistics_action,
        )

    def statistics_action(self):
        """
        Function to handle the Statistics button action.
        """
        messagebox.showinfo("Statistics Button", "Statistics functionality is not implemented yet!")

    def get_button(self):
        """
        Return the button instance.
        :return: The Statistics button instance.
        """
        return self.button