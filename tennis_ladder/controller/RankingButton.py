import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controller.ChallengeButton import connection_services_challenge_button

player_service, db_utils, db_init, session, match_repository, player_repository, league_round_repository, match_service = connection_services_challenge_button()
show_ordered_by_rank_initialization_for_ranking_button = player_service.show_ordered_by_rank()

def create_ranking_button(parent_frame):
     def ranking_action():
         window_ordered_ranking_player = tk.Toplevel(parent_frame)
         window_ordered_ranking_player.title('Statistics for Players')
         window_ordered_ranking_player.geometry("310x500")
         window_ordered_ranking_player.resizable(False, False)
         window_ordered_ranking_player.configure(bg="#45a049")

         def placing_title_label_GUI(num):
             ranking_title_label = tk.Label(window_ordered_ranking_player,text="Rank",bg="#45a049",fg="white",font=("Arial",19))
             naming_title_label = tk.Label(window_ordered_ranking_player,text="Name",bg="#45a049",fg="white",font=("Arial",19))

             ranking_title_label.grid(row=num,column=0)
             naming_title_label.grid(row=num,column=1)

         show_ordered_ranking_for_place_gui = show_ordered_by_rank_initialization_for_ranking_button

         def placing_ordered_ranking(index_run,num_player_in_list):
             try:
                if index_run <= len(show_ordered_ranking_for_place_gui):
                    rank_label_ranking_button = tk.Label(window_ordered_ranking_player,text=f"{show_ordered_ranking_for_place_gui[num_player_in_list].rank}",bg="#45a049",fg="white",font=("Arial",10))
                    name_label_ranking_button = tk.Label(window_ordered_ranking_player,text=f"{show_ordered_ranking_for_place_gui[num_player_in_list].name}",bg="#45a049",fg="white",font=("Arial",10))

                    rank_label_ranking_button.grid(row=index_run,column=0)
                    name_label_ranking_button.grid(row=index_run,column=1)
                if index_run == 19:
                    rank_label_ranking_button = tk.Label(window_ordered_ranking_player,
                                                      text=f"{show_ordered_ranking_for_place_gui[num_player_in_list+1].rank}",
                                                      bg="#45a049",fg="white",font=("Arial", 10))
                    name_label_ranking_button = tk.Label(window_ordered_ranking_player,
                                                      text=f"{show_ordered_ranking_for_place_gui[num_player_in_list+1].name}",
                                                      bg="#45a049",fg="white",font=("Arial", 10))
                window_ordered_ranking_player.after(1000,lambda: placing_ordered_ranking(index_run+1,num_player_in_list+1))
             except Exception as e:
                messagebox.showinfo("Error in Ranking",f"Error : {e}")

         placing_title_label_GUI(0)
         placing_ordered_ranking(1,0)

     ranking_button = tk.Button(
     parent_frame,
     text="Rank",
     font=("Arial", 12, "bold"),
     bg="#4CAF50",
     fg="white",
     width=20,
     height=2,
     bd=0,
     relief="solid",
     activebackground="#45a049",
     activeforeground="white",
     command=ranking_action,
         )
     return ranking_button