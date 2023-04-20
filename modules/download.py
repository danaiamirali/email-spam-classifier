import urllib.request
import os
import tarfile
import zipfile


class DataDownloader:
    """
    Class that takes in URL and downloads the data at said URL.
    url: URL of the data
    file_name: Vector of specific files to be downloaded from URL
    target_dir: Prespecificed directory to download data to
    """
    target_dir = "datasets/"
    
    def __init__(self, url, file_name=None):
        """
        constructor that handles initialization by taking in URL and file name(s)
        and fetching the file names from the URL if no file name is specified.
        url: string 
        file_name: string or vector of strings or None
        """
        print("Ctor called")
        self.url = url
        # Specified files
        if file_name is not None:
            if not isinstance(file_name, list):
                self.file_names = [file_name]
            else:
                self.file_names = file_name
        # All files
        else:
            self.file_names = self.file_names_from_url()
            

    def __str__(self):
        """
        object to string method for debugging or convenience purposes
        """
        print("URL: ", self.url)
        print("File names: ", self.file_names)

    def mkdir(self, path):
        """
        helper function to make local directory to store data
        returns created path
        path: string
        """
        # Make a directory
        path = os.path.join(self.target_dir, path)
        if not os.path.exists(path):
            os.mkdir(path)
        return path
    
    def file_names_from_url(self):
        """
        helper function to get file names from URL
        returns vector of file names
        """
        file_names = []
        with urllib.request.urlopen(self.url) as response:
            for line in response:
                decoded_line = line.decode("utf-8")
                if decoded_line.startswith("<a href="):
                    file_names.append(decoded_line.split('"')[1])
        return file_names

    def download(self, keep_zip=False):
        """
        downloads data from URL to local directory
        keeps zip files or deletes based on user specification
        keep_zip: boolean
        """
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
                with zipfile.ZipFile(file_path, 'r') as myzip:
                    zipfile.ZipFile.extractall(myzip, path=file_dir)
                if not keep_zip:
                    os.remove(file_path)
            elif extension in tars:
                tarfile.open(file_path, 'r').extractall(path=file_dir)
                if not keep_zip:
                    os.remove(file_path)
            else:
                raise Exception(f"Filetype {extension} not supported")

            print("Done!")