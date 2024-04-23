import os

# Path to GoPro SD card
sd_card_path = "G:\DCIM"

def delete_files(directory):
    # Iterate over all items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # Check if the item is a file
        if os.path.isfile(item_path):
            try:
                # Delete the file
                os.remove(item_path)
                print(f"Deleted file: {item_path}")
            except Exception as e:
                print(f"Error deleting file: {item_path} - {e}")

# Call the function to delete files
delete_files(sd_card_path)
