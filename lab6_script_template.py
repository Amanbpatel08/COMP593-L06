import subprocess
import os
import requests
import hashlib

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    vlc_sha256 = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.sha256'
    resp_msg = requests.get(vlc_sha256)
    if resp_msg.status_code == requests.codes.ok:
        file_content = resp_msg.content
    return 

def download_installer():
    vlc_app = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64'
    resp_msg = requests.get(vlc_app)
    if resp_msg.status_code == requests.codes.ok:
        file_content = resp_msg.content
    return

def installer_ok(installer_data, expected_sha256):
    image_hash = hashlib.sha256(installer_data).hexdigest()
    print(image_hash)
    return

def save_installer(installer_data):

    return

def run_installer(installer_path):
    subprocess.run([installer_path, '/L=1033', '/S'])

    return
    
def delete_installer(installer_path):
    os.remove(installer_path)
    return

if __name__ == '__main__':
    main()