import customtkinter
from tkinter import messagebox
from pytube import YouTube
import os

class Button2:
    def __init__(self, app):
        self.app = app
    
    def button2_fucntion(self):
        title = customtkinter.CTkLabel(self.app, text="Füge den YouTube Link ein:", font=("arial", 20))
        title.pack(padx=20, pady=20)
        entry = customtkinter.CTkEntry(self.app, width=400, placeholder_text="YouTube Link hier einfügen")
        entry.pack(padx=20, pady=20)