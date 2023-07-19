import openai
import re
import os

# Load the API key
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

# Read the content of the .txt file
current_folder = os.getcwd()
storage_folder = os.path.join(current_folder, "..")
with open(os.path.join(storage_folder, 'prompt.txt'), 'r') as file:
    content = file.read().replace('\n', ' ')

# Start the conversation with the content of the .txt file
messages = [{"role": "system", "content": content}]

# Ask the user for the subject
subject = input("Subject: ")

# Add the user's subject to the messages
messages.append({"role": "user", "content": subject})

# Send the messages to the API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    max_tokens=300,
    temperature=0.2,
    messages=messages)

# Get the AI's response
ai_message = response['choices'][0]['message']['content']

# Add the AI's response to the messages
messages.append({"role": "assistant", "content": ai_message})

# Print the AI's response
print(f"AI: {ai_message}")

# Now continue the conversation
while True:
    # Get the user's next message
    user_message = input("User: ")

    # Add the user's message to the messages
    messages.append({"role": "user", "content": user_message})

    # Send the updated messages to the API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        max_tokens=300,
        temperature=0.5,
        messages=messages)

    # Get the AI's new response
    ai_message = response['choices'][0]['message']['content']

    # Add the AI's response to the messages
    messages.append({"role": "assistant", "content": ai_message})

    # Print the AI's response
    print(f"AI: {ai_message}")
