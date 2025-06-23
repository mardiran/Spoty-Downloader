import os
import subprocess
import sys
from colorama import init, Fore, Style
import time

init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_stylized_title():
    title = """
  ___           _          ___                  _              _         
 / __|_ __  ___| |_ _  _  |   \ _____ __ ___ _ | |___  __ _ __| |___ _ _ 
 \__ \ '_ \/ _ \  _| || | | |) / _ \ V  V / ' \| / _ \/ _` / _` / -_) '_|
 |___/ .__/\___/\__|\_, | |___/\___/\_/\_/|_||_|_\___/\__,_\__,_\___|_|  
     |_|            |__/                                                                                                                                                
    """
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE]
    for i, line in enumerate(title.split('\n')):
        print(colors[i % len(colors)] + line + Style.RESET_ALL)
        time.sleep(0.1)
    print(Fore.CYAN + "         Created By mardiran" + Style.RESET_ALL)
    print(Fore.YELLOW + "="*40 + Style.RESET_ALL)
    time.sleep(0.5)

def is_ffmpeg_available():
    ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg.exe")
    return os.path.exists(ffmpeg_path)

def download_spotify_track(spotify_url):
    music_folder = os.path.join(os.getcwd(), "music")
    os.makedirs(music_folder, exist_ok=True)

    command = [
        sys.executable, "-m", "spotdl",
        spotify_url,
        "--output", os.path.join(music_folder, "{title}.{ext}")
    ]

    print(Fore.MAGENTA + "\n🚀 Initiating download process..." + Style.RESET_ALL)
    print(Fore.YELLOW + "📂 Saving to: " + music_folder + Style.RESET_ALL)
    print(Fore.CYAN + "⏳ Please wait..." + Style.RESET_ALL)

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while process.poll() is None:
            print(Fore.GREEN + "🔄 Downloading..." + Style.RESET_ALL, end="\r")
            time.sleep(0.5)
            print(Fore.YELLOW + "🔄 Downloading..." + Style.RESET_ALL, end="\r")
            time.sleep(0.5)
        print(" " * 50, end="\r")
        if process.returncode == 0:
            print(Fore.GREEN + "✅ Download complete! Saved to: " + music_folder + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Download failed. Check URL or spotdl installation." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"❌ Error: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    while True:
        clear_console()
        print_stylized_title()

        if not is_ffmpeg_available():
            print(Fore.RED + "❌ 'ffmpeg.exe' not found in current folder. Please place it next to this script." + Style.RESET_ALL)
            exit()

        spotify_link = input(Fore.BLUE + "🎵 Enter Spotify track/playlist/album URL: " + Style.RESET_ALL).strip()
        if not spotify_link:
            print(Fore.RED + "❌ No URL entered." + Style.RESET_ALL)
            exit()

        download_spotify_track(spotify_link)

        print(Fore.YELLOW + "\n📌 Want to download another track?" + Style.RESET_ALL)
        choice = input(Fore.BLUE + "➡️ Enter '1' to continue or any other key to exit: " + Style.RESET_ALL).strip()
        if choice != "1":
            print(Fore.CYAN + "👋 Exiting Spoty Downloader. Thanks for using!" + Style.RESET_ALL)
            break