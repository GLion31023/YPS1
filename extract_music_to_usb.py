import os
import shutil
from dotenv import load_dotenv

load_dotenv()

source_dir = os.getenv('SOURCE_DIR')
destination_dir = os.getenv('DESTINATION_DIR')

if not source_dir or not destination_dir:
    raise ValueError("Source or destination directory is not set. Please check your .env file.")

os.makedirs(destination_dir, exist_ok=True)

for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(('.mp3', '.m4p')):
            file_path = os.path.join(root, file)
            shutil.copy(file_path, destination_dir)
            print(f'Copied: {file_path} to {destination_dir}')

print('File extraction and copying completed.')
