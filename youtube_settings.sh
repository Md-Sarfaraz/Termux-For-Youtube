#!/data/data/com.termux/files/usr/bin/bash

echo "Updating default packages\n"
apt update && apt -y upgrade
echo -e "Installing Required Tools"
apt install termux-api figlet python ffmpeg -y

echo "Requesting access to storage\n"
termux-setup-storage
sleep 5

echo "Installing Dependencies\n"
yes | pip install youtube-dl

echo "Creating the Youtube folder to download the files\n"
mkdir ~/storage/shared/youtube

echo "Creating youtube-dl folder for config\n"
mkdir -p ~/.config/youtube-dl

echo "Creating bin folder\n"
mkdir ~/bin
 
echo "Downloading and installing termux-url-opener\n"
curl https://raw.githubusercontent.com/SarfarazRLZ/Termux-For-Youtube/master/termux-url-opener -o ~/bin/termux-url-opener
sleep 1
dos2unix ~/bin/termux-url-opener

echo "\n"
echo "Modified by :  \n"
figlet RAJ
