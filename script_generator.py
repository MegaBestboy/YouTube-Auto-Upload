import requests
import sys
import subprocess

def generate_script(topic):
    api_key = "your_deepai_api_key"  # Replace with your DeepAI API Key
    response = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={"text": f"Write a viral YouTube script about {topic}."},
        headers={"api-key": api_key}
    )
    return response.json()["output"]

topic = sys.argv[1]
script = generate_script(topic)

with open("script.txt", "w", encoding="utf-8") as file:
    file.write(script)

print("✅ Script generated!")
subprocess.run(["python", "video_generator.py"])  # Move to next step
