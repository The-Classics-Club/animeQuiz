import json
from random import choice
from pytube import YouTube
import os
import shutil
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from random import randint

#----------------function to get anime dict---------------

def anime_fetch(dict_len=1):      

    anime_dict = {}

    with open("anime_db.json", "r") as file:        #get data from json and converting into dictionary
        db = json.load(file)
        links = list(db.keys())
    
    if dict_len == 437:     #getting whole db output if input not given / or is default
        anime_dict = db
        return anime_dict

    elif dict_len > 437 or dict_len == 0 or dict_len < 0:       #if argument is invalid
        print("invalid input")
        return None

    else:       #gettind random anime names if input is given

        random_list = []

        for i in range(dict_len):
            anime_name = choice(links)
            links.remove(anime_name)       #to avoid repeating of name
            random_list.append(anime_name)
            
        for name in random_list:
            anime_dict[name] = db[name]

        return anime_dict

#----------------anime op downloader-----------------
res = "360p"

def op_download(link):

    path = os.getcwd() + r"\anime_ops"
    file_name = ''

    video = YouTube(link)
    req_video = video.streams.filter(res=res).first()

    file_name = req_video.default_filename

    req_video.download(path)
    print("done")

    print(file_name)
    print(link)
    
    trimmer(file_name)

#-----------trimming video----------
def trimmer(file_name):
    global target_path, file_path
    path = os.getcwd()

    file_path = path + r"\anime_ops" +"\\" +  file_name      #path of anime_op
    target_path = path + r"\anime_ops" + "\\" + 'anime_op' + ".mp4"     #path of trimmed anime_op

    clip_size = int(VideoFileClip(file_path).duration)        # Opening the clip and getting its duration

    start_pt = randint(0,clip_size-20)      # Setting random values for clipping points between 20 seconds

    end_pt = start_pt + 20

    ffmpeg_extract_subclip(file_path, start_pt, end_pt, targetname=target_path)        ## Clipping the final video

def clean_folder():
    folder = os.getcwd() + '\\anime_ops'
    shutil.rmtree(folder)
    os.mkdir(folder)
    with open(f"{folder}\\.gitignore", 'w') as fp:
        pass