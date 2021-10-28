from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# Its so fast when u just import the functions you need 0_0
from moviepy.editor import VideoFileClip
from random import randint

# Opening the clip and getting its duration
clip_size = int(VideoFileClip('danda.mkv').duration)

# Setting random values for clipping points between 20 seconds
start_pt = randint(0,clip_size-20)
end_pt = start_pt + 20

# Clipping the final video
ffmpeg_extract_subclip("danda.mkv", start_pt, end_pt, targetname="test.mp4")  