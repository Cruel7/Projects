import openai
import os

# Load the API key
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

current_folder = os.getcwd()
storage_folder = os.path.join(current_folder, "../storage/dreambooth_automation")
generated_prompts_folder = os.path.join(storage_folder, "generated_prompts/")

# Read the content of the 'prompt.txt' for instructions
with open(current_folder + '/../dreambooth_automation_3/prompt_instructions.txt', 'r') as file:
    instructions = file.read().replace('\n', ' ')

# Read the subjects from 'generated_results.txt'
with open(generated_prompts_folder + '/processed_results/architecture_processed_results.txt', 'r') as file:
    subjects = file.read().splitlines()

# Output file
with open(generated_prompts_folder + 'gpt_generated_prompts.txt', 'w') as output_file:
    # Process each subject
    for subject in subjects:
        # Start the conversation with the instructions and subject
        messages = [{"role": "system", "content": instructions},
                    {"role": "user", "content": subject}]

        # Send the messages to the API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            max_tokens=300,
            temperature=0.2,
            messages=messages)

        # Get the AI's response
        ai_message = response['choices'][0]['message']['content']

        # Split the AI's response to separate the descriptive part and the negative part
        split_message = ai_message.split('NEGATIVE:', 1)
        description_part = split_message[0][:250]  # limit to 200 characters
        negative_part = split_message[1][:125] if len(split_message) > 1 else ''  # limit to 100 characters

        # Write the AI's response to the output file
        output_file.write(f"Subject: {subject}\nAI: {description_part}\n")

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
