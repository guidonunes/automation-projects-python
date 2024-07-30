from pytube import YouTube
from tkinter import tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)

    except Exception as e:
        print(e)
