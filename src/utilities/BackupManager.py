import os
import shutil
import tempfile
import datetime

class BackupManager:
    @staticmethod
    def backup_old_links_files():
        try:
            dir_list = os.listdir(os.getcwd())
            old_links_files = [file for file in dir_list if "google_maps_links" in file and file.endswith(".txt")]
            backup_folder = "data/links"
            if not os.path.exists(backup_folder):
                os.makedirs(backup_folder)

            for file in old_links_files:
                source_path = os.path.join(os.getcwd(), file)
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_file = os.path.join(temp_dir, file)
                    shutil.copy(source_path, temp_file)
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    new_file = "links_" + current_time + ".txt"
                    destination_path = os.path.join(os.getcwd(), backup_folder, new_file)
                    shutil.move(temp_file, destination_path)
                os.remove(source_path)

            if old_links_files:
                print("Successfully backed up last session.")
            else:
                print("No previous session found, continuing without backup.\n")
        except Exception:
            print("No previous session found, continuing without backup.\n")
