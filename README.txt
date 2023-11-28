# **Filename Sanitizer Script**

## **Description**
This Python script, named `FilenameSanitizer.py`, is designed to traverse through all files in a specified directory and its subdirectories, and rename each file by removing spaces and brackets. The script ensures that no file conflicts occur by appending an incrementing number if a proposed filename already exists.

## **Requirements**
- Python 3.x

## **Installation**
No additional installation is required, as the script uses standard Python libraries.

## **Usage**
1. Place `FilenameSanitizer.py` in a convenient location on your system.
2. Open your command line tool (Terminal, Command Prompt, etc.).
3. Navigate to the directory where `FilenameSanitizer.py` is located.
4. Run the script with the directory path as an argument:
   ```shell
   python FilenameSanitizer.py [path_to_directory]
