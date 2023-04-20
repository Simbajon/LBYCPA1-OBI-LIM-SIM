import os
import shutil

def organize_files(directory_path):
   
    files = os.listdir(directory_path)


    # Get all the files in the desired directory
   
   
    file_types = {
        "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp"],
        "Videos": [".avi", ".mp4", ".wmv", ".mov", ".flv"],
        "Documents": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".vsdx", ".xlsx", ".pptx", ".jar"],
        "Audio": [".mp3", ".wav", ".wma", ".aac", ".flac"],
        "Code": [".ipynb", ".py", ".java", ".cpp", ".c", ".h", ".js", ".html", ".css"],
        "Compressed": [".zip", ".rar", ".gz", ".tar", ".7z"],
        "Executables": [".exe", ".msi"]
    }
   
    # Create a dictionary to hold the file types and their corresponding file extensions
   
    for folder_name in file_types:
        folder_path = os.path.join(directory_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
           
    # Create folders for each file type
   
    for file in files:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    folder_path = os.path.join(directory_path, folder_name)
                    shutil.move(file_path, folder_path)
                    break
                   
    # Move files to their appropriate folders

current_dir = os.path.dirname(os.path.abspath(__file__))
organize_files(current_dir)

