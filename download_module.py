import pathlib
import urllib
import os

class DataDownloader:
    """
    Class that takes in URL and downloads the data at said URL.
    url: URL of the data
    file_name: Vector of specific files to be downloaded from URL
    target_dir: Prespecificed directory to download data to
    """
    target_dir = "datasets/"

    # Overloaded constructor for two cases:
    # 1. Downloading specified file(s) from URL
    # 2. Downloading all files from URL
    def __init__(self, url, file_name=None):
        print("Ctor called")
        self.url = url
        if file_name is not None:
            if not isinstance(file_name, list):
                self.file_names = [file_name]
            else:
                self.file_names = file_name
        else:
            self.file_names = []
            for file in list(pathlib.path(url).iterdir()):
                self.file_names.append(os.path.basename(file))
    
    # Helper function to make directory
    def mkdir(self, path):
        # Make a directory
        path = os.path.join(self.target_dir, path)
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    # Downloads data
    def download(self):
        for file in self.file_names:
            path = os.path.join(self.mkdir(file), file)
            print(f"Downloading {file}... to {path}")
            print("Done!")