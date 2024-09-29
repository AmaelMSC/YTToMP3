from pytubefix import YouTube, Playlist
from pytubefix.innertube import _default_clients
import os

# Bypass Age restrict
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

Mode = int(input("Enter 1 for video downloading and 2 for playlist downloading : "))
if Mode != 1 and Mode != 2:
    print("Error")
    exit(1)

directory = str(
    input("Enter the name of the directory you want to save your files to : ")
)
if not os.path.exists("Output/"):
    os.mkdir("Output/")
if directory != "":
    os.mkdir("Output/" + directory)


def url_to_video(link):
    yt = YouTube(link, "WEB_CREATOR")
    video = yt.streams.filter(only_audio=True).first()
    return video


def download(video):
    out_file = video.download(output_path=("Output/" + directory))
    base, _ = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)


if Mode == 1:
    link = str(input("Enter the link you want to download : "))
    download(url_to_video(link))
    exit(0)


if Mode == 2:
    link = Playlist(str(input("Enter the link you want to download : ")), "WEB_CREATOR")
    for url in link.video_urls:
        download(url_to_video(url))
