import sys
import tkinter as tk
import time
from tkinter import messagebox,PhotoImage
from PIL import Image,ImageTk

from MatchCRUDExamplesAndTesting import match_service, league_round_repository
from db_utils import DBUtils

# 'Μονοπάτι' για σύνδεση μεταξύ φακέλων service/entinty και του συγκεκριμένου αρχείου,για εύρεση MatchService/PlayerService/Player.
# sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\service")
# sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\entity")
# sys.path.append("C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\repository")

# Παραδείγματα imports για τα services, τα οποία πρέπει να είναι γνωστά στην εφαρμογή σας.
from service.PlayerService import PlayerService  # Υποθέτουμε ότι υπάρχει.
from service.MatchService import MatchService  # Υποθέτουμε ότι υπάρχει.
from repository.PlayerRepository import PlayerRepository
from repository.MatchRepository import  MatchRepository
from repository.LeagueRoundRepository import LeagueRoundRepository
from entity.Player import Player
from DBInit import DBInit


def connection_services_challenge_button():
    db_utils = DBUtils()
    db_init = DBInit()
    session = db_init.session
    player_repository = PlayerRepository(session)
    match_repository = MatchRepository(session)
    league_round_repository = LeagueRoundRepository(session)
    player_service = PlayerService(session, player_repository)
    return player_service, db_utils, db_init, session, match_repository, player_repository, league_round_repository

