
import openai
import os
import base64
import requests

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Path to your image
image_path_on_disk = "images/image4-423.png"

# Getting the base64 string
base64_image = encode_image(image_path_on_disk)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}

test_data_generation_sys_prompt = """System: You are an expert in test data generation."
                            "Generate 10 test data samples for the given image in a .csv format"""

test_plan_generation_sys_prompt = """System: You are an expert in QA test plan generation."
                                "Generate a test plan to test the given image comprehensively"""

test_case_generation_sys_prompt = """System: You are an expert in QA test case generation."
                                "Generate all the test cases to test the given image comprehensively"""

selenium_test_case_generation_sys_prompt = """System: You are an expert in selenium and python test case generation." 
"Generate all the selenium and python automation tests  for acceptance testing the s/w behind the provided image 
please"""

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": selenium_test_case_generation_sys_prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 4096
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# print(response.json())
story = response.json()['choices'][0]['message']['content']
print(story)
