import os
import time

def download_wait(file_path, duration = 60):
    start = time.time()
    while not os.path.exists(file_path):
        if time.time() - start > duration:
            raise TimeoutError(f'Download timeout: {file_path}')
        time.sleep(1)