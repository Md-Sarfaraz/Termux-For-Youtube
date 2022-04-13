#!/data/data/com.termux/files/usr/bin/bash

echo "Updating default packages"
apt update && apt -y upgrade
echo "Installing Required Tools"
apt install termux-api python ffmpeg -y

echo "Requesting access to storage"
termux-setup-storage
sleep 5

echo "Installing Dependencies"
yes | pip install yt_dlp

echo "Creating the Youtube folder to download the files"
mkdir ~/storage/shared/youtube

echo "Creating bin folder"
mkdir ~/bin
mkdir ~/bin/.tmp
 
echo "Installing files..."
cp -r youtube ~/bin/youtube
cp -r termux-url-opener ~/bin/

sleep 2
dos2unix ~/bin/termux-url-opener
chmod u+x  ~/bin/termux-url-opener
chmod u+x  ~/bin/youtube/*

echo ""
echo "Created by : Sarfaraz"
