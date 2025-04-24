import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from InitializeButton import InitializeButton
from ManageButton import ManageButton
from ChallengeButton import ChallengeButton
from StatisticsButton import StatisticsButton
# Create of main_window for tkinter
main_window = tk.Tk()
main_window.title("Tennis Ladder")
main_window.state("zoomed")  # Full size of window

# Upload Picture for pathing
image = Image.open("maurits-bausenhart-XtcZbSPVJ3A-unsplash.png")

#Transaction from Uploading to Picture
photo = ImageTk.PhotoImage(image)

#Create background_label(full-sized)for the Image
background_label = tk.Label(main_window, image=photo)
background_label.place(relwidth=1, relheight=1, x=0, y=0)  # Κάνει την εικόνα να καλύπτει όλο το παράθυρο

#Create Frame for All_buttons
button_frame = tk.Frame(main_window,bg='black',bd=2)  # Frame για κουμπιά
button_frame.pack(side="left", fill="y",pady='160')  # Τοποθετεί το frame κάθετα στην αριστερή πλευρά

# # Δημιουργία Scrollbar σε ξεχωριστό frame
# scrollbar_frame = tk.Frame(main_window)  # Ξεχωριστό frame για το scrollbar
# scrollbar_frame.pack(side="right", fill="y")
#
# scrollbar = tk.Scrollbar(scrollbar_frame, orient="vertical")
# scrollbar.pack(side="right", fill="y")
#
# # Εδώ δημιουργούμε το Canvas για scrolling
# canvas = tk.Canvas(scrollbar_frame)
# canvas.pack(side="left", fill="both", expand=True)
#
# # Συνδέουμε το scrollbar με τον canvas
# canvas.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=canvas.yview)

# # Δημιουργία των κουμπιών μέσα στον canvas
# button_frame_canvas = tk.Frame(canvas)
# canvas.create_window((0, 0), window=button_frame_canvas, anchor="nw")

#Initialization of Buttons with cooperation of .py Buttons
initialize_button = InitializeButton(button_frame)
initialize_button.get_button().pack(padx=10, pady=10)

manage_button = ManageButton(button_frame)
manage_button.get_button().pack(padx=10, pady=10)

challenge_button = ChallengeButton(button_frame)
challenge_button.get_button().pack(padx=10, pady=10)

statistics_button = StatisticsButton(button_frame)
statistics_button.get_button().pack(padx=10, pady=10)

# Function to exit the application linked to btn_exit
def exit_application():
    main_window.destroy()

btn_exit = tk.Button(
    button_frame,
    text="Exit",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=20,
    height=2,
    bd=0,
    relief="solid",
    activebackground="#d32f2f",
    activeforeground="white",
    command=exit_application,
)

btn_exit.pack(padx=10, pady=10)

# # Ενημερώνουμε το scrollregion για να μπορεί το scrollbar να ενεργοποιηθεί
# button_frame_canvas.update_idletasks()
# canvas.config(scrollregion=canvas.bbox("all"))

#Display Tkinter window
main_window.mainloop()