import pandas as pd

def transform_file(input_path, output_path):
    # Read the file, replace null bytes
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read().replace('\0', '')

    # Split the data into lines
    lines = data.splitlines()

    # Join the lines into a single string
    flattened_data = ' '.join(lines)

    # Write the flattened data back into a file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(flattened_data)

# Paths to your input and output files
input_path = '/home/gkirilov/prompts/ddg_1M_prompts.csv'
output_path = '/home/gkirilov/prompts/flattened_ddg_1M_prompts.csv'

transform_file(input_path, output_path)
