from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
SERVICE_ACCOUNT_FILE = "client_secret.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

youtube = build("youtube", "v3", credentials=credentials)

def upload_video(video_file, title, description):
    request = youtube.videos().insert(
        part="snippet,status",
        body={"snippet": {"title": title, "description": description}, "status": {"privacyStatus": "public"}},
        media_body=MediaFileUpload(video_file, resumable=True),
    )
    response = request.execute()
    print("✅ Video Uploaded:", response["id"])

upload_video("generated_video.mp4", "My AI Video", "This video was made using AI!")
