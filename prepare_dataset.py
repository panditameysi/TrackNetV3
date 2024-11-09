import os
import shutil
import subprocess
import random

# Paths for videos and CSVs
video_folder = 'video'
csv_folder = 'csv'
output_folder = 'TrackNetV2_Dataset'

# Create the output dataset folder if not exists
os.makedirs(output_folder, exist_ok=True)

# divide videos into train,test,val in 6,2,2 ratio

train_folder = os.path.join(output_folder, 'train')
test_folder = os.path.join(output_folder, 'test')
val_folder = os.path.join(output_folder, 'val')

os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

files = os.listdir(video_folder)

random.shuffle(files)

train, test, val = files[:int(len(files)*0.6)], files[int(len(files)*0.6):int(len(files)*0.8)], files[int(len(files)*0.8):]

print(len(train),len(test),len(val))

print(train[0],test[0],val[0])



# Function to extract frames from video
def extract_frames(video_path, frames_folder):
    os.makedirs(frames_folder, exist_ok=True)
    # Construct the ffmpeg command
    ffmpeg_command = [
        'ffmpeg', '-i', video_path, '-q:v', '2', '-start_number', '0',
        os.path.join(frames_folder, '%d.png')
    ]
    subprocess.run(ffmpeg_command)

folders = [train_folder, test_folder, val_folder]

# # Iterate over all video files
clip = 1
for video_file in os.listdir(video_folder):
    if video_file.endswith('.mp4'):
        video_name = os.path.splitext(video_file)[0]
        video_path = os.path.join(video_folder, video_file)
        csv_path = os.path.join(csv_folder, f'{video_name}.csv')

        # Create folder for each video in the dataset
        type = "train"
        if video_file in test:
            type = "test"
        elif video_file in val:
            type = "val"
        video_output_folder = os.path.join(output_folder,type,"clip_"+str(clip)+"_"+video_name)
        os.makedirs(video_output_folder, exist_ok=True)

        # Create subfolders
        frames_folder = os.path.join(video_output_folder, 'frame', "clip_"+str(clip)+"_"+video_name)
        video_subfolder = os.path.join(video_output_folder, 'video')
        csv_subfolder = os.path.join(video_output_folder, 'csv')

        os.makedirs(video_subfolder, exist_ok=True)
        os.makedirs(csv_subfolder, exist_ok=True)

        # Extract frames and move video and CSV to appropriate folders
        extract_frames(video_path, frames_folder)
        destination_video = os.path.join(video_subfolder, "clip_"+str(clip)+"_"+video_name+".mp4")
        destination_csv = os.path.join(csv_subfolder,"clip_"+str(clip)+"_"+video_name+".csv")
        shutil.copy(video_path, destination_video)
        if os.path.exists(csv_path):
            shutil.copy(csv_path, destination_csv)

        clip += 1

print("Data preparation completed.")