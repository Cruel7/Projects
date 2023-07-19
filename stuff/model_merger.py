from checkpoint_merger import CheckpointMergerPipeline
import os
import argparse
from tqdm import tqdm
import torch

# Instantiate the pipeline with your custom class
pipe = CheckpointMergerPipeline()

# Set up argparse
parser = argparse.ArgumentParser(description='Model Merging Script')
parser.add_argument('--model_a', type=str, required=True, help='Path to the first model directory')
parser.add_argument('--model_b', type=str, required=True, help='Path to the second model directory')
parser.add_argument('--save_dir', type=str, required=True, help='Path to save the merged model')
args = parser.parse_args()

# Specify the models you want to merge
model_paths = [
    os.path.expanduser(args.model_a),
    os.path.expanduser(args.model_b),
]

# Merge the models using your custom method. Alpha signifies what % of the merged model will consist of model A and B
for _ in tqdm(range(len(model_paths)), desc='Merging models'):
    merged_pipe = pipe.merge(model_paths, interp='inv_sigmoid', alpha=0.5, force=True)

# Define the directory where the model will be saved
save_directory = os.path.expanduser(args.save_dir)

# Check and create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Move the pipeline to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
merged_pipe.to(device)

# Save the model
merged_pipe.save_pretrained(save_directory)
