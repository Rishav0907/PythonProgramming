import pytube
import subprocess
subprocess.call('clear')
video_url=str(input(">"))
youtube=pytube.YouTube(video_url)
video=youtube.streams.first()
video.download('/home/rishav/Desktop')

