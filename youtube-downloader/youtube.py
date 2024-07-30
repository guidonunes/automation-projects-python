from pytube import YouTube
from tkinter import Tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res = streams.get_highest_resolution()
        highest_res.download(output_path=save_path)
        print("Downloaded successfully!")

    except Exception as e:
        print(e)
