import customtkinter
from tkinter import messagebox
from Verify_Users import check_user_in_list
from Read_Data import update_conversation, read_file, find_database


# Colors for the application.
running_color = "#3399BB"
swimming_color = '#44FF44'
surfing_color = '#990099'
background_gray = "#333333"
light_gray1 = "#555555"
light_gray2 = "#333333"
white = '#EEEEEE'

# This is the application GUI.
class App(customtkinter.CTk):
    """
    The main application.
    """
    def __init__(self):
        """
        Starts the application.
        """
        super().__init__()

        customtkinter.set_default_color_theme("dark-blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Harmony Groups")
        self.geometry("400x200")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.sign_in()

    def initialize_app(self):
        """
        Creates the main application layout.
        """
        self.geometry("400x550")
        self.message_log = customtkinter.CTkTextbox(master=self, width=400, height=310, corner_radius=10, border_width=1, border_color=light_gray2)
        self.message_log.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.message_log.configure(state="disabled")
        self.message_input = customtkinter.CTkTextbox(master=self, width=400, height = 30, corner_radius=10, border_width=1, border_color=light_gray2)
        self.message_input.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.button = customtkinter.CTkButton(self, text="Send Message", corner_radius=10, fg_color=background_gray, border_width=1, border_color=light_gray2, hover_color=light_gray1, text_color=white, command=self.send_message)
        self.button.grid(row=3, column=0, padx=100, pady=1, sticky="ew", columnspan=2)
        # This creates a combobox and places it in a transparent frame. It is important to note that
        # there is a combobox_callback function that will do a command when an option is selected.
        self.group_selection = groupChatSelection(master=self, values=["Running", "Swimming", "Surfing"], combobox_action=self.change_group)
        self.group_selection.grid(row=4, column=0, padx=10, pady=(1, 140), sticky="s")
        self.group_selection.configure(fg_color="transparent")
        self.header = customtkinter.CTkLabel(self, width=15, height=110, text="No Group Selected", fg_color="transparent", font=("calibri", 27))
        self.header.grid(row=0, column=0, padx=10, pady=5, sticky="new")
        self.display_user_name = customtkinter.CTkLabel(self, width=15, height=5, text=self.user_name, fg_color="transparent", font=("calibri", 10))
        self.display_user_name.grid(row=0, column=0, padx=0, pady=(5, 5), sticky="ne")
        self.display_user_id = customtkinter.CTkLabel(self, width=15, height=5, text=self.user_id, fg_color="transparent", font=("calibri", 10))
        self.display_user_id.grid(row=0, column=0, padx=0, pady=(0,0), sticky="se")
        self.picked_group = False
    
    def send_message(self):
        """
        Sends a message to a group and updates the database. 
        """
        if not self.picked_group:
            return
        message_text = self.message_input.get("1.0", "end-1c")
        if message_text:
            group_name = self.group_selection.combobox.get()

            # Update the conversation file with the new message
            update_conversation(group_name, message_text, self.user_name)

            # Display the message in the message log
            self.message_log.configure(state="normal")
            self.message_log.insert("end", f"\n{self.user_name}: {message_text}")
            self.message_log.see("end")
            self.message_log.configure(state="disabled")

            # Clear the message input
            self.message_input.delete("1.0", "end")

    def sign_in(self):
        """
        Creates the sing in page.
        """
        self.user_name_label = customtkinter.CTkLabel(self, width=15, height=50, text="User Name:", fg_color="transparent", font=("calibri", 20))
        self.user_name_label.grid(row=0, column=0, padx=0, pady=1, sticky="n")
        self.input_user_name = customtkinter.CTkTextbox(master=self, width=250, height = 20, corner_radius=10, border_width=1, border_color=running_color)
        self.input_user_name.grid(row=0, column=1, padx=0, pady=1, sticky="n")
        self.user_id_label = customtkinter.CTkLabel(self, width=15, height=50, text="User ID:", fg_color="transparent", font=("calibri", 20))
        self.user_id_label.grid(row=1, column=0, padx=0, pady=1, sticky="n")
        self.input_user_id = customtkinter.CTkTextbox(master=self, width=250, height = 20, corner_radius=10, border_width=1, border_color=running_color)
        self.input_user_id.grid(row=1, column=1, padx=0, pady=1, sticky="n")
        self.login_button= customtkinter.CTkButton(self, text="Login", corner_radius=10, fg_color=background_gray, border_width=1,               border_color=running_color, hover_color=light_gray1, text_color=white, command=self.perform_login)
        self.login_button.grid(row=2, column=0, padx=100, pady=1, sticky="ew", columnspan=2)

    def perform_login(self):
        """
        Logs the user in.
        """
        user_name = self.input_user_name.get("1.0", "end-1c")
        user_id = self.input_user_id.get("1.0", "end-1c")

        # Validate the user
        if not check_user_in_list(user_name, user_id):
            self.input_user_name.delete("1.0", "end")
            self.input_user_id.delete("1.0", "end")
            messagebox.showerror("Invalid User", "User not found. Please try again.")
            return

        # Removes the login screen.
        self.user_name_label.destroy()
        self.input_user_name.destroy()
        self.user_id_label.destroy()
        self.input_user_id.destroy()
        self.login_button.destroy()

        # Store the user details
        self.user_id = user_id
        self.user_name = user_name
        self.initialize_app()

    def change_colors(self):
        """
        Change the border color of the objects.
        """
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

    def change_group(self):
        """
        Change the header label to the group_selection choice.
        """
        if not self.picked_group:
            self.picked_group = True
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


        
class groupChatSelection(customtkinter.CTkFrame):
    """
    A frame for group selection.
    """
    def __init__(self, master, values, combobox_action):
        """
        Creates each group.

        Args:
            master (customkinter.CTK): The application
            values (list): The name of each group
            combobox_action (_type_): The action performed when a group is selected
        """
        super().__init__(master)
        self.values = values
        self.action = combobox_action
        self.combobox = customtkinter.CTkComboBox(self, values = self.values, command=self.combobox_action_edited, corner_radius=10, border_width=1, border_color=light_gray2)
        self.combobox.grid(row=3, column=0, padx=10, pady=(1, 20), sticky="s")

    def combobox_action_edited(self, choice):
        """
        The action generated by the combobox.

        Args:
            choice (_type_): _description_
        """
        self.action()


if __name__ == "__main__":
    app = App()
    app.mainloop()