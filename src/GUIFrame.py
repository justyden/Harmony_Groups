import tkinter as tk
from tkinter import scrolledtext
import customtkinter
import json
import os


# This is the application GUI.
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_default_color_theme("dark-blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Harmony Groups")
        self.geometry("400x550")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self, width=400, height=310, corner_radius=0)
        self.textbox.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n" * 50)
        self.textbox.configure(state="disabled")
        self.button = customtkinter.CTkButton(self, text="Send Message")
        self.button.grid(row=1, column=0, padx=100, pady=1, sticky="ew", columnspan=2)
        # This creates a combobox and places it in a transparent frame. It is important to note that
        # there is a combobox_callback function that will do a command when an option is selected.
        self.combobox = groupChatSelection(self, values=["group 1", "group 2", "group 3"])
        self.combobox.grid(row=2, column=0, padx=10, pady=(1, 140), sticky="s")
        self.combobox.configure(fg_color="transparent")
        
class groupChatSelection(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.combobox = customtkinter.CTkComboBox(self, values = self.values, command=self.combobox_callback)
        self.combobox.grid(row=3, column=0, padx=10, pady=(1, 20), sticky="s")
    def combobox_callback(self, choice):
            print("combobox dropdown clicked:", choice)


app = App()
app.mainloop()