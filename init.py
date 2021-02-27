import os

def FilePath(directory, filename):
    script_dir = os.getcwd()
    file_path = os.path.join(script_dir, directory, filename)
    return file_path
