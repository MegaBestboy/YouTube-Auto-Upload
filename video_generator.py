import openai
import elevenlabs
import moviepy.editor as mp
import os
import subprocess

openai.api_key = "your_openai_api_key"  # Replace with your OpenAI Key
elevenlabs.set_api_key("your_elevenlabs_api_key")  # Replace with ElevenLabs Key

# Read script
with open("script.txt", "r", encoding="utf-8") as file:
    script_text = file.read()

# Generate AI Voiceover
audio = elevenlabs.generate(text=script_text, voice="Rachel")
with open("voiceover.mp3", "wb") as f:
    f.write(audio)

# Generate Video with AI Images
clips = []
lines = script_text.split(". ")
for index, line in enumerate(lines):
    response = openai.Image.create(prompt=line, n=1, size="1024x1024")
    image_url = response["data"][0]["url"]
    img_clip = mp.ImageClip(image_url).set_duration(5)
    clips.append(img_clip)

video = mp.concatenate_videoclips(clips)
audio = mp.AudioFileClip("voiceover.mp3")
final_video = video.set_audio(audio)

final_video.write_videofile("generated_video.mp4", fps=24)
print("✅ AI Video Generated!")
subprocess.run(["python", "upload.py"])
