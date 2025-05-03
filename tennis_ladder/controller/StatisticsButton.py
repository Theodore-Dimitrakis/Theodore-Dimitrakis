import tkinter as tk
from tkinter import messagebox
import sys


#'Μονοπάτι' για σύνδεση μεταξύ φακέλων service και του συγκεκριμένου αρχείου,για εύρεση MatchService,PlayerService
sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\service")
from service.MatchService import MatchService
from service.PlayerService import PlayerService

def create_statistics_button(parent_frame):

        def statistics_action():
           messagebox.showinfo("Statistics Button", "Statistics functionality is not implemented yet!")


        statistics_button = tk.Button(
            parent_frame,
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
            command=statistics_action,
        )
        return statistics_button