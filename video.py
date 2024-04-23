import os
import shutil
from datetime import datetime

# This will move all files that do not already exit at the destination into the directory
# under a folder named with the number tandem and the date e.g 001-date

# Path to GoPro SD card
sd_card_path = "G:\DCIM"

# Path to the directory where you want to organize the videos
destination_base_path = r"C:\Users\jakeo\Desktop\Desktop\Videoes\tandems\Todays Tandems"

def organize_videos(sd_card_path, destination_base_path):
    # Find the next available folder number based on existing folders
    folder_counter = len(os.listdir(destination_base_path)) + 1

    print("Starting file processing...")

    for root, dirs, files in os.walk(sd_card_path):
        for filename in sorted(files):
            if filename.lower().endswith(".mp4"):
                file_path = os.path.join(root, filename)
                
                # Create a new folder
                folder_name = f"{folder_counter:03d} - {datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')}"
                current_folder = os.path.join(destination_base_path, folder_name)
                os.makedirs(current_folder, exist_ok=True)

                # Create an internal "videos" folder
                videos_folder = os.path.join(current_folder, "videos")
                os.makedirs(videos_folder, exist_ok=True)

                # Check if the file already exists in the destination folder or its subdirectories
                destination_file_path = os.path.join(destination_base_path, filename)
                if not os.path.exists(destination_file_path):
                    # Move the video file to the current folder's "videos" folder
                    destination_file_path = os.path.join(videos_folder, filename)
                    shutil.copy(file_path, destination_file_path)
                    print(f"Moved file: {filename} to folder: {videos_folder}")
                else:
                    print(f"File {filename} already exists in the destination directory. Skipping...")

    print("File processing finished.")

    # Open the destination folder
    os.startfile(destination_base_path)

# Call the function to organize the videos
organize_videos(sd_card_path, destination_base_path)

