# Termux-For-Youtube
A Youtube Video Downloader For Android using Termux App with youtube-dl plugins.  
**NOTE : _I'm just modified this Script to a more User-friendly interface._**

## How to Use It


* Download Termux and Termux API from Google Play Store.  
* Make Sure You Are Connected To Intenet.  
* Open Termux App and type this line of code  
```
apt update

apt install curl dos2unix -y

curl -fsSL https://raw.githubusercontent.com/SarfarazRLZ/Termux-For-Youtube/master/youtube_settings.sh -o youtube_settings.sh || {
  echo "Download failed"
  exit 1
}

chmod +x youtube_settings.sh
dos2unix youtube_settings.sh

./youtube_settings.sh

```
* After this, just share Youtube Videos to Termux App and press the Enter for the Best Quality Download.   


#### All Videos Save to Internal-Storage/Youtube Folder
