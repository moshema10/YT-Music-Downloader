from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm




def prompt():
    path = input("Enter your download location (Enter full path): ")
    link = input("Enter the link: ")
    return path, link

def DownloadSong():
    
    path,link = prompt()

    yt = YouTube(link)
    print(f"Downloading song : {yt.title}")
    
    yd = yt.streams.get_audio_only()
    yd.download(path)

def DownloadPlaylist():
    path,link = prompt()
    
    p = Playlist(link)
    for song in tqdm(p.videos):
        yd = song.streams.get_audio_only()
        print(f"\nDownloading song : {yd.title}")
        yd.download(path)

def Help():
    print("** Link: copy the full link from the YT")
    print("** Path: copy the full path for the directory location")




def menu():
    print("\nLet's Download Some Music\n")
    print("1. Download a song")
    print("2. Download a playlist")
    print("3. Help")
    number = int(input("Choose a number: "))
    print()
    if number == 1:
        DownloadSong()
    if number == 2:
        DownloadPlaylist()
    if number == 3:
        Help()
    else:
        print("Enter numbers from the range of [1-3]")
    
if __name__ == '__main__':
    menu()
