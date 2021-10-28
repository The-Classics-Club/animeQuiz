#----------picking random anime-------------

import json

link_dict = {}      #dictionary of "anime_name" : "op_link" pair
titles = []         #list of anime_titles

with open("anime_db.json", "r") as file:        #extracting data from json file
    link_dict = json.load(file)
    titles = list(link_dict.keys())
    file.close() 

#---------downloading random op------------
from random import choice 
from pytube import YouTube

anime_title = choice(titles)       #title of randomly chosen anime

path = "C:/Users/suraj das/Documents/Projects/AnimeQuiz/ops/"        #path of download
res = "360p"        #resolution of video

link = link_dict[anime_title]
video = YouTube(link)
video_link = video.streams.filter(res=res).first()
video_link.download(path)

#-----------trimming anime_op--------------
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from random import randint

file_path = path + video_link.title + ".mp4"        #path of anime_op
target_path = path + video_link.title + " trimmed" + ".mp4"     #path of trimmed anime_op

clip_size = int(VideoFileClip(file_path).duration)        # Opening the clip and getting its duration

# Difficulty modes
modes = [20, 10, 5, 1]

start_pt = randint(0,clip_size-20)      # Setting random values for clipping points between 20 seconds

end_pt = start_pt + 20

ffmpeg_extract_subclip(file_path, start_pt, end_pt, targetname=target_path)        ## Clipping the final video