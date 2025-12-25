#!/data/data/com.termux/files/usr/bin/bash

echo "[+] Updating packages"
apt update && apt -y upgrade

echo "[+] Installing required packages"
apt install -y python ffmpeg figlet termux-api aria2

echo "[+] Installing yt-dlp"
pip install -U yt-dlp

echo "[+] Requesting storage access"
termux-setup-storage
sleep 5

echo "[+] Creating directories"
mkdir -p ~/bin
mkdir -p ~/storage/shared/Youtube
mkdir -p ~/.config/yt-dlp
mkdir -p ~/.ytdlp

echo "[+] Creating yt-dlp config (aria2 + retry + resume)"
cat > ~/.config/yt-dlp/config <<EOF
--no-warnings
--newline
--continue
--retries infinite
--fragment-retries infinite
--external-downloader aria2c
--external-downloader-args "-c -j 8 -x 8 -s 8 -k 1M --file-allocation=trunc --retry-wait=5 --max-tries=0"
-o /data/data/com.termux/files/home/storage/shared/Youtube/%(title)s.%(ext)s
EOF

echo "[+] Downloading termux-url-opener"
curl -fsSL https://raw.githubusercontent.com/YOUR_REPO/termux-url-opener -o ~/bin/termux-url-opener
chmod +x ~/bin/termux-url-opener

echo "[+] Setup complete"
figlet RAJ
