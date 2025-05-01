
import requests
import os
from pydub import AudioSegment

# Configuration
API_URL = "https://api.sunbird.ai/tasks/org/stt"
ACSESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwYXRyaWNrY21kIiwiYWNjb3VudF90eXBlIjoiRnJlZSIsImV4cCI6NDg2OTE4NjUzOX0.wcFG_GjBSNVZCpP4NPC2xk6Dio8Jdd8vMb8e_rzXOFc"
SUPPORTED_FORMATS = ['.wav', '.mp3', '.ogg', '.m4a', '.aac']

# Supported languages
LANGUAGES = {
    "english": "eng",
    "luganda": "lug",
    "runyankole": "run",
    "ateso": "ate",
    "lugbara": "lgg",
    "acholi": "ach"
}

def convert_audio(input_path, output_format='wav'):
    """Converting audio to API-supported format if needed"""
    try:
        audio = AudioSegment.from_file(input_path)
        filename = f"converted.{output_format}"
        audio.export(filename, format=output_format)
        return filename
    except Exception as e:
        print(f"Conversion failed: {str(e)}")
        return None

def transcribe_audio(audio_path):
    
    headers = {"Authorization": f"Bearer {ACSESS_TOKEN}"}
    
    try:
        with open(audio_path, 'rb') as audio_file:
            files = {'audio': (os.path.basename(audio_path), audio_file, 'audio/wav')}
            data = {
                'language': 'eng',
                'adapter': 'eng',
                'recognise_speakers': 'false',
                'whisper': 'false'
            }
            response = requests.post(API_URL, headers=headers, files=files, data=data)
            response.raise_for_status()
            return response.json().get("audio_transcription", "No transcription found")
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("\n🔊 Sunbird AI Audio Transcriber")
    print("Supported formats: WAV, MP3, OGG, M4A, AAC files")
    print("Supported languages: English, Luganda, Runyankole, Ateso, Lugbara, Acholi\n")
   
    
    while True:
        audio_path = input("Enter AUDIO path (or 'end'): ").strip(' "\'')
        
        if audio_path.lower() == 'end':
            break
            
        if not os.path.exists(audio_path):
            print("File not found. Try again.")
            continue

        print("Please choose the target language (English, Luganda, Runyankole, Ateso, Lugbara or Acholi):")
        language_choice = input(">> ").strip().lower()

        if language_choice not in LANGUAGES:
            print("Unsupported language. Try again.")
            continue

        lang_code = LANGUAGES[language_choice]
            
        # Handle format conversion if needed
        ext = os.path.splitext(audio_path)[1].lower()
        if ext not in SUPPORTED_FORMATS:
            print("Converting to WAV format...")
            converted_path = convert_audio(audio_path)
            if not converted_path:
                continue
            audio_path = converted_path
            
        print(" 🔁Transcribing...")
        transcription = transcribe_audio(audio_path)
        
        print(f"\n📝 Audio transcription text in {language_choice}:")
        print(transcription)
        
       
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")