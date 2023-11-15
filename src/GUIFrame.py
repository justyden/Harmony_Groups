import tkinter as tk
from tkinter import scrolledtext
import customtkinter

class GroupChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Group Chat App")
        
        # Set Dark Mode Theme
        customtkinter.set_default_color_theme("dark-blue")
        customtkinter.set_appearance_mode("dark")
        
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
        self.group_chat_var = tk.StringVar(value="Group 1")
        self.group_chat_menu = tk.OptionMenu(root, self.group_chat_var, "Group 1", "Group 2", "Group 3")
        self.group_chat_menu.pack(pady=5)

    def send_message(self):
        # Get the message from the input field
        message = self.message_input.get()
        
        if message:
            # Append the message to the chat window
            self.chat_window.config(state=tk.NORMAL)
            self.chat_window.insert(tk.END, f"You: {message}\n")
            self.chat_window.config(state=tk.DISABLED)
            
            # Clear the message input field
            self.message_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GroupChatApp(root)
    root.mainloop()