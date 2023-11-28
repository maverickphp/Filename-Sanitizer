import os
import sys
import re

def remove_spaces_and_brackets(file_dir):
    for path, dirs, files in os.walk(file_dir):
        existing_names = {}  # Keep track of existing filenames
        
        for filename in files:
            file_path = os.path.join(path, filename)
            new_filename = re.sub('[\s\(\)]', '', filename)
            
            counter = 1
            original_name = new_filename  # Store the original name without modifications
            
            while new_filename in existing_names:
                name, extension = os.path.splitext(original_name)
                new_filename = f"{name}_{counter}{extension}"
                counter += 1
            
            existing_names[new_filename] = True  # Store the modified filename
            
            if new_filename != filename:
                new_file_path = os.path.join(path, new_filename)
                
                while os.path.exists(new_file_path):
                    name, extension = os.path.splitext(new_filename)
                    new_filename = f"{name}_{counter}{extension}"
                    new_file_path = os.path.join(path, new_filename)
                    counter += 1
                
                os.rename(file_path, new_file_path)
                print(f"{file_path} renamed to {new_file_path}")
            else:
                print(f"{file_path} remains unchanged")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please supply the directory path as an argument.")
    else:
        directory = sys.argv[1]
        if os.path.exists(directory):
            remove_spaces_and_brackets(directory)
        else:
            print("The provided directory does not exist.")
