import pytube
import os

def downloadAudio(link):
    # making youtube object with the link
    youtube = pytube.YouTube(link)

    # fetching good quality audio
    audio = youtube.streams.filter(only_audio=True).first()

    # to download the mp3
    mp3 = audio.download(filename="yt_audio")

    # to make it  mp3 extension
    file = mp3 + ".mp3"
    os.rename(mp3, file)

    print("Downloaded successfully!")


url = input("Enter the YouTube video's link: ")
downloadAudio(url)

