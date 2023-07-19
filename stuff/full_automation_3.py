import argparse
import os
import torch
import subprocess
import shutil
from pytorch_lightning import seed_everything
from pathlib import Path
import time
from infer_models_2 import infer_models
import automation_grid_2
import warnings
import glob

warnings.filterwarnings("ignore")

if torch.cuda.is_available():
    torch.cuda.set_per_process_memory_fraction(0.8)
    device = torch.device('cuda')
    print('Total GPU Memory:', torch.cuda.get_device_properties(device).total_memory)
    print('Allocated GPU Memory:', torch.cuda.memory_allocated(device))
    print('Cached GPU Memory:', torch.cuda.memory_reserved(device))
else:
    print('CUDA is not available.')

torch.cuda.empty_cache()


def train_model(max_train_steps, learning_rate, batch_size, unique_output_dir, pretrained_model, instance_data_dir, instance_prompt, resolution, gradient_accumulation_steps, lr_scheduler, lr_warmup_steps, checkpoint_steps, log_dir):
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

    start_time = time.time()

    process = subprocess.Popen(accelerate_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    end_time = time.time()
    training_time = end_time - start_time

    if process.returncode == 0:
        print("Command executed successfully. Starting training")
    else:
        print("Error executing command:")
        print(stderr.decode())

    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    print("Time for training with max_train_steps =", max_train_steps, ", learning_rate =", learning_rate, ", batch_size =", batch_size, ":", training_time, "seconds")

    with open(f"{log_dir}/automation.txt", "a") as log_file:
        log_file.write(f"Model: {unique_output_dir}, Time for training with max_train_steps = {max_train_steps}, learning_rate = {learning_rate}, batch_size = {batch_size}: {training_time} seconds\n")


def main(pretrained_model, output_dir, base_folder, log_dir, grid_dir, output_base_dir, main_dir):
    resolution = 512
    batch_size_list = [1]
    gradient_accumulation_steps = 1
    learning_rate_list = [4e-6]
    lr_scheduler = "constant"
    lr_warmup_steps = 0
    max_train_steps_list = [1]
    checkpoint_steps = 10000

    seed_everything(123)
    torch.cuda.empty_cache()

    subfolders = [f.name for f in os.scandir(base_folder) if f.is_dir()]

    for subfolder in subfolders:
        instance_data_dir = os.path.join(base_folder, subfolder)

        if not os.listdir(instance_data_dir):
            print(f"The directory {instance_data_dir} is empty. Skipping...")
            continue

        instance_prompt = f"__{subfolder}__"

        for lr in learning_rate_list:
            for steps in max_train_steps_list:
                for batch_size in batch_size_list:
                    unique_output_dir = f"{output_dir}_{subfolder}_{Path(pretrained_model).stem}_steps_{steps}_lr_{lr}_batch_{batch_size}"
                    train_model(steps, lr, batch_size, unique_output_dir, pretrained_model, instance_data_dir, instance_prompt, resolution, gradient_accumulation_steps, lr_scheduler, lr_warmup_steps, checkpoint_steps, log_dir)

    torch.cuda.empty_cache()

    base_dir = output_dir
    subdirs = [os.path.join(base_dir, name) for name in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, name))]

    for sub_dir in glob.glob(os.path.join(main_dir, '*')):
        infer_models(sub_dir, output_base_dir)

    automation_grid_2.main(directory="/home/gkirilov/Checkpoint/output_folder")

    image_grids_dir = os.path.join(grid_dir, "image_grids")
    os.makedirs(image_grids_dir, exist_ok=True)

    for root, dirs, files in os.walk(grid_dir):
        for file in files:
            if "grid" in file and file.endswith((".jpg", ".png")):
                file_path = os.path.join(root, file)
                new_filename = f"{int(time.time())}_{file}"
                dest_path = os.path.join(image_grids_dir, new_filename)
                shutil.move(file_path, dest_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretrained_model", type=str, required=True, help="Directory of the pretrained model")
    parser.add_argument("--output_dir", type=str, required=True, help="Output directory for the training")
    parser.add_argument("--base_folder", type=str, required=True, help="Base directory containing subfolders for training")
    parser.add_argument("--log_dir", type=str, required=True, help="Directory for logs")
    parser.add_argument("--grid_dir", type=str, required=True, help="Directory for grid output")
    parser.add_argument("--output_base_dir", type=str, required=True, help="Base directory for output")
    parser.add_argument("--main_dir", type=str, required=True, help="Main directory path")

    args = parser.parse_args()
    main(args.pretrained_model, args.output_dir, args.base_folder, args.log_dir, args.grid_dir, args.output_base_dir, args.main_dir)

    automation_grid_2.main(args.output_base_dir)
