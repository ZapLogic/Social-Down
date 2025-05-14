# SocialDown v1.0

import os
import sys
import json
from datetime import date

# JSON file for settings (resolution, codec)
json_path = "/data/data/com.termux/files/home/default.json"

if not os.path.isfile(json_path):
    jsonnew = {
        "default": [
            {"code": "", "codec": ""}
        ],
        "1": [{"height": "2160", "res": "4k"}],
        "2": [{"height": "1440", "res": "2k"}],
        "3": [{"height": "1080", "res": "1080p"}],
        "4": [{"height": "720", "res": "720p"}],
        "5": [{"height": "480", "res": "480p"}],
        "6": [{"height": "360", "res": "360p"}],
        "7": [{"height": "240", "res": "240p"}],
        "8": [{"height": "144", "res": "144p"}]
    }
    with open(json_path, "w") as out:
        out.write(json.dumps(jsonnew, indent=4))

# Dependency check
try:
    import ffmpeg
except ModuleNotFoundError:
    os.system('pip install ffmpeg')
try:
    import yt_dlp
except ModuleNotFoundError:
    os.system('pip install --no-deps -U yt_dlp')

# Get link from command line
link = sys.argv[1]

genPath = "/storage/emulated/0/"

def downloader(opt):
    import yt_dlp
    with yt_dlp.YoutubeDL(opt) as yt:
        yt.extract_info(link, download=True)

def youtube_flow():
    # Step 1: Ask for quality or audio
    print("Select download option:")
    print("1 - 4k\n2 - 2k\n3 - 1080p\n4 - 720p\n5 - 480p (default)\n6 - 360p\n7 - 240p\n8 - 144p\na - Audio only")
    choice = input("Enter code (1-8) for video quality or 'a' for audio (default 480p): ").strip()
    if choice == "a":
        audio_download()
        return
    if choice not in ["1","2","3","4","5","6","7","8"]:
        choice = "5"  # default 480p
    with open(json_path, "r") as f:
        data = json.load(f)
    j = data[choice][0]["height"]
    k = data[choice][0]["res"]
    if "playlist" in link:
        path = genPath+'SocialDown/Youtube/%(playlist)s/%(title)s.%(ext)s'
    else:
        path = genPath+'SocialDown/Youtube/%(title)s.%(ext)s'
    sub = input("Download subtitle? (y/n): ").lower() == "y"
    opt = {
        'external_downloader': 'aria2c',
        'outtmpl': path,
        'writesubtitles': sub,
        'writeautomaticsub': sub,
        'merge_output_format': 'mp4',
        'writethumbnail': True,
        'format': f'bestvideo[height<={j}]+bestaudio[ext=m4a]/best[height<={j}]/best[ext=m4a]',
        'postprocessors': [
            {'key': 'FFmpegEmbedSubtitle', 'already_have_subtitle': False},
            {'key': 'FFmpegMetadata', 'add_metadata': True},
            {'key': 'EmbedThumbnail', 'already_have_thumbnail': False}
        ]
    }
    downloader(opt)

def audio_download():
    with open(json_path, "r") as f:
        data = json.load(f)
    codec = data["default"][0]["codec"]
    if not codec:
        codec = input('Enter audio format (mp3, aac, m4a, flac...): ').strip() or "mp3"
        data["default"][0]["codec"] = codec
        with open(json_path, "w") as f2:
            json.dump(data, f2)
    path = genPath+"SocialDown/Youtube/"
    if not os.path.isdir(path):
        os.makedirs(path)
    if "playlist" in link:
        op_path =  path + '/%(playlist)s/%(title)s.%(ext)s'
    else:
        op_path =  path + '%(title)s.%(ext)s'
    opt = {
        'format': 'bestaudio/best',
        'writethumbnail': True,
        'ignoreerrors': True,
        'outtmpl': op_path,
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': codec},
            {'key': 'FFmpegMetadata', 'add_metadata': True},
            {'key': 'EmbedThumbnail', 'already_have_thumbnail': False}
        ]
    }
    downloader(opt)

def others():
    if "www" in link:
        l1 = link.split("www.")
    else:
        l1 = link.split("://")
    l2 = l1[1].split(".")
    dir_name = l2[0].capitalize()
    path = genPath+'SocialDown/'+ dir_name +'/'
    if not os.path.isdir(path):
        os.makedirs(path)
    opt = {
        'outtmpl': path + "%(title).50s.%(ext)s",
        'external_downloader': 'aria2c',
        'writesubtitles': True,
        'writeautomaticsub': True,
    }
    try:
        downloader(opt)
    except:
        os.rmdir(path)

def main():
    if "youtube" in link or "youtu.be" in link:
        youtube_flow()
    else:
        others()

main()
