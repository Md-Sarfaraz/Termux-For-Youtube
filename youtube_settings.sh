#!/data/data/com.termux/files/usr/bin/bash

echo -e "Updating default packages\n"
apt update && apt -y upgrade
echo -e "Installing Required Tools"
apt install termux-api figlet nano python ffmpeg -y

echo -e "Requesting access to storage\n"
termux-setup-storage
sleep 5

echo -e "Installing youtube-dl\n"
yes | pip install youtube-dl

echo -e "Creating the Youtube folder to download the files\n"
mkdir ~/storage/shared/youtube

echo -e "Creating youtube-dl folder for config\n"
mkdir -p ~/.config/youtube-dl

echo -e "Creating bin folder\n"
mkdir ~/bin
 
echo -e "Downloading and installing termux-url-opener\n"
curl http://pastebin.com/raw/PQN5iJqi -O ~/bin/termux-url-opener
sleep 1
dos2unix ~/bin/termux-url-opener

echo -e "\n"
echo -e "Modified by :  \n"
figlet RAJ