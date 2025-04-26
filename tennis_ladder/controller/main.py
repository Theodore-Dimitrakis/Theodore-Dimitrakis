import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from InitializeButton import InitializeButton
from ManageButton import ManageButton
from controller.ChallengeButton import create_challenge_button  # Import the Challenge button function
from controller.StatisticsButton import create_statistics_button  # Import the Statistics button function
from controller.ExitButton import create_exit_button  # Import the Exit button function
from controller.Leaderboard import add_leaderboard_to_main_window  # Import the leaderboard function

# Create of main_window for tkinter
main_window = tk.Tk()
main_window.title("Tennis Ladder")
main_window.state("zoomed")  # Full size of window

# Set the background image
background_image = ImageTk.PhotoImage(Image.open("maurits-bausenhart-XtcZbSPVJ3A-unsplash.png"))
background_label = tk.Label(main_window, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the entire window

# Create Frame for All_buttons
button_frame = tk.Frame(main_window, bg='black', bd=2)  # Frame for buttons
button_frame.pack(side="left", fill="y", pady='160')  # Places the frame vertically on the left side

# Create Frame for Leaderboard
leaderboard_frame = tk.Frame(main_window, bg="white", bd=2, width=600, height=450)  # Tripled dimensions
leaderboard_frame.place(relx=0.2, rely=0.1)  # Position it next to the buttons

#Add the leaderboard to the leaderboard frame and get the refresh function
refresh_leaderboard = add_leaderboard_to_main_window(leaderboard_frame)

# Add the Initialize button to the button frame
initialize_button = InitializeButton(button_frame, refresh_leaderboard)
initialize_button.get_button().pack(padx=10, pady=10)

#Add the Manage button to the button frame with a refresh function for the leaderboard
manage_button = ManageButton(button_frame, refresh_leaderboard)
manage_button.pack(padx=10, pady=10)

# Add the Challenge button to the button frame
challenge_button = create_challenge_button(button_frame)
challenge_button.pack(padx=10, pady=10)

# Add the Statistics button to the button frame
statistics_button = create_statistics_button(button_frame)
statistics_button.pack(padx=10, pady=10)

# Create the Exit button
exit_button = create_exit_button(button_frame, main_window)
exit_button.pack(padx=10, pady=10)

# Display Tkinter window
main_window.mainloop()