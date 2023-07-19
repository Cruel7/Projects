import os
import argparse
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image
import json
from termcolor import colored

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--images_folder", required=True, help="Path to folder containing images")

# Parse the arguments
args = parser.parse_args()

# Load model and tokenizer
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}


def predict_step(image_paths):
    captions = []
    for image_path in image_paths:
        i_image = Image.open(image_path)
        if i_image.mode != "RGB":
            i_image = i_image.convert(mode="RGB")

        pixel_values = feature_extractor(images=[i_image], return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device)

        output_ids = model.generate(pixel_values, **gen_kwargs)

        preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        caption = preds[0].strip()
        captions.append(caption)

    return captions


root_image_folder = args.images_folder  # Now root_image_folder is the same as images_folder

# Create a new storage folder for generated prompts
current_folder = os.getcwd()
storage_folder = os.path.join(current_folder, "../storage/dreambooth_automation")
os.makedirs(storage_folder, exist_ok=True)
generated_prompts_folder = os.path.join(storage_folder, "generated_prompts/")
os.makedirs(generated_prompts_folder, exist_ok=True)

# Traverse through the subdirectories
for subdir, dirs, files in os.walk(root_image_folder):
    # Select only image files in the current directory
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg", ".png"))]

    # Construct their full paths
    image_paths = [os.path.join(subdir, filename) for filename in image_files]

    # If there are no image files in the current directory, skip
    if not image_paths:
        continue

    generated_captions = predict_step(image_paths)

    # Create a json file with the name of the current directory
    json_filename = os.path.basename(subdir) + ".json"
    file_path = os.path.join(generated_prompts_folder, json_filename)

    # Open the JSON file in write mode
    with open(file_path, "w") as json_file:
        data_list = []
        for caption, image_path in zip(generated_captions, image_paths):
            # Define file_name as relative path from root_image_folder
            file_name = os.path.relpath(image_path, root_image_folder)

            image_obj = {
                "file_name": file_name,
                "text": caption
            }
            data_list.append(image_obj)

        json_file.write(json.dumps(data_list, indent=4))  # Write all data at once

print(colored("Image data and captions converted and saved to JSON file successfully.", "green"))
