from checkpoint_merger import CheckpointMergerPipeline
import os
import torch

# Instantiate the pipeline with your custom class
pipe = CheckpointMergerPipeline()

# Specify the models you want to merge
model_paths = ["/home/gkirilov/Brand_new_PC/jenna_768/dreambooth_dreamshaper_6BakedVae_steps_2500_lr_4e-06_batch_1",
               "/home/gkirilov/models/cyberrealistic_v31",]

# Merge the models using your custom method
merged_pipe = pipe.merge(model_paths, interp = 'sigmoid', alpha = 0.5, force = True)

# Move the pipeline to GPU
merged_pipe.to('cuda')

# Save the model
merged_pipe.save_pretrained("/home/gkirilov/Checkpoint/jenna_768_cyberrealistic")