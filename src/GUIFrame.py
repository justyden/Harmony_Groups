'''
import tkinter as tk
from tkinter import scrolledtext
import customtkinter
'''
import tkinter as tk
from tkinter import scrolledtext
import customtkinter
import json
import os

'''
class GroupChatApp:
    def __init__(self, root, data):
        self.root = root
        self.root.title("Group Chat App")

        # Set Dark Mode Theme
        self.root.tk_setPalette(background="#001F3F", foreground="white", activeBackground="#003366", activeForeground="white")

        self.data = data  # Pass the data to the app

        # Chat Window
        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.chat_window.pack(padx=10, pady=10)
        self.chat_window.config(state=tk.DISABLED)  # Make it read-only

        # Message Input Field
        self.message_input = tk.Entry(root, width=40)
        self.message_input.pack(pady=5)

        # Send Button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        # Group Chat Options
        group_chat_options = [conv["conversationID"] for conv in data.get("conversations", [])]
        self.group_chat_var = tk.StringVar(value=group_chat_options[0] if group_chat_options else "")
        self.group_chat_menu = tk.OptionMenu(root, self.group_chat_var, *group_chat_options)
        self.group_chat_menu.config(bg="#001F3F", fg="white")  # Use hexadecimal color code for dark blue
        self.group_chat_menu.pack(pady=5)

    def send_message(self):
        # Get the message from the input field
        message = self.message_input.get()

        if message:
            # Get the selected conversation ID
            selected_conversation = self.group_chat_var.get()

            # Find the selected conversation in the data
            conversation = next((conv for conv in self.data.get("conversations", []) if conv["conversationID"] == selected_conversation), None)

            if conversation:
                # Append the message to the selected conversation
                conversation["messages"].append({"sender": "You", "text": message})

                # Update the chat window
                self.update_chat_window(selected_conversation, message)

                # Clear the message input field
                self.message_input.delete(0, tk.END)

    def update_chat_window(self, conversation_id, message):
        # Find the selected conversation in the data
        conversation = next((conv for conv in self.data.get("conversations", []) if conv["conversationID"] == conversation_id), None)

        if conversation:
            # Update the chat window with the latest messages
            self.chat_window.config(state=tk.NORMAL)
            self.chat_window.delete(1.0, tk.END)  # Clear existing content

            for msg in conversation["messages"]:
                self.chat_window.insert(tk.END, f"{msg['sender']}: {msg['text']}\n")

            # Append the new message
            self.chat_window.insert(tk.END, f"You: {message}\n")

            self.chat_window.config(state=tk.DISABLED)

if __name__ == "__main__":
    file_name = "Database.txt"
    data = {}

    # Read data from the file
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            data = json.loads(file_content)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

    root = tk.Tk()
    app = GroupChatApp(root, data)
    root.mainloop()
'''
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