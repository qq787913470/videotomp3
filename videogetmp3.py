from moviepy.editor import *

video = VideoFileClip('少年.mp4')
audio = video.audio
# audio.write_audiofile('test.wav')
audio.write_audiofile('少年.mp3')
