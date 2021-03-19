import os
import tarfile
import urllib

PATH = "" 
URL = ""

def fetch_data(url = URL,path=PATH):
    os.makedirs(path,exist_ok=True)
    tgz_path = os.path.join(path,"dataset_name.tgz")
    urllib.request.urlretrieve(path,tgz_path)
    tgz_file = tarfile.open(tgz_path)
    tgz_file.extractall(path=path)
    tgz_file.close()
