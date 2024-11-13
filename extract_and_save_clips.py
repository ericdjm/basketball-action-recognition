import cv2
import os

# Set paths to your folders
dataset_dir = 'dataset'
has_ball_dir = os.path.join(dataset_dir, 'has_ball')
no_ball_dir = os.path.join(dataset_dir, 'no_ball')
shot_taken_dir = os.path.join(dataset_dir, 'shot_taken')

# Ensure directories exist
os.makedirs(has_ball_dir, exist_ok=True)
os.makedirs(no_ball_dir, exist_ok=True)
os.makedirs(shot_taken_dir, exist_ok=True)

# Video processing function
def save_clip(frames, output_path, fps=30):
    height, width, _ = frames[0].shape
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()

# Function to process and add a clip
def add_clip(video_path, action_type, start_time, duration, clip_num):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    start_frame = int(start_time * fps)
    end_frame = start_frame + int(duration * fps)

    # Choose the correct folder based on action type
    if action_type == 'has_ball':
        output_dir = has_ball_dir
    elif action_type == 'no_ball':
        output_dir = no_ball_dir
    elif action_type == 'shot_taken':
        output_dir = shot_taken_dir
    else:
        print("Invalid action type!")
        return

    # Frame extraction
    frames = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    for i in range(start_frame, end_frame):
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    # Save the extracted clip
    output_filename = os.path.join(output_dir, f'clip_{clip_num:03d}.mp4')
    save_clip(frames, output_filename, fps)
    print(f"Saved {action_type} clip to {output_filename}")

    cap.release()

# Example usage
video_path = 'path/to/full_game_video.mp4'

# Add a 'has_ball' clip from 10 seconds to 15 seconds of the video
add_clip(video_path, action_type='has_ball', start_time=10, duration=5, clip_num=1)

# Add a 'shot_taken' clip from 20 seconds to 23 seconds of the video
add_clip(video_path, action_type='shot_taken', start_time=20, duration=3, clip_num=1)
