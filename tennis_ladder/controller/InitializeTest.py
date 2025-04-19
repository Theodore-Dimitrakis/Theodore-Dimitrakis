import tkinter as tk
# from tkinter import PhotoImage

main_window = tk.Tk()
main_window.title('Tennis Ladder')
main_window.geometry('1000x600')
# main_window.iconbitmap('tennis_icon_app.ico')


# top_frame =tk.Frame(main_window,bg='blue',highlightbackground='yellow',highlightcolor='red',width='600',height='80')
# left_frame = tk.Frame(main_window,bg='red',width='200',height='50')#)#,relief='sunken',width='50',height='300')
# top_frame.grid(row=0,column=0,)
# left_frame.grid(row=1,column=0,pady='20',sticky='w')


btn_initialize = tk.Button(main_window, text='Initialize', font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white', width=20, height=2, bd=0, relief='solid', activebackground='#45a049', activeforeground='white')
btn_challenge = tk.Button(main_window, text='Challenge', font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white', width=20, height=2, bd=0, relief='solid', activebackground='#45a049', activeforeground='white')
btn_manage = tk.Button(main_window, text='Manage', font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white', width=20, height=2, bd=0, relief='solid', activebackground='#45a049', activeforeground='white')
btn_statistics = tk.Button(main_window, text='Statistics', font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white', width=20, height=2, bd=0, relief='solid', activebackground='#45a049', activeforeground='white')

# background_photo = PhotoImage(file='maurits-bausenhart-XtcZbSPVJ3A-unsplash.png')
# photo =tk.Label(main_window, image =background_photo,height='800')
# photo.place(x = 0, y = 0)
btn_initialize.pack(pady='20',command=initialize_db)
btn_challenge.pack(pady='20')
btn_manage.pack(pady='20')
btn_statistics.pack(pady='20')

main_window.mainloop()