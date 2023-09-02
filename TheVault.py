import customtkinter
import tkinter.messagebox as tkmb
from tkinter import filedialog
from tkinter import *

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Vault")
root.resizable(0, 0)



def wund():
	username = "admin"
	password = "12345"
	if entry.get() == username and entry1.get() == password:
		tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
		root.destroy()
		root2 = customtkinter.CTk()
		root2.geometry("700x600")
		root2.title("Vault")
		###- MAIN APP FUNCTIONS  -###
		frame_main = customtkinter.CTkFrame(master=root2)
		frame_main.pack(pady=35, padx=35, fill="both", expand=True)
		label_main = customtkinter.CTkLabel(master=frame_main, text="The Vault", font=("E-SQUARE", 50),  text_color=("#FFB300"))
		label_main.pack(pady=12)

		


		root2.mainloop()
	else:
		tkmb.showinfo(title="Login Incorrect",message="Login is incorrect, please try again")
		
################ DEF FUNCTIONS #################

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=35, padx=35, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login", font=("E-SQUARE", 50), text_color=("#FFB300"))
label.pack(pady=12)

entry = customtkinter.CTkEntry(master=frame, width=300, height=50, placeholder_text="Username", font=("E-SQUARE", 25), border_color=("#FFB300"))
entry1 = customtkinter.CTkEntry(master=frame, width=300, height=50, placeholder_text="Password", font=("E-SQUARE", 25), border_color=("#FFB300"))

button1 = customtkinter.CTkButton(master=frame, width=150, height=25, text="Login", font=("E-SQUARE", 25), fg_color=("#FFB300"), text_color=("#363636"), command=wund)
button2 = customtkinter.CTkButton(master=frame, width=150, height=25, text="Forgot Password/Username? Click here", font=("E-SQUARE", 15), fg_color=("transparent"), text_color=("#FFB300"))

entry.pack(pady=20)
entry1.pack(pady=20)
button1.pack(pady=20)
button2.pack(pady=20)

root.mainloop()