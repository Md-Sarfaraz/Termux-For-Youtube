#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "Updating Termux packages..."
pkg update -y && pkg upgrade -y

echo "Installing required packages..."
pkg install -y \
  termux-api \
  figlet \
  python \
  ffmpeg \
  yt-dlp \
  curl \
  dos2unix

echo "Requesting storage permission..."
termux-setup-storage
sleep 3

if [ ! -d "$HOME/storage/shared" ]; then
  echo "Storage permission not granted. Exiting."
  exit 1
fi

echo "Creating download directory..."
mkdir -p "$HOME/storage/shared/Youtube"

echo "Creating bin directory..."
mkdir -p "$HOME/bin"

if ! grep -q 'export PATH=$HOME/bin:$PATH' "$HOME/.bashrc" 2>/dev/null; then
  echo 'export PATH=$HOME/bin:$PATH' >> "$HOME/.bashrc"
fi

echo "Installing termux-url-opener..."
curl -fsSL \
  https://raw.githubusercontent.com/SarfarazRLZ/Termux-For-Youtube/master/termux-url-opener \
  -o "$HOME/bin/termux-url-opener"

dos2unix "$HOME/bin/termux-url-opener"
chmod +x "$HOME/bin/termux-url-opener"

echo ""
echo "Setup completed successfully."
echo "Modified by:"
figlet RAJ

echo ""
echo "Please restart Termux or run: source ~/.bashrc"
