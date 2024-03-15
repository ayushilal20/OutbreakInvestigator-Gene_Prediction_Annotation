import os
import shutil
import gzip

folder_path = "/home/alal61/filtered_skesa_asm/"
bakta_db_path = "/home/alal61/bakta/db/"


# Get a list of all folders in the specified directory
folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

for folder in folders:
    if folder.startswith("F") and folder[1:].isdigit():

        # Construct the full path to the folder
        folder_full_path = os.path.join(folder_path, folder)

        # Get a list of all files in the folder
        files = [f for f in os.listdir(folder_full_path) if os.path.isfile(os.path.join(folder_full_path, f))]

        for file in files:
            if file.endswith(".fa"):

                # Construct the full path to the input file
                input_file_full_path = os.path.join(folder_full_path, file)

                # Specify the output file name with ".gz" extension and folder name
                output_file = os.path.join(folder_full_path, f"{folder}_{file}.gz")

                # Open the input file, compress it, and write to the output file
                with open(input_file_full_path, 'rb') as input_file, gzip.open(output_file, 'wb') as gzipped_file:
                    gzipped_file.writelines(input_file)

                print(f"Compressed {input_file_full_path} to {output_file} and kept original as {input_file_full_path}.original")
