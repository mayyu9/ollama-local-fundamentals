import ollama
import os

model = "llama3.2:1b"

# paths to input and output files
input_file = "./data/user_reviews.txt"
output_file = "./data/summarized_reviews.txt"

# check if the input exists

if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")
    exit(1)

# Read the user reviews from the input file
with open(input_file, 'r') as f:
    items = f.read().strip()

# Prepare the prompt for the model

prompt = f"""
You are an expert analyst extract the user reviews.

Here is the list of user reviews:

{items}

Please:

1. Summarize the reviews based on texture, fragnance, absoprtion etc.. 
"""

# send the prompt and get the response

try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_summary = response.get("response", "")
    print("=======Summarized reviews=======")
    print(generated_summary)
    
    # write the summary to the output file
    with open(output_file, "w") as f:
        f.write(generated_summary.strip())

except Exception as e:
    print("An error occured: ", str(e))