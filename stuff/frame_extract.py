import os
import cv2
import torch
import argparse
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F


def extract_frames(video_path, output_folder, skip_frames=10):
    # Load pre-trained model for object detection
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    if torch.cuda.is_available():
        model = model.cuda()

    # Get the video name (without extension)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Open the video file
    vidcap = cv2.VideoCapture(video_path)

    success, image = vidcap.read()
    count = 0
    save_count = 0
    while success:
        # Save frame as JPG file if a human is detected
        if count % skip_frames == 0:  # If count is multiple of skip_frames
            image_tensor = F.to_tensor(image).unsqueeze(0)

            if torch.cuda.is_available():
                image_tensor = image_tensor.cuda()

            with torch.no_grad():
                prediction = model(image_tensor)

            # The category ID for "person" in COCO dataset is 1
            if any(label == 1 for label in prediction[0]['labels']):
                # Resize the image
                frame_filename = f"{output_folder}/{video_name}_frame{save_count}.jpg"
                cv2.imwrite(frame_filename, image)
                save_count += 1
        success, image = vidcap.read()
        print('Processed frame: ', count)
        count += 1


def main():
    parser = argparse.ArgumentParser(description='Extract frames from video.')
    parser.add_argument('--input_folder', type=str, help='Path to the input video.')
    parser.add_argument('--output_folder', type=str, help='Path to the output folder for frames.')
    parser.add_argument('--skip_frames', type=int, default=10, help='Number of frames to skip between saving.')

    args = parser.parse_args()

    extract_frames(args.input_folder, args.output_folder, args.skip_frames)


if __name__ == "__main__":
    main()
