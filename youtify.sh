#!/data/data/com.termux/files/usr/bin/bash

# Get the URL
URL=$1
echo "Opening URL"

# Cheks if its Youtube or Spotify URL and downloads it
if [[ $URL == *"open.spotify.com"* ]] ; then
  echo "Downloading Song"
  spotdl --song $URL
elif  [[ $URL == *"youtu.be"* || $URL == *"youtube.com"* ]]; then
  formatvar=0
  read -p $'What do you want to download \n(Select the number and press enter) \n 1) Video \n 2) Audio \n' formatvar
  if [[ $formatvar == 1 ]]; then
    echo 'Downloading Video'
    youtube-dl $URL
  elif [[ $formatvar == 2 ]]; then
      echo 'downloading Audio'
      youtube-dl -x --audio-format 'mp3' $URL
  else
    echo 'Default downloading Video'
    youtube-dl $URL
  fi

else
  echo "No downloader for this URL type"
fi

read -n 1 -s -p "Press any key to exit..."