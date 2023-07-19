import subprocess
import os
import torch
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
from pytorch_lightning import seed_everything
from pathlib import Path
from PIL import Image
from train_dreambooth import parse_args
from train_dreambooth import DreamBoothDataset, tokenize_prompt

torch.cuda.set_per_process_memory_fraction(0.8)
import time
start_time = time.time()

# Specify the variables used to train dreambooth and lora models
pretrained_model="/media/gkirilov/Storage/huggingface/hub/models--SG161222--Realistic_Vision_V1.4/snapshots/6e02ccb36bd0d45ec803cd58cd61f7e7edaff39f"
instance_data_dir="/home/gkirilov/Brand_new_PC/images"
output_dir="/home/gkirilov/Brand_new_PC/dreambooth"
instance_prompt="a photo of JENNAORTEGAX"
resolution=512
batch_size=1
gradient_accumulation_steps=1
learning_rate=5e-6
lr_scheduler="constant"
lr_warmup_steps=0
max_train_steps=400
output_dir_lora="/home/gkirilov/Brand_new_PC/lora"
learning_rate_lora=1e-4
validation_prompt="JENNAORTEGAX in the park, black hair, dark eyes, wearing a red dress"
validation_epochs=50
seed="0"


def dreambooth_training():
    accelerate_command = [
        "accelerate",
        "launch",
        "train_dreambooth.py",
        f"--pretrained_model_name_or_path={pretrained_model}",  # Replace "model_name" with the actual model name
        f"--instance_data_dir={instance_data_dir}",  # Replace "instance_dir" with the actual instance data directory
        f"--output_dir={output_dir}",  # Replace "output_dir" with the actual output directory
        f"--instance_prompt={instance_prompt}",
        f"--resolution={resolution}",
        f"--train_batch_size={batch_size}",
        f"--gradient_accumulation_steps={gradient_accumulation_steps}",
        f"--learning_rate={learning_rate}",
        f"--lr_scheduler={lr_scheduler}",
        f"--lr_warmup_steps={lr_warmup_steps}",
        f"--max_train_steps={max_train_steps}"
    ]

    try:
        process = subprocess.Popen(accelerate_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Command executed successfully.")
        else:
            print("Error executing command:")
            print(stderr.decode())

    except Exception as e:
        print("An error occurred:")
        print(str(e))


seed_everything(123)

def lora_training():
    accelerate_command = [
        "accelerate",
        "launch",
        "train_dreambooth_lora.py",
        f"--pretrained_model_name_or_path={pretrained_model}",  # Replace "model_name" with the actual model name
        f"--instance_data_dir={instance_data_dir}",  # Replace "instance_dir" with the actual instance data directory
        f"--output_dir={output_dir_lora}",  # Replace "output_dir" with the actual output directory
        f"--instance_prompt={instance_prompt}",
        f"--resolution={resolution}",
        f"--train_batch_size={batch_size}",
        f"--gradient_accumulation_steps={gradient_accumulation_steps}",
        f"--learning_rate={learning_rate_lora}",
        f"--lr_scheduler={lr_scheduler}",
        f"--lr_warmup_steps={lr_warmup_steps}",
        f"--max_train_steps={max_train_steps}",
        f"--validation_prompt={validation_prompt}",
        f"--validation_epochs={validation_epochs}",
        f"--seed={seed}"
    ]

    try:
        process = subprocess.Popen(accelerate_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Command executed successfully.")
        else:
            print("Error executing command:")
            print(stderr.decode())

    except Exception as e:
        print("An error occurred:")
        print(str(e))


def test_models():
    models = {
        "RV1.4": {
            "path": "/home/gkirilov/Brand_new_PC/dreambooth",
            "active": True,
            "keyword": "JORTEGAXO"
        },
    }

    for model_name, model_info in models.items():
        if model_info["active"]:
            pipe = StableDiffusionPipeline.from_pretrained(model_info["path"], safety_checker=None,
                                                           torch_dtype=torch.float16)
            pipe = pipe.to("cuda")
            pipe_img2img = StableDiffusionImg2ImgPipeline.from_pretrained(model_info["path"], safety_checker=None,
                                                                          torch_dtype=torch.float16)
            pipe_img2img = pipe_img2img.to("cuda")

            print(f"Model {model_name} is on: {pipe.device}")
            print(f"Image-to-Image model {model_name} is on: {pipe_img2img.device}")

            pipe.enable_xformers_memory_efficient_attention()
            pipe_img2img.enable_xformers_memory_efficient_attention()

            for main_prompt in [
                "woman, solo, light blue hair, dark blue eyes, detailed face, ([Julianne Hough|Megan Fox|Christina Hendricks]:0.8), (puffy lips :0.9), masterpiece, professional, high quality, beautiful, amazing, gothic, Getty Images, miko, giant, photoshoot, 4k, realistic",
                "woman, solo, JENNAORTEGAX, light blue hair, dark blue eyes, detailed face, ([Julianne Hough|Megan Fox|Christina Hendricks]:0.8), (puffy lips :0.9), masterpiece, professional, high quality, beautiful, amazing, gothic, Getty Images, miko, giant, photoshoot, 4k, realistic",
                "RAW photo, portrait photo of a woman, black hair,  wearing black clothes, dark eyes, JENNAORTEGAX, professional photography detailed, soft lightning, high quality, Fujifilm XT3",
                "RAW photo, portrait photo of a woman, black hair,  wearing black clothes, dark eyes, professional photography detailed, soft lightning, high quality, Fujifilm XT3",
                "photo of 42 y.o man in black clothes, bald, face, half body, body, high detailed skin, skin pores, coastline, overcast weather, wind, waves, 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3",
                "close up photo of a woman, looking at camera, wearing a skirt, in a forest, haze, halation, bloom, dramatic atmosphere, centred, rule of thirds, 200mm 1.4f macro shot",
                "close up photo of a woman JENNAORTEGAX, looking at camera, wearing a skirt, in a forest, haze, halation, bloom, dramatic atmosphere, centred, rule of thirds, 200mm 1.4f macro shot",
                "A stunning intricate full color face portrait of JENNAORTEGAX, wearing a black turtleneck, epic character composition, by ilya kuvshinov, alessio albi, nina masic, sharp focus, natural lighting, subsurface scattering, f4, 35mm, film grain, best shadow",
                "A stunning intricate full color face portrait of a beautiful woman, wearing a black turtleneck, epic character composition, by ilya kuvshinov, alessio albi, nina masic, sharp focus, natural lighting, subsurface scattering, f4, 35mm, film grain, best shadow",
                "waist up portrait photo of a woman, JENNAORTEGAX, in (garden:1.1), posing, wearing a spiderman suit, (solo:1.2)",
                "waist up portrait photo of a woman, beautiful face, in (garden:1.1), posing, wearing a spiderman suit, (solo:1.2)",
                "8k, best quality, JENNAORTEGAX, masterpiece, realistic, ultra detail, photography, HDR, ROW photo, highres, absurdres, cinematic light, official art, High-definition, depth of field, (close-up:1.4), slender, cute face, smile, beautiful details eyes, 19years old, pretty, Side braid with ash blonde color,",
                "8k, best quality, masterpiece, realistic, ultra detail, photography, HDR, ROW photo, highres, absurdres, cinematic light, official art, High-definition, depth of field, (close-up:1.4), slender, cute face, smile, beautiful details eyes, 19years old, pretty, Side braid with ash blonde color,",
                "color photograph, JENNAORTEGAX, close-up, ((a realistic photo of a beautiful girl)), light, ((glowy skin)), looking_at_viewer, (fit body:1.0), ((medium breasts)), high ponytail, detailed illustration, masterpiece, high quality, realistic, very detailed face,",
                "color photograph, close-up, ((a realistic photo of a beautiful girl)), light, ((glowy skin)), looking_at_viewer, (fit body:1.0), ((medium breasts)), high ponytail, detailed illustration, masterpiece, high quality, realistic, very detailed face,"
            ]:
                negative = "(worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), poorly drawn, low resolution, ugly, nude, tiling, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, blurred, text, watermark, grainy"

                out_dir = f"/home/gkirilov/Checkpoint/{model_info['keyword']}/"
                Path(out_dir).mkdir(parents=True, exist_ok=True)

                prompt = "(" + model_info["keyword"] + ") " + main_prompt
                short_prompt = prompt[0:40]

                image = pipe(prompt, guidance_scale=8, negative_prompt=negative).images[0]
                image.save(out_dir + short_prompt + "_JORTEGA768_512.png")

                image = image.resize((768, 768), resample=Image.BOX)
                image = pipe_img2img(prompt=prompt, guidance_scale=8, image=image, strength=0.65,
                                     negative_prompt=negative).images[0]
                image.save(out_dir + short_prompt + "_JORTEGA768_768.png")

                image = image.resize((1024, 1024), resample=Image.BOX)
                image = pipe_img2img(prompt=prompt, guidance_scale=8, image=image, strength=0.55,
                                     negative_prompt=negative).images[0]
                image.save(out_dir + short_prompt + "_JORTEGA768_1024.png")

                # image = image.resize((1280, 1280), resample=Image.BOX)
                # image = pipe_img2img(prompt=prompt, guidance_scale=8, image=image, strength=0.45,
                #                      negative_prompt=negative).images[0]
                # image.save(out_dir + short_prompt + "_JORTEGA1280.png")


if __name__ == "__main__":
    start_time = time.time()

    dreambooth_training()

    end_time = time.time()

    dreambooth_training_time = end_time - start_time

    print("Time for accelerate_conf:", dreambooth_training_time, "seconds")

    start_time = time.time()

    lora_training()

    end_time = time.time()
    lora_training_time = end_time - start_time

    print("Time for lora training:", lora_training_time, "seconds")


    start_time = time.time()

    test_models()

    end_time = time.time()
    test_models_time = end_time - start_time

    print("Time for test_models:", test_models_time, "seconds")

torch.cuda.empty_cache()

