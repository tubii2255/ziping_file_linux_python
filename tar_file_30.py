import os
import subprocess
import datetime
import sys

def create_tar_file_name(directory, extension):
    current_date = datetime.datetime.now().strftime("%d_%m_%Y")
    base_name = os.path.basename(directory)
    return f"{base_name}_{current_date}{extension}.tar"

def tar_files_with_extension(directory, extension, destination_folder):
    tar_file_name = create_tar_file_name(directory, extension)
    tar_path = os.path.join(destination_folder, tar_file_name)
    tar_command = ['tar', '-cf', tar_path]

    os.chdir(directory)  # Change the working directory to the given directory

    files_to_tar = [file for file in os.listdir('.') if file.endswith(extension)]
    tar_command.extend(files_to_tar)

    subprocess.call(tar_command)

    for file in files_to_tar:
        os.remove(file)

def main():
    if len(sys.argv) < 3:
        print("Usage: <script> <directory_path> <extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    extension = sys.argv[2]
    destination_folder = '/home/kali/Desktop/testing/move'

    tar_files_with_extension(directory_path, extension, destination_folder)

if __name__ == "__main__":
    main()
