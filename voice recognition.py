import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    output.config(text="Assistant: " + text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            output.config(text="Listening...")
            root.update()

            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()

            output.config(text="You said: " + command)

            if "hello" in command:
                speak("Hello! Welcome to the Voice User Interface.")
            elif "time" in command:
                from datetime import datetime
                current_time = datetime.now().strftime("%I:%M %p")
                speak("Current time is " + current_time)
            elif "date" in command:
                from datetime import datetime
                current_date = datetime.now().strftime("%d %B %Y")
                speak("Today's date is " + current_date)
            elif "exit" in command or "close" in command:
                speak("Goodbye!")
                root.destroy()
            else:
                speak("Sorry, I didn't understand that command.")

    except Exception:
        messagebox.showerror("Error", "Could not recognize your voice.")

# GUI
root = tk.Tk()
root.title("Voice User Interface")
root.geometry("500x350")
root.configure(bg="#E8F6F3")

title = tk.Label(
    root,
    text="Voice User Interface",
    font=("Arial", 22, "bold"),
    bg="#E8F6F3",
    fg="#2C3E50"
)
title.pack(pady=20)

instruction = tk.Label(
    root,
    text="Click the button and say:\nHello, Time, Date, or Exit",
    font=("Arial", 12),
    bg="#E8F6F3"
)
instruction.pack(pady=10)

listen_btn = tk.Button(
    root,
    text="🎤 Start Listening",
    font=("Arial", 14),
    bg="#3498DB",
    fg="white",
    width=20,
    command=listen
)
listen_btn.pack(pady=20)

output = tk.Label(
    root,
    text="Press the button to begin.",
    font=("Arial", 12),
    bg="#E8F6F3",
    wraplength=450
)
output.pack(pady=20)

root.mainloop()