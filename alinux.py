import os
import subprocess
import sys
import time
import datetime

def tar_files_with_extension(directory, extension, destination_folder):
    date_for_tar = datetime.datetime.now()
    final_date_for_tar = date_for_tar.strftime("%d_%m_%Y")

    tar_file_name = os.path.basename(directory) + '_' + final_date_for_tar + extension + '.tar'
    tar_path = os.path.join(destination_folder, tar_file_name)

    tar_command = ['tar', '-cf', tar_path]

    os.chdir(directory)  # Change the working directory to the given directory
    list_to_delete = []
    

    for file in os.listdir('.'):
    	
        file_path = os.path.join(directory, file)

        if file.endswith(extension):

        #if os.path.isfile(file_path) and file.endswith(extension) and (time.time() - os.path.getmtime(file_path)) > 30 * 24 * 60 * 60:
            tar_command.append(file)
            list_to_delete.append(file)

    subprocess.call(tar_command)
    for files in list_to_delete:
       os.remove(files)


if len(sys.argv) < 3:
    print("Please provide directory path and file extension as command-line arguments.")
    sys.exit(1)

directory_path = sys.argv[1]
extension = sys.argv[2]
destination_folder = '/home/kali/Desktop/testing/move'

tar_files_with_extension(directory_path, extension, destination_folder)
