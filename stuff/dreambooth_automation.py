import os
import torch
import subprocess
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
from pytorch_lightning import seed_everything
from pathlib import Path
from PIL import Image
import time
from datetime import datetime

torch.cuda.set_per_process_memory_fraction(0.8)

# Check CUDA availability
if torch.cuda.is_available():
    device = torch.device('cuda')
    print('Total GPU Memory:', torch.cuda.get_device_properties(device).total_memory)
    print('Allocated GPU Memory:', torch.cuda.memory_allocated(device))
    print('Cached GPU Memory:', torch.cuda.memory_reserved(device))
else:
    print('CUDA is not available.')

torch.cuda.empty_cache()

log_dir = "/home/gkirilov/Brand_new_PC/Logs"


# Main training function
def train_model(max_train_steps, learning_rate, batch_size, unique_output_dir):
    vendor_script = os.path.expanduser("~/workspace/model-manager/vendor/train_dreambooth.py")
    accelerate_command = [
        "accelerate",
        "launch",
        vendor_script,
        "--enable_xformers_memory_efficient_attention",
        f"--pretrained_model_name_or_path={pretrained_model}",
        f"--instance_data_dir={instance_data_dir}",
        f"--output_dir={unique_output_dir}",
        f"--instance_prompt={instance_prompt}",
        f"--resolution={resolution}",
        f"--train_batch_size={batch_size}",
        f"--gradient_accumulation_steps={gradient_accumulation_steps}",
        f"--learning_rate={learning_rate}",
        f"--lr_scheduler={lr_scheduler}",
        f"--lr_warmup_steps={lr_warmup_steps}",
        f"--max_train_steps={max_train_steps}",
        f"--checkpointing_steps={checkpoint_steps}"
    ]

    process = subprocess.Popen(accelerate_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Error executing command:")
        print(stderr.decode())

    if torch.cuda.is_available():
        torch.cuda.empty_cache()

# Pass the training arguments
pretrained_model = "/home/gkirilov/models/cyberrealistic_v31"
output_dir = "/home/gkirilov/Brand_new_PC/automation_test/"
resolution = 512
batch_size_list = [1]
gradient_accumulation_steps = 1
learning_rate_list = [4e-6]
lr_scheduler = "constant"
lr_warmup_steps = 0
max_train_steps_list = [100]
checkpoint_steps = 10000

seed_everything(123)
torch.cuda.empty_cache()

# Base folder containing subfolders
base_folder = "/home/gkirilov/Checkpoint/For_Dreambooth_Tests"

# Get all subfolders in the base_folder
subfolders = [f.name for f in os.scandir(base_folder) if f.is_dir()]

# Loop over each subfolder
for subfolder in subfolders:
    # Full path to subfolder
    instance_data_dir = os.path.join(base_folder, subfolder)

    # Check if the directory is empty
    if not os.listdir(instance_data_dir):
        print(f"The directory {instance_data_dir} is empty. Skipping...")
        continue

    instance_prompt = f"__{subfolder}__"

    for lr in learning_rate_list:
        for steps in max_train_steps_list:
            for batch_size in batch_size_list:
                # unique output directory for each run
                unique_output_dir = f"{output_dir}_{subfolder}_{Path(pretrained_model).stem}_steps_{steps}_lr_{lr}_batch_{batch_size}"

                start_time = time.time()
                train_model(steps, lr, batch_size, unique_output_dir)
                end_time = time.time()
                training_time = end_time - start_time
                print("Time for training with max_train_steps =", steps, ", learning_rate =", lr, ", batch_size =",
                      batch_size, ":", training_time, "seconds")

                with open(f"{log_dir}/automation.txt", "a") as log_file:
                    log_file.write(
                        f"Model: {unique_output_dir}, Time for training with max_train_steps = {steps}, learning_rate = {lr}, batch_size = {batch_size}: {training_time} seconds\n")

torch.cuda.empty_cache()


