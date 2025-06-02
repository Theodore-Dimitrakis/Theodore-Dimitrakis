import tkinter as tk
from tkinter import messagebox,PhotoImage
from PIL import Image,ImageTk
import sys

#'Μονοπάτι' για σύνδεση μεταξύ φακέλων service και του συγκεκριμένου αρχείου,για εύρεση MatchService,PlayerService
sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\service")
sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\repository")
sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\db_utils")
from service.PlayerService import PlayerService
from repository import PlayerRepository
from db_utils import DBUtils
from DBInit import DBInit
from ChallengeButton import connection_services_challenge_button

(player_service,db_utils_for_statistics,db_init_for_statistics,
             session_for_statistics,match_repository,player_repository_for_statistics,league_round_repository) = connection_services_challenge_button()

def create_statistics_button(parent_frame):

        def statistics_action():
            window_statistics_player = tk.Toplevel(parent_frame)
            window_statistics_player.title('Statistics for Players')
            window_statistics_player.geometry("810x200")
            window_statistics_player.resizable(True, True)
            rank_label = tk.Label(window_statistics_player,text="",font=("Arial", 18))
            name_label = tk.Label(window_statistics_player, text="", font=("Arial", 18))
            photo_label = tk.Label(window_statistics_player, text="")
            show_statistics_ordered = player_service.show_ordered_by_rank()

            def show_ranks(num_of_list):
                if num_of_list < len(show_statistics_ordered):
                    info = num_of_list
                    number_place = 0
                    for info in show_statistics_ordered:
                        rank_label.config(text=f"{info.rank}")
                        rank_label.grid(row=number_place,column=number_place)
                        name_label.config(text=f"{info.name}")
                        name_label.rank_label.grid(row=number_place,column=number_place+1)
                        #εδω επειδη πρεπει να συνδεσω το ονομα του παιχτη που βρισκεται σε αυτη την λιστα (show_statistics_ordered) με την φωτογραφια που εχει ο καθε παιχτης, στo αρχειο ChallengeButon στην load_images_into_dictionary_with_name_images_as_key_values() εχω dictionary με {name:photo} , οποτε if info.name == name : τοτε να μπει στο photo_label.config() και να εμφανιστει εκει . με grid και το number_place αναλογα την επανα΄ληψη.
                        #Επισης να κανω μια συναρτηση με τις φωτογραφιες να προσαρμοσω παλι το μεγεθος τους
                        #για να ειναι ομοιομορφες (θελουν πολυ μικρο μεγεθος).
                        photo_label.config(text=f"{info.rank}")





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