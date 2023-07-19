import argparse
import os
import sys
import glob
import torch
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
from pathlib import Path
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

def infer_models(model_dir, output_base_dir):
    Path(output_base_dir).mkdir(parents=True, exist_ok=True)

    model_name = os.path.basename(model_dir)
    out_dir = f"{output_base_dir}/{model_name}/"
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    pipe = StableDiffusionPipeline.from_pretrained(model_dir, safety_checker=None, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    pipe_img2img = StableDiffusionImg2ImgPipeline.from_pretrained(model_dir, safety_checker=None, torch_dtype=torch.float16)
    pipe_img2img = pipe_img2img.to("cuda")

    print(f"Model {model_name} is on: {pipe.device}")
    print(f"Image-to-Image model {model_name} is on: {pipe_img2img.device}")

    pipe.enable_xformers_memory_efficient_attention()
    pipe_img2img.enable_xformers_memory_efficient_attention()

    # Load instance prompts from the file
    with open('instance_prompt.txt', 'r') as f:
        instance_prompts = f.read().strip().split('\n')

    for instance_prompt in instance_prompts:
        if instance_prompt in model_name:  # Check if instance prompt is in the model name
            for main_prompt in [

                "woman, solo, black hair, dark blue eyes, detailed face, (puffy lips :0.9), masterpiece, professional, high quality, beautiful, amazing, gothic, Getty Images, miko, giant, photoshoot, 4k, realistic",
                "A big poison dart frog under a mushroom, animal, background rain forest, 3d uv colors, ultra reallistic, extremely detailed, 8k, poster, ultra detailed,high definition, colourful",
                "RAW photo, portrait photo of a woman, black hair,  wearing black clothes, dark eyes, professional photography detailed, soft lightning, high quality, Fujifilm XT3",
                # "photo of 42 y.o man in black clothes, bald, face, half body, body, high detailed skin, skin pores, coastline, overcast weather, wind, waves, 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3",
                # "A stunning intricate full color face portrait wearing a black turtleneck, epic character composition, by ilya kuvshinov, alessio albi, nina masic, sharp focus, natural lighting, subsurface scattering, f4, 35mm, film grain, best shadow",
                # "waist up portrait photo of a woman, in (garden:1.1), posing, wearing a spiderman suit, (solo:1.2)",
                # "Rainy street with two women by Leonid Afremov, digital painting, ultra reallistic, intricate, beautiful, dynamic lighting, ultra detailed, colourful, light reflections.",
                # "8k, best quality, slender, cute face, smile, masterpiece, realistic, ultra detail, photography, HDR, RAW photo, highres, absurdres, cinematic light, official art, High-definition, depth of field, (close-up:1.4), beautiful details eyes, 19years old, pretty, Side braid with ash blonde color,",
                # "realistic digital painting of a beautiful woman bathing in a fountain, ice hair, platinum hair, fractal ice crystals, highly detailed, intricate, elegant",
                # "meadow, rivers, blue skies, castles, magnificent, light effect, high - definition, unreal engine, beautiful, by Marc Simonetti and Caspar David Friedrich",
                # "color photograph, close-up, ((a realistic photo of a beautiful girl)), light, ((glowy skin)), looking_at_viewer, (fit body:1.0), ((medium breasts)), high ponytail, detailed illustration, masterpiece, high quality, realistic, very detailed face",
                # "A beautiful teen girl with long hair and a hair bun, a flower in her hair, gentle smile, blue eyes, a character portrait, pre-raphaelitism, studio photograph, enchanting",
                # "Inside a Swiss chalet, snow capped mountain view out of window, with a fireplace, at night, interior design, d & d concept art, d & d wallpaper, warm, digital art. art by james gurney and larry elmore, extremely detailed, intricate, beautiful, colourful.",
                # "Seductive lingerie, portrait, luminous necklace, luminous butterflies, film grain, closeup, focus blur"
                # "aerial view of a giant fish tank shaped like a tower in the middle of new york city, 8k octane render, photorealistic --ar 9:20",
                # "THE CHERRY BLOSSOM TREE HOUSE, beautiful ornate treehouse in a gigantic pink cherry blossom tree on a high blue grey and brown cliff with light snow and pink cherry blossom trees :: Intricate details, very realistic, cinematic lighting, volumetric lighting, photographic",
                # "portrait art of blade runner 8 k ultra realistic, lens flare, atmosphere, glow, detailed, intricate, full of colour, cinematic lighting, trending on artstation, 4 k, hyperrealistic, focused, extreme details, unreal engine 5, cinematic, masterpiece",
                # "stunning city of stone inside a gray granite canyon, fusion of star wars and gothic revival architecture, by marc simonetti, natural volumetric lighting, realistic 4k octane beautifully detailed render, 4k post-processing —ar 9:16 —no people --uplight",
                # "photo of 8k ultra realistic harbour, port, boats, sunset, beautiful light, golden hour, full of colour, cinematic lighting, battered, trending on artstation, 4k, hyperrealistic, focused, extreme details, unreal engine 5, cinematic, masterpiece, art by studio ghibli",
                # "peaceful landscape, cinematic, 8k, detailed, realistic , octane render, --ar 828:1792 --q 2 --upbeta",
                # "ultra realistic illustration and highly detailed digital render of panorama view in a dark underground cavern rich in huge colorful crystal",
                # "ethereal winter flowers, carved ice door at the end of ice steps, magical atmosphere, Renato muccillo, Andreas Rocha, Johanna Rupprecht, Beardsley, Unreal render, cinematic blue --aspect 9:16 --s 2500",
                # "valley, fairytale treehouse village covered , matte painting, highly detailed, dynamic lighting, cinematic, realism, realistic, photo real, sunset, detailed, high contrast, denoised, centered, michael whelan",
                # "Bucharest| street| old town, old city| winter| heavy snow| comprehensive cinematic| Atmosphere| Masterpiece",
                # "ethereal winter flowers, carved ice door at the end of ice steps, magical atmosphere, Renato muccillo, Andreas Rocha, Johanna Rupprecht, Beardsley, Unreal render, cinematic blue --aspect 9:16 --s 2500",
                # "Garden+factory, Tall factory, Many red rose, A few roses, clouds, ultra wide shot, atmospheric, hyper realistic, 8k, epic composition, cinematic, octane render, artstation landscape vista photography by Carr Clifton & Galen Rowell, 16K resolution,",
                # "futuristic synthwave city, retro sunset, crystals, spires, volumetric lighting, studio Ghibli style, rendered in unreal engine with clean details --ar 9:16 --hd --q 2",
                # "Garden China Palace, Many flowers, A few roses, clouds, dramatic clouds above, pink, dreamy ultra wide shot, atmospheric, hyper realistic, 8k, epic composition, cinematic, octane render, artstation landscape vista photography by Carr Clifton & Galen Rowell",
                # "Garden+factory, Tall factory, Many red rose, A few roses, clouds, ultra wide shot, atmospheric, hyper realistic, 8k, epic composition, cinematic, octane render, artstation landscape vista photography by Carr Clifton & Galen Rowell",
                # "matte painting of floating clean and bright city in the sky, Hyperrealistic, highly detailed, cinematic lighting",
                # "Garden factory, Tall factory, Many yellow marigold , A few roses, clouds, ultra wide shot, atmospheric, hyper realistic, 8k, epic composition, cinematic, octane render",
                # "futuristic tempura food, night, japanese, neon light, volumetric smoke, volumetric light, octane render, food commercial, Filmic",
                # "steam locomotive train running through the snowy mountains, the polar express, scenic landscape, stunning environment, dusk, mist, realistic, dramatic lighting, highly detailed, intricate, volumetric lighting",
                # "highly detailed marble and jade sculpture of a female necromancer, volumetric fog, Hyperrealism, breathtaking, ultra realistic, unreal engine, ultra detailed, cyber background, Hyperrealism, cinematic lighting, highly detailed, breathtaking , photography, stunning environment"

            ]:
                negative = "(worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, no glasses, ((monochrome)), ((grayscale)), poorly drawn, low resolution, ugly, nude, tiling, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, blurred, text, watermark, grainy"

                full_prompt = f"{instance_prompt} {main_prompt}"
                prompt = "(" + model_name[0:10] + ") " + full_prompt
                model_parts = model_name.split('_')
                # Adjusted filename
                short_prompt = model_parts[1] + '_' + instance_prompt[:15] + '_' + main_prompt[:20]

                image = pipe(prompt, guidance_scale=8, negative_prompt=negative).images[0]
                image.save(out_dir + short_prompt + "_512.png")

                image = image.resize((768, 768), resample=Image.BOX)
                image = \
                    pipe_img2img(prompt=prompt, guidance_scale=8, image=image, strength=0.65, negative_prompt=negative).images[
                        0]
                image.save(out_dir + short_prompt + "_768.png")

                image = image.resize((1024, 1024), resample=Image.BOX)
                image = \
                    pipe_img2img(prompt=prompt, guidance_scale=8, image=image, strength=0.55, negative_prompt=negative).images[
                        0]
                image.save(out_dir + short_prompt + "_1024.png")

                torch.cuda.empty_cache()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--models_dir", required=True, type=str, help="Directory where the models are located.")
    parser.add_argument("--output_base_dir", required=True, type=str, help="Output directory where the generated images are saved.")
    args = parser.parse_args()

    main_dir = args.models_dir
    output_base_dir = args.output_base_dir
    for sub_dir in glob.glob(os.path.join(main_dir, '*')):
        infer_models(sub_dir, output_base_dir)