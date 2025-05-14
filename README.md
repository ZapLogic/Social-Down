# SocialDown

A simple, powerful downloader for Android (Termux) to grab videos and audio from YouTube and most social media platforms.

---

**Owner & Developer:** Abdul Qadeer (Owner & CEO at ZapLogic)
- GitHub: [@ZapLogic](https://github.com/ZapLogic)

---

## Features
- Download YouTube videos in your chosen quality (4k, 2k, 1080p, 720p, 480p, 360p, 240p, 144p)
- Download YouTube audio only (choose your preferred audio format)
- Download from other social media and video sites (Facebook, Instagram, Twitter/X, Reddit, etc.)
- Simple, interactive command-line interface
- No history, utilities, or update bloat—just fast, direct downloads

---

## Installation (Android/Termux)
1. **Install Termux**
   - Download the latest Termux APK from [here](https://github.com/termux/termux-app/releases)
2. **Update and install git**
   ```
   pkg update -y
   pkg install git -y
   ```
3. **Clone SocialDown**
   ```
   git clone https://github.com/ZapLogic/SocialDown.git
   cd SocialDown
   ```
4. **Install dependencies and set up**
   ```
   pkg install python aria2 ffmpeg -y
   pip install yt-dlp
   ```
5. **(Optional) Give storage permissions**
   - Run: `termux-setup-storage`
   - Allow storage access when prompted

---

## Usage
1. **Share a video or audio link to Termux** (from YouTube, social media, etc.)
2. **Or run directly in Termux:**
   ```
   python SocialDown.py "<your-link-here>"
   ```
3. **For YouTube links:**
   - You'll be prompted to select video quality (1-8) or audio only (a). If you skip, it defaults to 480p.
   - Optionally, choose to download subtitles.
4. **For other sites:**
   - The script will download the video/audio using the best available quality.

---

## Example
```
python SocialDown.py "https://www.youtube.com/watch?v=example"
```

---

## License
MIT License

---

© 2025 Abdul Qadeer / ZapLogic. All rights reserved.
