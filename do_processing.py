from defines import file_with_urls
from src.video_downloader import download_segmented_video
from src.video_processor import merge_audio_with_video

number = 1

f = open(file_with_urls)

for master_json_url in f:
    print master_json_url
    master_json_url = str(master_json_url).strip()
    download_segmented_video(master_json_url)
    merge_audio_with_video("v.mp4", "a.mp3", number)
    number = number + 1



