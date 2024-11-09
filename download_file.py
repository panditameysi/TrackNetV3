import gdown
import argparse


def download_file_from_google_drive(file_id):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output=None, quiet=False)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_id", type=str)
    file_id = parser.parse_args().file_id
    download_file_from_google_drive(file_id=file_id)