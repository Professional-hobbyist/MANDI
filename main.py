import google.generativeai as genai
from google.generativeai.types.model_types import Model

import customtkinter as tk

# Configure your API key
API_KEY = "AIzaSyAGJAW7Uu5KsAczN_L0zaj5hqJZ8ku9sg0"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

messages = []

def initializeAI():
    file_path = 'prompt.txt'

    try:
        with open(file_path, 'r') as file:
            prompt = file.read()

        # Initialize chat with the prompt
        response = chat.send_message(prompt)
        #messages.append("Medbot: " + response.text)
        #displayChat(textbox, messages)
        return True
    except Exception as e:
        print("Error:", e)
        return False

def askGemini(user_message):
    response = chat.send_message(user_message)
    print("Bot:", response.text)

def displayChat(textbox, messages):
    textbox.configure(state="normal")

    textbox.delete("1.0", tk.END)
    for message in messages:
        textbox.insert(tk.END, message + "\n")
    textbox.see(tk.END)
    textbox.configure(state="disabled")

def sendMessage(messages):

    response = chat.send_message(entry.get()).text

    messages.append("ME: " + entry.get())
    messages.append("Medbot: " + response)
    displayChat(textbox, messages)

    entry.delete(0, tk.END)  

def onReturn(event):
    sendMessage(messages)

# Initialize the chatbot with the prompt from the file

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

app = tk.CTk()
app.title("M.A.N.D.I")
app.grid_columnconfigure(0, weight=1)
resolution = (app.winfo_screenwidth(), app.winfo_screenheight())

font_style = ("Helvetica", 14)

textbox = tk.CTkTextbox(app, height=0.74*resolution[1], width=0.51*resolution[0])
textbox.configure(state="disabled")
textbox.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

entry = tk.CTkEntry(app)
entry.grid(row=1, column=0, padx=20, pady=(5, 20), sticky="ew")
entry.bind("<Return>", onReturn)


if initializeAI():
    app.mainloop()
