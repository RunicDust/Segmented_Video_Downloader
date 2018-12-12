import os
import subprocess as sp
from defines import FFMPEG_BIN, output_dir, input_dir

def compress(input_video, output_video):
    sp.check_call(
        [FFMPEG_BIN, '-v', '-8', '-i', input_video, '-vf', 'scale=-2:720', '-preset', 'slow',
         '-c:v', 'libx264', '-strict', 'experimental', '-c:a', 'aac', '-crf', '20', '-maxrate', '800k',
         '-bufsize', '800k', '-r', '25', '-f', 'mp4', output_video, '-y'])


def compress_all_video_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            new_filename = output_dir +"compressed/" + filename
            compress(directory + filename, new_filename)
            print(new_filename)
            continue
        else:
            continue

compress_all_video_in_directory(input_dir)
