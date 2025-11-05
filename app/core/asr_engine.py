import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_url):
    # Download or access Twilio audio file here if necessary
    result = model.transcribe(audio_url)
    return result["text"]
