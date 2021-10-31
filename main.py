import json
from random import choice
from pytube import YouTube
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from random import randint

#----------------function to get anime dict---------------

def anime_fetch(dict_len=437):      

    anime_dict = {}

    with open("anime_db.json", "r") as file:        #get data from json and converting into dictionary
        db = json.load(file)
        titles = list(db.keys())
    
    if dict_len == 437:     #getting whole db output if input not given / or is default
        anime_dict = db
        return anime_dict

    elif dict_len > 437 or dict_len == 0 or dict_len < 0:       #if argument is invalid
        print("invalid input")
        return None

    else:       #gettind random anime names if input is given

        random_list = []

        for i in range(dict_len):
            anime_name = choice(titles)
            titles.remove(anime_name)       #to avoid repeating of name
            random_list.append(anime_name)
            
        for name in random_list:
            anime_dict[name] = db[name]

        return anime_dict

#----------------anime op downloader-----------------
res = "360p"

def op_download(links):

    path = os.getcwd() + r"\anime_ops"
    titles = list(links.keys())
    file_name = []

    for title in titles:
        video = YouTube(links[title])
        req_video = video.streams.filter(res=res).first()

        file_name.append(req_video.default_filename)

        req_video.download(path)
        print("done")

    print(file_name)
    print(titles)
    
    trimmer(file_name, titles)

#-----------trimming video----------
def trimmer(file_name, titles):
    path = os.getcwd()

    for i in range(len(file_name)):
        file_path = path + r"\anime_ops" +"\\" +  file_name[i]      #path of anime_op
        target_path = path + r"\anime_ops" + "\\" + titles[i] + ".mp4"     #path of trimmed anime_op

        clip_size = int(VideoFileClip(file_path).duration)        # Opening the clip and getting its duration

        start_pt = randint(0,clip_size-20)      # Setting random values for clipping points between 20 seconds

        end_pt = start_pt + 20

        ffmpeg_extract_subclip(file_path, start_pt, end_pt, targetname=target_path)        ## Clipping the final video

db = anime_fetch(1)
print(db)
op_download(db)

print("done")
