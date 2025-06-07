import os
import sys
import tkinter as tk
from tkinter import ttk

from service.PlayerService import PlayerService

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from repository.PlayerRepository import PlayerRepository
from DBInit import DBInit

def add_leaderboard_to_main_window(parent_frame):
    """
    Add a leaderboard table to the main window.
    :param parent_frame: The frame where the leaderboard will be placed.
    """
    db_init = DBInit()
    player_repository = PlayerRepository(db_init.session)
    player_service = PlayerService(db_init.session, player_repository)

    # Create Treeview for Leaderboard
    leaderboard_tree = ttk.Treeview(parent_frame, columns=("Rank", "Name"), show="headings", height=15)  # Increased height
    leaderboard_tree.heading("Rank", text="Rank")
    leaderboard_tree.heading("Name", text="Name")
    leaderboard_tree.column("Rank", width=120, anchor="center")  # Wider column
    leaderboard_tree.column("Name", width=240, anchor="center")  # Wider column
    leaderboard_tree.pack(fill="both", expand=True, padx=10, pady=10)  # Adjusted padding

    def refresh_leaderboard():
        """
        Refresh the leaderboard table with updated player data.
        """
        for row in leaderboard_tree.get_children():
            leaderboard_tree.delete(row)

        try:
            players = player_service.show_ordered_by_rank()
            for player in players:
                leaderboard_tree.insert("", "end", values=(player.rank, player.name))
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to refresh leaderboard: {e}")

    refresh_leaderboard()

    return refresh_leaderboard