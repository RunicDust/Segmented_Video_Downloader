import subprocess as sp
from defines import FFMPEG_BIN, output_dir

def merge_audio_with_video(video_filename, audio_filename, number):
    global filename
    filename = output_dir + "step" + str(number) + ".mp4"
    command = [FFMPEG_BIN,
               '-y',  # (optional) overwrite output file if it exists
               '-i', audio_filename,
               '-i', video_filename,
               '-acodec', 'copy',
               '-vcodec', 'h264',
               filename]
    sp.call(command, shell=True)


