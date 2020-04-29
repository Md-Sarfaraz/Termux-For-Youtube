#!/data/data/com.termux/files/usr/bin/bash

echo "Updating default packages"
apt update && apt -y upgrade
echo "Installing Required Tools"
apt install termux-api python ffmpeg -y

echo "Requesting access to storage"
termux-setup-storage
sleep 5

echo "Installing Dependencies"
yes | pip install youtube-dl

echo "Creating the Youtube folder to download the files"
mkdir ~/storage/shared/youtube

echo "Creating youtube-dl folder for config"
mkdir -p ~/.config/youtube-dl

echo "Creating bin folder"
mkdir ~/bin
 
echo "Downloading and installing termux-url-opener"
#curl https://raw.githubusercontent.com/SarfarazRLZ/Termux-For-Youtube/master/termux-url-opener -o ~/bin/termux-url-opener

cp -r youtube ~/bin/youtube
cp -r termux-url-opener ~/bin/

sleep 2
dos2unix ~/bin/termux-url-opener

echo ""
echo "Modified by : Sarfaraz"