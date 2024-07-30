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

def open_file_dialog():
    folder =filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder



if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    video_url = input("Enter the video URL: ")
    save_path = open_file_dialog()

    if save_path:
        print("Downloading...")
        download_video(video_url, save_path)
    else:
        print("No folder selected...")
