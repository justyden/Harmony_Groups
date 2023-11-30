import tkinter as tk
from tkinter import scrolledtext
import customtkinter
import json
import os
from Read_Data import update_conversation, read_file, find_database


# Colors for the application.
running_color = "#3399BB"
swimming_color = '#44FF44'
surfing_color = '#990099'
background_gray = "#333333"
light_gray = "#555555"
white = '#EEEEEE'

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

        self.message_log = customtkinter.CTkTextbox(master=self, width=400, height=310, corner_radius=10, border_width=1, border_color=running_color)
        self.message_log.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.message_log.configure(state="disabled")
        self.message_input = customtkinter.CTkTextbox(master=self, width=400, height = 30, corner_radius=10, border_width=1, border_color=running_color)
        self.message_input.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.button = customtkinter.CTkButton(self, text="Send Message", corner_radius=10, fg_color=background_gray, border_width=1, border_color=running_color, hover_color=light_gray, text_color=white, command=self.send_message)
        self.button.grid(row=3, column=0, padx=100, pady=1, sticky="ew", columnspan=2)
        # This creates a combobox and places it in a transparent frame. It is important to note that
        # there is a combobox_callback function that will do a command when an option is selected.
        self.group_selection = groupChatSelection(master=self, values=["Running", "Swimming", "Surfing"], combobox_action=self.change_group)
        self.group_selection.grid(row=4, column=0, padx=10, pady=(1, 140), sticky="s")
        self.group_selection.configure(fg_color="transparent")
        self.header = customtkinter.CTkLabel(self, width=15, height=110, text=self.group_selection.combobox.get(), fg_color="transparent", font=("calibri", 27))
        self.header.grid(row=0, column=0, padx=10, pady=5, sticky="new")
        self.change_group()

    # Sends a message to a group and updates the database. 
    def send_message(self):
        message_text = self.message_input.get("1.0", "end-1c")
        if message_text:
            group_name = self.group_selection.combobox.get()
            user_id = "user1"  # Replace with the actual user ID; you may obtain it from user authentication or elsewhere.

            # Update the conversation file with the new message
            update_conversation(group_name, message_text, user_id)

            # Display the message in the message log
            self.message_log.configure(state="normal")
            self.message_log.insert("end", f"\n{user_id}: {message_text}")
            self.message_log.see("end")
            self.message_log.configure(state="disabled")

            # Clear the message input
            self.message_input.delete("1.0", "end")

    def change_colors(self):
        # Get the selected group name
        group_name = self.group_selection.combobox.get()

        # Change the color of borders for message log, message input, and button
        if group_name == "Running":
            border_color_ = running_color
        elif group_name == "Swimming":
            border_color_ = swimming_color
        elif group_name == "Surfing":
            border_color_ = surfing_color
        self.message_log.configure(border_color=border_color_)
        self.message_input.configure(border_color=border_color_)
        self.button.configure(border_color=border_color_)

        # Change the color of borders for the combobox in the group selection
        self.group_selection.combobox.configure(border_color=border_color_)

        # Update other widget borders if needed

        # You may need to call update_idletasks to ensure the changes take effect immediately
        self.update_idletasks()

    # A simple function that will change the header label to the group_selection choice.
    def change_group(self):
        group_name = self.group_selection.combobox.get()
        self.header.configure(text=group_name)
        self.change_colors()

        # Read the existing data from the file
        file_name = find_database()
        if file_name:
            data = read_file(file_name)

            # Display the messages in the message log for the selected group
            self.message_log.configure(state="normal")
            self.message_log.delete("1.0", "end")  # Clear existing content

            for conversation in data.get("conversations", []):
                if conversation["conversationID"] == group_name:
                    if "messages" in conversation:
                        for message in conversation["messages"]:
                            sender = message.get("sender", "")
                            text = message.get("text", "")
                            self.message_log.insert("end", f"\n{sender}: {text}")

            self.message_log.configure(state="disabled")


        
# The group selection.
class groupChatSelection(customtkinter.CTkFrame):
    def __init__(self, master, values, combobox_action):
        super().__init__(master)
        self.values = values
        self.action = combobox_action
        self.combobox = customtkinter.CTkComboBox(self, values = self.values, command=self.combobox_action_edited, corner_radius=10, border_width=1, border_color=running_color)
        self.combobox.grid(row=3, column=0, padx=10, pady=(1, 20), sticky="s")

    def combobox_action_edited(self, choice):
        self.action()


if __name__ == "__main__":
    app = App()
    app.mainloop()