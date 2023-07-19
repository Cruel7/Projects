import openai
import os
from termcolor import colored
from tqdm import tqdm

# Load the API key
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

current_folder = os.getcwd()
storage_folder = os.path.join(current_folder, "../storage/dreambooth_automation")
processed_results_folder = os.path.join(storage_folder, "generated_prompts/json_results/processed_results/")

# Create a new folder for the results
gpt_generated_prompts_folder = os.path.join(storage_folder, "generated_prompts/gpt_generated_prompts")
os.makedirs(gpt_generated_prompts_folder, exist_ok=True)

# Read the content of the 'prompt.txt' for instructions
with open(current_folder + '/../dreambooth_automation_3/prompt_instructions.txt', 'r') as file:
    instructions = file.read().replace('\n', ' ')

try:
    # Get the list of files in the processed_results_folder
    files = [f for f in os.listdir(processed_results_folder) if os.path.isfile(os.path.join(processed_results_folder, f))]

    # Pre-filter files to be processed
    files_to_process = [filename for filename in files if not os.path.exists(os.path.join(gpt_generated_prompts_folder, filename.rsplit('.', 1)[0] + '_gpt_generated_prompts.txt'))]

    if not files_to_process:
        print(colored("\nAll files have already been processed. Skipping...", "magenta"))
    else:
        # Iterate over each file in the processed_results_folder
        for filename in tqdm(files_to_process, desc="Processing files"):
            # Output file for each input file
            output_file_name = filename.rsplit('.', 1)[0] + '_gpt_generated_prompts.txt'
            output_file_path = os.path.join(gpt_generated_prompts_folder, output_file_name)

            # Read the subjects from each file
            with open(os.path.join(processed_results_folder, filename), 'r') as file:
                subjects = file.read().splitlines()

            with open(output_file_path, 'w') as output_file:
                # Process each subject
                for subject in tqdm(subjects, desc="Processing subjects", leave=False):
                    # Start the conversation with the instructions and subject
                    messages = [{"role": "system", "content": instructions},
                                {"role": "user", "content": subject}]

                    # Send the messages to the API
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo-0613",
                        max_tokens=150,
                        temperature=0.5,
                        messages=messages)

                    # Get the AI's response
                    ai_message = response['choices'][0]['message']['content']

                    # Split the AI's response to separate the descriptive part and the negative part
                    split_message = ai_message.split('NEGATIVE:', 1)
                    description_part = split_message[0][:250]  # limit to 250 characters
                    negative_part = split_message[1][:125] if len(split_message) > 1 else ''  # limit to 125 characters

                    # Write the AI's response to the output file
                    output_file.write(f"Subject: {subject}\nPrompt: {description_part}\n")

                    # If the negative part exists, write it to the output file
                    if negative_part:
                        output_file.write(f"NEGATIVE: {negative_part}\n")
                    else:
                        # Continue the conversation by asking for the negative aspects of the subject
                        messages.append({"role": "user", "content": "What are the potential negative aspects of this scene?"})

                        # Send the updated messages to the API
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo-0613",
                            max_tokens=150,  # limit to 150 tokens
                            temperature=0.5,
                            messages=messages)

                        # Get the AI's new response
                        ai_message = response['choices'][0]['message']['content']

                        # Write the AI's response to the output file without the prefix
                        output_file.write(f"{ai_message[:150]}\n")  # limit to 150 characters

                    # Add an extra line break after each subject
                    output_file.write("\n")

    print(colored("\nGPT prompt files created successfully.", "green"))
except Exception as e:
    print(colored("\nAn error occurred:", str(e),"red"))