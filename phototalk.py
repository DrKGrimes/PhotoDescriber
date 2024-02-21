import base64
import requests
import os
import json

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Directory containing your images
image_dir = "pictures"

# Filter for image files only
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Initialize a list to store the responses
descriptions = []

for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "describe what is in this image"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Add the response to the list
    descriptions.append({
        "image": image_file,
        "description": response.json()
    })

# Output the results to a JSON file
with open('image_descriptions.json', 'w') as outfile:
    json.dump(descriptions, outfile, indent=4)

print("Descriptions saved to image_descriptions.json")






