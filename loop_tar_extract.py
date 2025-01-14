import tarfile
import os

def extractor(path):
    while True:
        with tarfile.open(path, "r") as tar:
            tar.extractall()
            os.remove(path)
            path = next((f for f in os.listdir() if f.endswith(".tar")), None)
            if not path:
                break

extractor("1000.tar")
            
            