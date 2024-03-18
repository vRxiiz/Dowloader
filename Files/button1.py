import customtkinter
from tkinter import messagebox
from pytube import YouTube
import os

class Button1:
    def __init__(self, app):
        self.app = app
        
    def download_video(self, url):
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        video.download(download_path)
        messagebox.showinfo("Download abgeschlossen", "Das Video wurde erfolgreich heruntergeladen.")
        
    def button1_function(self):
        title = customtkinter.CTkLabel(self.app, text="Füge den YouTube Link ein:", font=("arial", 20))
        title.pack(padx=20, pady=20)

        entry = customtkinter.CTkEntry(self.app, width=400, placeholder_text="YouTube Link hier einfügen")
        entry.pack(padx=20, pady=20)
        
        def on_download_click():
            url = entry.get()  # URL aus dem Eingabefeld abrufen
            self.download_video(url)  # download_video-Funktion aufrufen

        download_button = customtkinter.CTkButton(self.app, text="Download", command=on_download_click)
        download_button.pack(pady=20)