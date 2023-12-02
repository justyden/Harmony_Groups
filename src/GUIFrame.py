import customtkinter
from tkinter import messagebox
from Verify_Users import check_user_in_list, check_user_in_group, put_users_in_group
from Read_Data import update_conversation, read_file, find_database
import random


# Colors for the application.
running_color = "#3399BB"
swimming_color = '#44FF44'
surfing_color = '#990099'
hiking_color = '#492374'
reading_color = '#0012BB'
sports_color = '#BB237A'
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
        self.groups = put_users_in_group()
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
        self.group_selection = groupChatSelection(master=self, values=["Running", "Swimming", "Surfing", "Hiking", "Reading", "Sports"], combobox_action=self.change_group)
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
            if random.random() < 0.2:
                self.display_inspirational_quote()
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

    def display_inspirational_quote(self):
        """
        Display a random inspirational quote.
        """
        inspirational_quotes = [
            "Believe you can and you're halfway there. -Theodore Roosevelt",
            "The only way to do great work is to love what you do. -Steve Jobs",
            "Your time is limited, don't waste it living someone else's life. -Steve Jobs",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
            "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
            "The best way to predict the future is to create it. -Peter Drucker",
            "You miss 100% of the shots you don't take. -Wayne Gretzky",
            "In the middle of difficulty lies opportunity. -Albert Einstein",
            "The only person you are destined to become is the person you decide to be. -Ralph Waldo Emerson",
            "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
            "It always seems impossible until it's done. -Nelson Mandela",
            "Your attitude, not your aptitude, will determine your altitude. -Zig Ziglar",
            "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. -Roy T. Bennett",
            "The only impossible journey is the one you never begin. -Tony Robbins",
            "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
            "It's not whether you get knocked down, it's whether you get up. -Vince Lombardi",
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
            "Success is stumbling from failure to failure with no loss of enthusiasm. -Winston S. Churchill",
            "The only place where success comes before work is in the dictionary. -Vidal Sassoon",
            "Hard work beats talent when talent doesn't work hard. -Tim Notke"
        ]

        quote = random.choice(inspirational_quotes)

        # Display the quote using a messagebox or any other suitable method
        messagebox.showinfo("Inspirational Quote", quote)

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
        elif group_name == "Hiking":
            border_color_ = hiking_color
        elif group_name == "Reading":
            border_color_ = reading_color
        elif group_name == "Sports":
            border_color_ = sports_color
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
        if check_user_in_group(self.groups, group_name, self.user_id):
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
        else:
            messagebox.showinfo("Not a Participant", "You are not a participant in the selected group.")

        
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
