import customtkinter
import tkinter as tk
from pytube import YouTube
import os
from tkinter import messagebox
import Files
from Files.button1 import Button1


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1290x720")
app.title("Python Projekt")

# Erstellen einer Instanz von Button1
button1_instance = Button1(app)

def reset_gui():
    for widget in app.winfo_children():
        widget.destroy()
    initialize_gui()

def on_button_click():
    button1_instance.button1_function()  # Funktion ausführen
    reset_button = customtkinter.CTkButton(app, text="Hauptmenü", command=reset_gui)
    reset_button.place(x=50, y=50)
    button1.destroy()

def initialize_gui():
    global button1
    button1 = customtkinter.CTkButton(
        master=app,
        text="YouTube Download MP4",
        height=100,
        width=200,
        command=on_button_click 
    )
    button1.place(relx=0.7, rely=0.4, anchor=customtkinter.CENTER)

initialize_gui()
app.mainloop()