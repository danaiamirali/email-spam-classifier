import pathlib
import os

class DataDownloader:
    """
    Class that takes in URL and downloads the data at said URL.
    """
    def __init__(self, url):
        self.url = url
        self.file_names = []
        for file in list(pathlib.path(url).iterdir()):
            self.file_names.append(os.path.basename(file))

    # Overloaded constructor for specific file name
    def __init__(self, url, file_name):
        self.url = url
        self.file_names = [file_name]

    def download(self):
        # Download the data
        pass

    def save(self):
        # Save the data
        pass