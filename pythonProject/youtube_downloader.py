from pytube import YouTube
import tkinter as tk # tkinter -> python GUI
from tkinter import filedialog

#download -: 
def download_video(url,path):
    try:
        yt_vid = YouTube(url)
        # to download best quality of stream 
        stream = yt_vid.streams.filter(progressive=True,file_extension="mp4")

        #resolution
        highest_res_stream = stream.get_highest_resolution()
        highest_res_stream.download(output_path=path) # downloading resolution 
        print("Video Downloaded")

    except Exception as E:
        print(E)

def open_file_save():
    folder = filedialog.askdirectory() # asking folder directory
    if folder : # if something is typed
        print(f"folder location : {folder}")
    return folder    

if __name__ == "__main__": #executes as main

    #executes only when python is run
    root = tk.Tk() # instansiate a tkinter window -> req by filedialog
    root.withdraw() # hides the window 

    video_url = input("enter url : ")
    save_directory = open_file_save()

    if not save_directory:
        print('invalid location...please try again')
    else:
        print('Download Started .... ')
        download_video(video_url,save_directory)    
        print('Download finished ')