def create_challenge_button(parent_frame, refresh_leaderboard):


    # Συνάρτηση για δημιουργία κουμπιού "Challenge".
    def challenge_action():
        new_window_for_challenge = tk.Toplevel(parent_frame)
        new_window_for_challenge.title('Challenge for Players')
        new_window_for_challenge.geometry("810x200")
        new_window_for_challenge.resizable(True, True)

        player_service, db_utils, db_init, session, match_repository, player_repository, league_round_repository = connection_services_challenge_button()


        # # Και μετά χρησιμοποίησέ το στην PlayerService
        # player_service_initialization = PlayerService(session, player_repository)
        # show_players_for_option_menu = player_service_initialization.get_all_players()
        # list_of_players = [each_player.name for each_player in show_players_for_option_menu]

        player_service_initialization = player_service
        show_players_for_option_menu = player_service_initialization.get_all_players()
        list_of_players = [each_player.name for each_player in show_players_for_option_menu]

        #Δημιουργια Frame.
        frame_menu = tk.Frame(new_window_for_challenge,bg="#45a049",height='100',width='200',bd='3',relief="sunken")
        frame_menu.pack(anchor='center')
        value_for_option_menu_1 = tk.StringVar(new_window_for_challenge)
        value_for_option_menu_2 = tk.StringVar(new_window_for_challenge)
        value_for_option_menu_1.set("Select Player 1")
        value_for_option_menu_2.set("Select Player 2")

        option_menu_challenge_1 = tk.OptionMenu(frame_menu, value_for_option_menu_1, *list_of_players)
        option_menu_challenge_1.grid(row=0, column=1, padx='10', pady='10')
        player_1_label = tk.Label(frame_menu, text="Player 1",bg="#45a049", fg="white" ,font=("Arial", 12))
        player_1_label.grid(row=0, column=0, padx='10', pady='10')

        option_menu_challenge_2 = tk.OptionMenu(frame_menu, value_for_option_menu_2, *list_of_players)
        option_menu_challenge_2.grid(row=1, column=1, padx='10', pady='10')
        player_2_label = tk.Label(frame_menu, text="Player 2",bg="#45a049", fg="white",font=("Arial", 12))
        player_2_label.grid(row=1, column=0, padx='10', pady='10')

        # Διόρθωση 2: Labels ενημερώνονται όταν γίνει επιλογή.
        show_player_name_1_label = tk.Label(frame_menu, text='',bg="#45a049", fg="white",font=("Arial", 12))
        show_player_name_1_label.grid(row=2, column=0)
        show_player_name_2_label = tk.Label(frame_menu, text='',bg="#45a049", fg="white",font=("Arial", 12))
        show_player_name_2_label.grid(row=2, column=2)

        select_button_option_menu_1 = tk.Button(frame_menu, text='Select',
                                                command=lambda: show_player_name_1_label.config(
                                                    text=f"Player 1 Selection: {value_for_option_menu_1.get()}"),bg="#45a049", fg="white",font=("Arial", 12))
        select_button_option_menu_1.grid(row=0, column=3, padx='10', pady='10')

        select_button_option_menu_2 = tk.Button(frame_menu, text='Select',
                                                command=lambda: show_player_name_2_label.config(
                                                    text=f"Player 2 Selection: {value_for_option_menu_2.get()}"),bg="#45a049", fg="white",font=("Arial", 12))
        select_button_option_menu_2.grid(row=1, column=3, padx='10', pady='10')


        # def player_names():
        #     players = [
        #     "Novak Djokovic", "Margaret Court", "Rafael Nadal", "Serena Williams",
        #     "Steffi Graf", "Roger Federer", "Helen Wills", "Martina Navratilova", "Chris Evert", "Billie Jean King",
        #     "Roy Emerson", "Rod Laver", "Bill Tilden", "Suzanne Lenglen", "Ken Rosewall", "Maria Sakkari",
        #     "Naomi Osaka", "Andre Agassi", "Bjorn Borg", "Pete Sampras"
        # ]
        #     return players
        #
        # def fix_size_images(image):
        #     if image.width == 260 and image.height == 250:
        #         return image
        #     else:
        #         return image.resize((260, 250))

        # def load_images_into_PyCharm():
        #     andre_aggasi_1 = Image.open(
        #         "C:\\Users\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\andre-aggasi-photos\\andre-1.jpeg")
        #     bill_tilden_1 = Image.open(
        #         "C:\\Users\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\bill-tilden-photos\\bill-1.jpg")
        #     bill_jean_king_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\billie-jean-king-photos\\billie-1.jpg")
        #     bjorn_borg_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\Bjorn-Borg-photos\\bjorn-1.jpg")
        #     chris_event_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\Chris-Evert-photos\\chris-1.jpeg")
        #     default_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\default-photos\\default-1.jpg")
        #     default_2 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\default-photos\\default-2.jpg")
        #     default_3 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\default-photos\\default-3.jpg")
        #     default_5 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\default-photos\\default-5.jpg")
        #     default_6 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\default-photos\\default-6.jpg")
        #     versus = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\default-photos\\versus.png")
        #     hellen_wills_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\hellen-wills-photos\\hellen-1.jpg")
        #     ken_rosewall_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\Ken-Rosewall-photos\\ken-1.jpeg")
        #     margaret_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\margaret-court-photos\\marga-1.jpeg")
        #     sakari_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\maria-sakari-photos\\maria-1.jpg")
        #     matina_2 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\matina-navralitova-photos\\mat-2.jpg")
        #     naomi_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\naomi-osaka-photos\\naomi-1.jpeg")
        #     novak_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\novak-djokovic-photos\\novak-1.jpg")
        #     pete_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\Pete-Sampras-photos\\pete-1.jpeg")
        #     rafael_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\rafael-nadal-photos\\rafael-1.jpg")
        #     rod_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\Rod-Laver-photos\\rod-1.jpg")
        #     roger_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\roger-federer-photos\\roger-1.jpg")
        #     roy_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\roy-emerson-photos\\roy-1.jpeg")
        #     serena_3 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\serena-williams-photos\\serena-3.jpeg")
        #     steffi_4 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\steffi-graff-photos\\steffi-4.jpeg")
        #     suzane_1 = Image.open(
        #         "C:\\Users\\Ελένη\\EAP_tennis_ladder\\tennis_ladder\\tennis-ladder-photos-challenge\\suzzane-leglen-photos\\suz-1.jpeg")
        #
        #     return [andre_aggasi_1,bill_tilden_1,bill_jean_king_1,bjorn_borg_1,chris_event_1,
        #             default_1,default_2,default_3,default_5,default_6,versus,hellen_wills_1,
        #             ken_rosewall_1,margaret_1,sakari_1,matina_2,naomi_1,novak_1,pete_1,
        #             rafael_1,rod_1,roger_1,roy_1,serena_3,steffi_4,suzane_1]
        #
        # def load_fixed_images_with_proper_size():
        #
        #
        #     image = load_images_into_PyCharm()
        #
        #
        #     andre_aggasi_1 = fix_size_images(image[0])
        #     bill_tilden_1 = fix_size_images(image[1])
        #     bill_jean_king_1 = fix_size_images(image[2])
        #     bjorn_borg_1 = fix_size_images(image[3])
        #     chris_event_1 = fix_size_images(image[4])
        #     default_1 = fix_size_images(image[5])
        #     default_2 = fix_size_images(image[6])
        #     default_3 = fix_size_images(image[7])
        #     default_5 = fix_size_images(image[8])
        #     default_6 = fix_size_images(image[9])
        #     versus = image[10].resize((100,100))
        #     hellen_wills_1 = fix_size_images(image[11])
        #     ken_rosewall_1 = fix_size_images(image[12])
        #     margaret_1 = fix_size_images(image[13])
        #     sakari_1 = fix_size_images(image[14])
        #     matina_2 = fix_size_images(image[15])
        #     naomi_1 = fix_size_images(image[16])
        #     novak_1 = fix_size_images(image[17])
        #     pete_1 = fix_size_images(image[18])
        #     rafael_1 = fix_size_images(image[19])
        #     rod_1 = fix_size_images(image[20])
        #     roger_1 = fix_size_images(image[21])
        #     roy_1 = fix_size_images(image[22])
        #     serena_3 = fix_size_images(image[23])
        #     steffi_4 = fix_size_images(image[24])
        #     suzane_1 = fix_size_images(image[25])
        #
        #
        #     return [andre_aggasi_1,
        #             bill_tilden_1,bill_jean_king_1,bjorn_borg_1,chris_event_1,
        #             default_1, default_2, default_3, default_5,default_6,versus,
        #             hellen_wills_1,ken_rosewall_1,margaret_1,sakari_1,matina_2,naomi_1,
        #             novak_1,pete_1, rafael_1,rod_1,roger_1,roy_1,serena_3, steffi_4,suzane_1]
        #
        # def load_images_with_PhotoImage():
        #
        #     fixed_images_with_proper_size = load_fixed_images_with_proper_size()
        #
        #     andre_aggasi_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[0])
        #     bill_tilden_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[1])
        #     bill_jean_king_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[2])
        #     bjorn_borg_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[3])
        #     chris_event_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[4])
        #     default_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[5])
        #     default_2 = ImageTk.PhotoImage(fixed_images_with_proper_size[6])
        #     default_3 = ImageTk.PhotoImage(fixed_images_with_proper_size[7])
        #     default_5 = ImageTk.PhotoImage(fixed_images_with_proper_size[8])
        #     default_6 = ImageTk.PhotoImage(fixed_images_with_proper_size[9])
        #     versus = ImageTk.PhotoImage(fixed_images_with_proper_size[10])
        #     hellen_wills_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[11])
        #     ken_rosewall_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[12])
        #     margaret_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[13])
        #     sakari_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[14])
        #     matina_2 = ImageTk.PhotoImage(fixed_images_with_proper_size[15])
        #     naomi_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[16])
        #     novak_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[17])
        #     pete_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[18])
        #     rafael_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[19])
        #     rod_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[20])
        #     roger_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[21])
        #     roy_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[22])
        #     serena_3 = ImageTk.PhotoImage(fixed_images_with_proper_size[23])
        #     steffi_4 = ImageTk.PhotoImage(fixed_images_with_proper_size[24])
        #     suzane_1 = ImageTk.PhotoImage(fixed_images_with_proper_size[25])
        #
        #
        #     return [andre_aggasi_1, bill_tilden_1, bill_jean_king_1, bjorn_borg_1,chris_event_1,
        #             default_1, default_2, default_3, default_5, default_6, versus,hellen_wills_1,
        #             ken_rosewall_1,margaret_1, sakari_1, matina_2, naomi_1,novak_1, pete_1,
        #             rafael_1,rod_1,roger_1,roy_1, serena_3,steffi_4, suzane_1]
        #
        # def listing_images_each_player():
        #
        #     finished_images_players = load_images_with_PhotoImage()
        #
        #     andre_aggasi_list_images = finished_images_players[0]
        #     bill_tilden_list_images = finished_images_players[1]
        #     bill_jean_king_list_images = finished_images_players[2]
        #     bjorn_borg_list_images = finished_images_players[3]
        #     chris_event_list_images = finished_images_players[4]
        #     hellen_wills_list_images = finished_images_players[11]
        #     ken_rosewall_list_images = finished_images_players[12]
        #     margaret_list_images = finished_images_players[13]
        #     sakari_list_images = finished_images_players[14]
        #     matina_list_images = finished_images_players[15]
        #     naomi_list_images = finished_images_players[16]
        #     novak_list_images = finished_images_players[17]
        #     pete_list_images = finished_images_players[18]
        #     rafael_list_images = finished_images_players[19]
        #     rod_list_images = finished_images_players[20]
        #     roger_list_images = finished_images_players[21]
        #     roy_list_images = finished_images_players[22]
        #     serena_list_images = finished_images_players[23]
        #     steffi_list_images = finished_images_players[24]
        #     suzane_list_images = finished_images_players[25]
        #
        #     return [
        #         novak_list_images,
        #         margaret_list_images,
        #         rafael_list_images,
        #         serena_list_images,
        #         steffi_list_images,
        #         roger_list_images,
        #         #default_list_images,
        #         hellen_wills_list_images,
        #         matina_list_images,
        #         chris_event_list_images,
        #         bill_jean_king_list_images,
        #         roy_list_images,
        #         rod_list_images,
        #         bill_tilden_list_images,
        #         suzane_list_images,
        #         ken_rosewall_list_images,
        #         sakari_list_images,
        #         naomi_list_images,
        #         andre_aggasi_list_images,
        #         bjorn_borg_list_images,
        #         pete_list_images]
        #
        # def load_images_into_dictionary_with_name_images_as_key_values():
        #
        #     dictionary_names_with_images = {}
        #     list_image_of_each_player = listing_images_each_player()
        #     names_of_player_list = player_names()
        #
        #     nested_list_of_images_per_player = [list_image_of_each_player[0],list_image_of_each_player[1],list_image_of_each_player[2],list_image_of_each_player[3],
        #                                         list_image_of_each_player[4],list_image_of_each_player[5],list_image_of_each_player[6],list_image_of_each_player[7],
        #                                         list_image_of_each_player[8],list_image_of_each_player[9],list_image_of_each_player[10],list_image_of_each_player[11],
        #                                         list_image_of_each_player[12],list_image_of_each_player[13],list_image_of_each_player[14],list_image_of_each_player[15],
        #                                         list_image_of_each_player[16],list_image_of_each_player[17],list_image_of_each_player[18],list_image_of_each_player[19]]
        #
        #
        #     counter = 0
        #     for name in names_of_player_list:
        #         dictionary_names_with_images[name] = nested_list_of_images_per_player[counter]
        #         counter += 1
        #
        #     return dictionary_names_with_images

        def start_challenge():
            global name_of_challenger, name_of_opponent, match_result
            name_of_challenger = value_for_option_menu_1.get()
            name_of_opponent = value_for_option_menu_2.get()

            if name_of_challenger == "Select Player 1" or name_of_opponent == "Select Player 2":
                messagebox.showwarning("Invalid Selection", "Please select both players before proceeding.")
                new_window_for_challenge.destroy()
                return
            if name_of_challenger == name_of_opponent:
                messagebox.showwarning("Invalid Selection", "Player 1 and Player 2 cannot be the same.")
                new_window_for_challenge.destroy()
                return

            try:
                global all_players_list, id_of_challenger, id_of_opponent
                all_players_list = player_service_initialization.get_all_players()
                id_of_challenger = ''
                id_of_opponent = ''
                for index in all_players_list:
                    if index.name == name_of_challenger:
                        id_of_challenger = index.player_id
                    elif index.name == name_of_opponent:
                        id_of_opponent = index.player_id

                match_result = match_service.simulate_round(id_of_challenger, id_of_opponent)

                if not match_result or (isinstance(match_result, dict) and "error" in match_result):
                    error_msg = match_result.get("error", "Could not create match.")
                    messagebox.showerror("Invalid Match", error_msg)
                    new_window_for_challenge.destroy()
                    return

                ####
                # Check if it's the tournament winner
                if isinstance(match_result, dict) and "tournament_winner" in match_result:
                    messagebox.showinfo("🏆 Tournament Complete",
                                        f"The tournament has ended!\nWinner: {match_result['tournament_winner']}")
                else:
                    summary = ""
                    for result in match_result:
                        summary += f"{result['challenger']} vs {result['opponent']} → Winner: {result['winner']} ({result['score']})\n"
                    messagebox.showinfo("Round Completed", summary)

                messagebox.showinfo("Success", "The challenge has been simulated successfully.")
                refresh_leaderboard()
                new_window_for_challenge.destroy()
                #playing_mini_video_before_presentation_of_user_choice_players(name_of_challenger, name_of_opponent)

            except Exception as e:
                messagebox.showerror("Error", str(e))
                new_window_for_challenge.destroy()

        # def playing_mini_video_before_presentation_of_user_choice_players(name_challenger, name_opponent):
        #     default_images_for_mini_video_before_presentation = load_images_with_PhotoImage()
        #     default_images_for_running_presentation = default_images_for_mini_video_before_presentation[5:10]
        #
        #     try:
        #         new_window_for_default_images_presentation = tk.Toplevel(parent_frame)
        #         new_window_for_default_images_presentation.geometry("430x400")
        #         new_window_for_default_images_presentation.resizable(False, False)
        #         new_window_for_default_images_presentation.configure(bg="#45a049")
        #         loading_label = tk.Label(new_window_for_default_images_presentation, text="LOADING",bg="#45a049",fg="white",font=("Arial", 22))
        #         loading_label.pack()
        #
        #         dot_label = tk.Label(new_window_for_default_images_presentation, text="",bg="#45a049",fg="white",font=("Arial", 26))
        #         default_image_label = tk.Label(new_window_for_default_images_presentation,bg="#45a049",text="")
        #
        #         global num_index_of_dots
        #         num_index_of_dots = 0
        #
        #         def running_dots_with_images_same_time():
        #             global num_index_of_dots
        #             dots_string = "." * num_index_of_dots
        #             dot_label.config(text=dots_string)
        #             dot_label.pack()
        #             num_index_of_dots += 1
        #             if num_index_of_dots > 4:
        #                 num_index_of_dots = 0
        #             new_window_for_default_images_presentation.after(500, running_dots_with_images_same_time)
        #
        #         def counting_time_for_running_images(num):
        #             try:
        #                 if num < len(default_images_for_running_presentation):
        #                     image_showing = default_images_for_running_presentation[num]
        #                     image_showing.label = image_showing
        #                     default_image_label.config(image=image_showing)
        #                     default_image_label.pack()
        #                     new_window_for_default_images_presentation.after(2500, counting_time_for_running_images,
        #                                                                      num + 1)
        #                 else:
        #                     new_window_for_default_images_presentation.after(500,
        #                                                                      check_if_mini_video_finish_and_continue)
        #             except Exception as e:
        #                 messagebox.showinfo("Error", f"Error in mini video: {str(e)}")
        #
        #         def check_if_mini_video_finish_and_continue():
        #             new_window_for_default_images_presentation.destroy()
        #             playing_choice_user_match(name_challenger, name_opponent, match_result)
        #
        #         running_dots_with_images_same_time()
        #         counting_time_for_running_images(0)
        #
        #     except Exception as e:
        #         messagebox.showinfo("Error", f"Error: {str(e)}")

        # def playing_choice_user_match(challenger_name, opponent_name, match_result):
        #     default_images_for_playing_choice_user_match = load_images_with_PhotoImage()
        #
        #     try:
        #         ChallengerName = False
        #         OpponentName = False
        #         window_playing_choice_user_match = tk.Toplevel(parent_frame)
        #         window_playing_choice_user_match.geometry("930x450")
        #         window_playing_choice_user_match.resizable(False, False)
        #         window_playing_choice_user_match.configure(bg="#45a049")
        #         dictionary = load_images_into_dictionary_with_name_images_as_key_values()
        #
        #         for key, value in dictionary.items():
        #             if challenger_name == key:
        #                 name_challenger_label = tk.Label(window_playing_choice_user_match, text=key,bg="#45a049",fg="white",font=("Arial", 14))
        #                 challenger_photo = value
        #                 challenger_label = tk.Label(window_playing_choice_user_match,bg="#45a049",image=challenger_photo)
        #                 challenger_label.image = challenger_photo
        #                 name_challenger_label.grid(row=0, column=0)
        #                 challenger_label.grid(row=1, column=0)
        #                 ChallengerName = True
        #             if opponent_name == key:
        #                 name_opponent_label = tk.Label(window_playing_choice_user_match, text=key,bg="#45a049",fg="white",font=("Arial", 14))
        #                 opponent_photo = value
        #                 opponent_label = tk.Label(window_playing_choice_user_match,bg="#45a049",image=opponent_photo)
        #                 opponent_label.image = opponent_photo
        #                 name_opponent_label.grid(row=0, column=3)
        #                 opponent_label.grid(row=1, column=3)
        #                 OpponentName = True
        #             if ChallengerName and OpponentName:
        #                 versus_label = tk.Label(window_playing_choice_user_match,bg="#45a049",
        #                                         image=default_images_for_playing_choice_user_match[25])
        #                 versus_photo = default_images_for_playing_choice_user_match[10]
        #                 versus_label.image = versus_photo
        #                 versus_label.grid(row=1, column=2)
        #
        #         score_label = tk.Label(window_playing_choice_user_match, text="",bg="#45a049",fg="white",font=("Arial", 24))
        #         score_label.grid(row=3, column=2, pady=10)
        #
        #         winner_label = tk.Label(window_playing_choice_user_match, text="",bg="#45a049",fg="white",font=("Arial", 24))
        #         winner_label.grid(row=4, column=2, pady=10)
        #
        #         the_game_will_start_in_label = tk.Label(window_playing_choice_user_match,
        #                                                 text="THE GAME WILL START IN...",bg="#45a049",fg="white",font=("Arial", 22))
        #         the_game_will_start_in_label.grid(row=2, column=2)
        #
        #         time_running_label = tk.Label(window_playing_choice_user_match, text="",bg="#45a049",fg="white",font=("Arial", 22))
        #         time_running_label.grid(row=3, column=2)
        #
        #         def deleting_titles_time_running_and_game_will_start():
        #             the_game_will_start_in_label.destroy()
        #             time_running_label.destroy()
        #
        #         def inserting_time_with_score_winner_labels():
        #             score_label.config(text=f"Set Score: {match_result['score']}")
        #             winner_label.config(text=f"Winner: {match_result['winner']}")
        #
        #         def countdown_time_game():
        #             def counting_num(num):
        #                 if num > 0:
        #                     time_running_label.config(text=str(num))
        #                     window_playing_choice_user_match.after(1000, counting_num, num - 1)
        #                 elif num == 0:
        #                     deleting_titles_time_running_and_game_will_start()
        #                     inserting_time_with_score_winner_labels()
        #
        #             counting_num(3)
        #         countdown_time_game()
        #
        #
        #
        #     except Exception as e:
        #         messagebox.showinfo("Error", f"Error: {e}")



        start_challenge_button = tk.Button(frame_menu, text='Start Challenge',font=("Arial", 12), command=start_challenge)
        start_challenge_button.grid(row=4, column=1, padx='10', pady='10')

    challenge_button = tk.Button(parent_frame, text="Challenge", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                                 width=20, height=2, bd=0, relief="solid", activebackground="#45a049",
                                 activeforeground="white" ,command=challenge_action)
    return challenge_button