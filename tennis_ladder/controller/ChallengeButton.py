import tkinter as tk
from tkinter import messagebox
import sys


#'Μονοπάτι' για σύνδεση μεταξύ φακέλων service και του συγκεκριμένου αρχείου,για εύρεση MatchService.
sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\service")
from service.MatchService import MatchService


def create_challenge_button(parent_frame):
    # Fuction για έναρξη παιχνιδιού μεταξύ των παιχτών.
    def challenge_action():
        MatchService.create_match()

    #Δημιουργια κουμπιού χαρακτηριστικών Challenge.
    challenge_button = tk.Button(
        parent_frame,
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
        command=challenge_action
    )



    return challenge_button