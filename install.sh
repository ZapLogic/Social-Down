#!/bin/bash

# Move main script to home directory and rename
cp "SocialDown.py" "/data/data/com.termux/files/home/SocialDown.py"

# (Optional) Move termux-url-opener if you want share-to-termux integration
if [ -f "termux-url-opener" ]; then
    cp "termux-url-opener" "/data/data/com.termux/files/home/termux-url-opener"
    chmod +x "/data/data/com.termux/files/home/termux-url-opener"
fi

# Storage permission
termux-setup-storage

# Install dependencies
pkg update -y
pkg install python aria2 ffmpeg -y
pip install yt-dlp

# Installation complete
clear
echo "SocialDown installation complete!"
echo "Run: python SocialDown.py <link>"
