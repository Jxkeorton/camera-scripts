import os
import shutil
import subprocess
from datetime import datetime
from moviepy.editor import VideoFileClip

# Made for an SD card with multiple skydives
# This script will create a seperate folder per skydive you have done. 
# You must record a >3second video between each skydive you do.
# It creates a folder for each skydive with the relevant videoes.

# It will copy the files from the SD card

# Path to your GoPro SD card
sd_card_path = "G:\DCIM"

# Path to the directory where you want to organize the videos
destination_base_path = r"C:\Users\jakeo\Desktop\Desktop\Videoes\tandems\Todays Tandems"

def get_video_length(file_path):
    clip = VideoFileClip(file_path)
    clip.close()
    return clip.duration

def organize_videos(sd_card_path, destination_base_path):
    # Iterate through each file in the SD card and its subdirectories
    video_length_threshold = 3  # Minimum video length in seconds
    folder_counter = 1
    print("Starting file processing...")

    for root, dirs, files in os.walk(sd_card_path):
        for filename in sorted(files):
            if filename.lower().endswith(".mp4"): 
                file_path = os.path.join(root, filename)
                # Get the length of the video
                video_length = get_video_length(file_path)
                if video_length < video_length_threshold:
                    # Create a new folder
                    folder_name = f"{folder_counter:03d} - {datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')}"
                    current_folder = os.path.join(destination_base_path, folder_name)
                    os.makedirs(current_folder, exist_ok=True)
                    # Create an internal "videos" folder
                    videos_folder = os.path.join(current_folder, "videos")
                    os.makedirs(videos_folder, exist_ok=True)
                    print(f"Created new folder: {folder_name}")
                    folder_counter += 1
                else:
                    # Move the video file to the current folder's "videos" folder
                    videos_folder = os.path.join(destination_base_path, f"{folder_counter-1:03d} - {datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')}", "videos")
                    os.makedirs(videos_folder, exist_ok=True)  # Create videos folder if it doesn't exist
                    
                    # Check if the file already exists in the destination folder
                    destination_file_path = os.path.join(videos_folder, filename)
                    if not os.path.exists(destination_file_path):
                        try:
                            shutil.copy(file_path, destination_file_path)
                            print(f"Moved file: {filename} to folder: {videos_folder}")
                        except PermissionError as e:
                            print(f"PermissionError: {e}. Skipping file: {filename}")
                        print(f"Moved file: {filename}")
                    else:
                        print(f"File {filename} already exists in the destination directory. Skipping...")

    print("File processing finished.")

    # Open Premiere Pro desktop app
    subprocess.Popen(["C:\Program Files\Adobe\Adobe Premiere Pro 2024\Adobe Premiere Pro.exe"])

    # Open the destination folder
    os.startfile(destination_base_path)

# Call the function to organize the videos
organize_videos(sd_card_path, destination_base_path)

