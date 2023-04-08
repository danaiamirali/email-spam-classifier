import pathlib
import urllib.request
import os
import tarfile

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
            for file in list(pathlib.Path(url).iterdir()):
                self.file_names.append(os.path.basename(file))

    def __str__(self):
        print("URL: ", self.url)
        print("File names: ", self.file_names)
    
    # Helper function to make local directory to store the data
    # Returns created path
    def mkdir(self, path):
        # Make a directory
        path = os.path.join(self.target_dir, path)
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    # Downloads data
    def download(self, keep_zip=False):
        for file in self.file_names:
            # Local Path to store the data
            file_dir = self.mkdir(file)
            file_path = os.path.join(file_dir, file)

            print(f"Downloading {file}... to {file_dir}")

            # Download the data
            urllib.request.urlretrieve(self.url + file, file_path)
            extension = file.split(".")[-1]
            print("Filetype: ", extension)

            tars = ["tar", "tgz", "bz2", "gz", "xz"]
            if extension == "zip":
                # TODO: Implement zip file extraction
                pass
            elif extension in tars:
                tarfile.open(file_path, 'r').extractall(path=file_dir)
                if not keep_zip:
                    os.remove(file_path)
            else:
                raise Exception(f"Filetype {extension} not supported")

            print("Done!")