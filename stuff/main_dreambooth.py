# import os
#
#
# # Training script parameters
# train_script_name = "new_training_2.py"
# pretrained_model_path = "/home/gkirilov/models/cyberrealistic_v31"
# output_dir = "/home/gkirilov/Brand_new_PC/automation_test/dreambooth"
# log_dir_path = "/home/gkirilov/Brand_new_PC/Logs/"
# max_train_steps_list = [1]
# max_train_steps_str = ' '.join(map(str, max_train_steps_list))
#
#
# # Inference script parameters
# infer_script_name = "inference.py"
# output_base_dir = "/home/gkirilov/Checkpoint/output_folder_2"
# models_dir = "/home/gkirilov/Brand_new_PC/automation_test"
#
# # Image grid parameters
# grid_script_name= "dreambooth_image_grid.py"
# output_folder_path= output_base_dir
#
#
# # Call the training script with the paths
# os.system(f"python {train_script_name} --pretrained_model_path {pretrained_model_path} --output_dir {output_dir} --max_train_steps_list {max_train_steps_str} --log_dir {log_dir_path}")
#
# # Call the inference script with the paths
# os.system(f"python {infer_script_name} --models_dir {models_dir} --output_base_dir {output_base_dir}")
#
# # Call the inference script with the paths
# os.system(f"python {grid_script_name} --output_folder {output_folder_path}")
#


import os

# Training script parameters
train_script_name = "new_training_2.py"
pretrained_model_path = "/home/gkirilov/models/cyberrealistic_v31"  # path to cached model
output_dir = "/home/gkirilov/Brand_new_PC/automation_test_2/dreambooth"  # path to where you want the models to be saved
log_dir_path = "/home/gkirilov/Brand_new_PC/Logs/"  # path to logging directory
base_folder = "/home/gkirilov/Checkpoint/For_Dreambooth_Tests"  # path to folder containing subfolders of images
resolution = 512
batch_size_list = [1]
max_train_steps_list = [1]  # specify the number of training steps
batch_size_list_str = ' '.join(map(str, batch_size_list))
max_train_steps_str = ' '.join(map(str, max_train_steps_list))

# Inference script parameters
infer_script_name = "inference.py"
output_base_dir = "/home/gkirilov/Checkpoint/output_folder_2"
models_dir = "/home/gkirilov/Brand_new_PC/automation_test_2"

# Image grid parameters
grid_script_name = "dreambooth_image_grid.py"
output_folder_path = output_base_dir

# Call the training script with the paths
os.system(f"python {train_script_name}"
          f" --pretrained_model_path {pretrained_model_path}"
          f" --output_dir {output_dir}"
          f" --max_train_steps_list {max_train_steps_str}"
          f" --log_dir {log_dir_path}"
          f" --resolution {resolution}"
          f" --batch_size_list {batch_size_list_str}"
          f" --base_folder {base_folder}")

# Call the inference script with the paths
os.system(f"python {infer_script_name}"
          f" --models_dir {models_dir}"
          f" --output_base_dir {output_base_dir}")

# Call the image grid script with the paths
os.system(f"python {grid_script_name}"
          f" --output_folder {output_folder_path}")


# Delete the instance_prompt.txt file
if os.path.exists('instance_prompt.txt'):
    os.remove('instance_prompt.txt')
else:
    print("The file does not exist")