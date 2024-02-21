import tkinter as tk
import tkinter.ttk as ttk
import youtube as yt
from tkinter import filedialog
from threading import Thread

def show_loading_message():
    status_label.config(text="Downloading, please wait...")

def download_audio_process():
    try:
        url = url_entry.get()
        yt.check_download(url)
        status_label.config(text="Download complete!")
    except Exception as e:
        status_label.config(text="An error occurred. Please check the URL and try again.")

def download_audio():
    show_loading_message()
    Thread(target=download_audio_process).start()

def open_file_process():
    try:
        file_path = filedialog.askopenfilename()
        yt.download_audio_from_file(file_path)
        status_label.config(text="Download complete!")
    except Exception as e:
        status_label.config(text="An error occurred. Please check the file and try again.")

def open_file():
    show_loading_message()
    Thread(target=open_file_process).start()

root = tk.Tk()
root.geometry('500x300')
root.title('My YouTube Downloader')

url_label = tk.Label(root, text="YouTube URL:", font=("Arial", 14))
url_label.pack(padx=10, pady=10)

url_entry = tk.Entry(root, font=("Arial", 14))
url_entry.pack(padx=10, pady=10)

download_button = tk.Button(root, text="Download Audio", command=download_audio, font=("Arial", 14))
download_button.pack(padx=10, pady=10)

file_button = tk.Button(root, text="Open File", command=open_file, font=("Arial", 14))
file_button.pack(padx=10, pady=10)

status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(padx=10, pady=10)


root.mainloop()