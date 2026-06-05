import whisper

model = whisper.load_model("base")

result = model.transcribe("sample_video.mp4")

print("\nTRANSCRIPTION:\n")

print(result["text"])