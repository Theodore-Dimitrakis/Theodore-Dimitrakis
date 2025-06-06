import tkinter as tk
from tkinter import messagebox,PhotoImage

###************* Tα file paths εδω δε χρειαζονται, πρεπει να σβηστουν *********####

#'Μονοπάτι' για σύνδεση μεταξύ φακέλων service και του συγκεκριμένου αρχείου,για εύρεση MatchService,PlayerService
# sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\service")
# sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\repository")
# sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\db_utils")

from ChallengeButton import connection_services_challenge_button

(player_service,db_utils_for_statistics,db_init_for_statistics,
             session_for_statistics,match_repository,player_repository_for_statistics,league_round_repository) = connection_services_challenge_button()

def create_statistics_button(parent_frame):

        # def statistics_action():
        #     window_statistics_player = tk.Toplevel(parent_frame)
        #     window_statistics_player.title('Statistics for Players')
        #     window_statistics_player.geometry("410x500")
        #     window_statistics_player.resizable(False, False)
        #     window_statistics_player.configure(bg="#45a049")
        #
        #     def position_titles_each_category():
        #             rank_title_label = tk.Label(window_statistics_player,text="Rank",bg="#45a049",fg="white",font=("Arial",19))
        #             name_title_label = tk.Label(window_statistics_player, text="Name",bg="#45a049",fg="white",font=("Arial", 19))
        #             wins_title_label = tk.Label(window_statistics_player, text="Wins",bg="#45a049",fg="white",font=("Arial", 19))
        #             looses_title_label = tk.Label(window_statistics_player, text="Losses",bg="#45a049",fg="white",font=("Arial", 19))
        #
        #             rank_title_label.grid(row=0,column=0)
        #             name_title_label.grid(row=0, column= 1)
        #             wins_title_label.grid(row=0,column=2)
        #             looses_title_label.grid(row=0,column=3)
        #             window_statistics_player.after(500,lambda: position_titles_each_category())
        #
        #     position_titles_each_category()
        #
        #
        #
        #     def import_statistics_ranks_from_list(player_stats,index_of_list):
        #
        #             rank_label = tk.Label(window_statistics_player, text=f"{player_stats['rank']}",bg="#45a049",fg="white",font=("Arial", 10))
        #             rank_label.grid(row=index_of_list+1, column=0)
        #
        #             name_label = tk.Label(window_statistics_player, text=f"{player_stats['name']}",bg="#45a049",fg="white",font=("Arial", 10))
        #             name_label.grid(row=index_of_list+1, column=1)
        #
        #             wins_label = tk.Label(window_statistics_player, text=f"{player_stats['wins']}",bg="#45a049",fg="white",font=("Arial", 10))
        #             wins_label.grid(row=index_of_list+1, column=2)
        #
        #             looses_label = tk.Label(window_statistics_player, text=f"{player_stats['losses']}",bg="#45a049",fg="white",font=("Arial", 10))
        #             looses_label.grid(row=index_of_list+1, column=3)
        #
        #     show_statistics = player_service.show_statistics()
        #     print(show_statistics)
        #
        #     def show_information_each_player_for_rank_in_gui(num_of_list):
        #         try:
        #             if num_of_list < len(show_statistics):
        #                 player_information = show_statistics[num_of_list]
        #                 import_statistics_ranks_from_list(player_information,num_of_list)
        #                 window_statistics_player.after(500,lambda: show_information_each_player_for_rank_in_gui(num_of_list+1))
        #         except Exception as e:
        #             messagebox.showinfo("Error in Statistics",f"Error : {e}.")
        #
        #     show_information_each_player_for_rank_in_gui(0)
        #
        # statistics_button = tk.Button(
        #     parent_frame,
        #     text="Statistics",
        #     font=("Arial", 12, "bold"),
        #     bg="#4CAF50",
        #     fg="white",
        #     width=20,
        #     height=2,
        #     bd=0,
        #     relief="solid",
        #     activebackground="#45a049",
        #     activeforeground="white",
        #     command=statistics_action,
        # )
        # return statistics_button


        # Δες την ανανεωμένη μέθοδο χωρίς το delay
        def statistics_action():
            window_statistics_player = tk.Toplevel(parent_frame)
            window_statistics_player.title('Statistics for Players')
            window_statistics_player.geometry("410x500")
            window_statistics_player.resizable(False, False)
            window_statistics_player.configure(bg="#45a049")

            rank_title_label = tk.Label(window_statistics_player, text="Rank", bg="#45a049", fg="white",
                                        font=("Arial", 19))
            name_title_label = tk.Label(window_statistics_player, text="Name", bg="#45a049", fg="white",
                                        font=("Arial", 19))
            wins_title_label = tk.Label(window_statistics_player, text="Wins", bg="#45a049", fg="white",
                                        font=("Arial", 19))
            looses_title_label = tk.Label(window_statistics_player, text="Losses", bg="#45a049", fg="white",
                                          font=("Arial", 19))

            rank_title_label.grid(row=0, column=0)
            name_title_label.grid(row=0, column=1)
            wins_title_label.grid(row=0, column=2)
            looses_title_label.grid(row=0, column=3)

            try:
                show_statistics = player_service.show_statistics()

                for i, player_stats in enumerate(show_statistics):
                    tk.Label(window_statistics_player, text=player_stats["rank"], bg="#45a049", fg="white",
                             font=("Arial", 10)).grid(row=i + 1, column=0)
                    tk.Label(window_statistics_player, text=player_stats["name"], bg="#45a049", fg="white",
                             font=("Arial", 10)).grid(row=i + 1, column=1)
                    tk.Label(window_statistics_player, text=player_stats["wins"], bg="#45a049", fg="white",
                             font=("Arial", 10)).grid(row=i + 1, column=2)
                    tk.Label(window_statistics_player, text=player_stats["losses"], bg="#45a049", fg="white",
                             font=("Arial", 10)).grid(row=i + 1, column=3)

            except Exception as e:
                messagebox.showerror("Error in Statistics", f"Error: {e}")

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