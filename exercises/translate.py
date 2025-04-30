import requests
import json

# Configuration
API_URL = "https://api.sunbird.ai/tasks/nllb_translate"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwYXRyaWNrY21kIiwiYWNjb3VudF90eXBlIjoiRnJlZSIsImV4cCI6NDg2OTE4NjUzOX0.wcFG_GjBSNVZCpP4NPC2xk6Dio8Jdd8vMb8e_rzXOFc"

LANGUAGES_CODES = {
    "eng": "English",
    "lug": "Luganda",
    "nyn": "Runyankole",
    "ach": "Acholi",
    "teo": "Ateso",
    "lgg": "Lugbara"
}

# Invert the LANGUAGES_CODES for name-to-code mapping
LANGUAGE_NAMES = {name.lower(): code for code, name in LANGUAGES_CODES.items()}

def normalize_language_input(input_lang):
    
    input_lang = input_lang.strip().lower()
    if input_lang in LANGUAGES_CODES:
        return input_lang
    elif input_lang in LANGUAGE_NAMES:
        return LANGUAGE_NAMES[input_lang]
    return None

def translate_text(text, source_lang, target_lang):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "source_language": source_lang,
        "target_language": target_lang,
        "text": text
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["output"]["translated_text"]
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: {str(e)}"
    except KeyError:
        return "⚠️ Error: Invalid response format from server."

def main():
    print("Sunbird AI Translator ")
    print("Available languages:")
    for code, name in LANGUAGES_CODES.items():
        print(f"  {name}: {code}")
    
    print("\nType 'end' at any point to exit.")

    while True:
        source_input = input("\nSource language (one of the available languages ): ").strip()
        if source_input.lower() == 'end':
            print("👋 Goodbye!")
            break

        target_input = input("Target language (enter a different language ): ").strip()
        if target_input.lower() == 'end':
            print("👋 Goodbye!")
            break

        source_lang = normalize_language_input(source_input)
        target_lang = normalize_language_input(target_input)

        if not source_lang or not target_lang:
            print("Unsupported language input. Please use valid code or name.")
            continue

        if source_lang == target_lang:
            print("Source and target languages must be different.")
            continue

        text = input("Enter text to translate: ").strip()
        if text.lower() == 'end':
            print("👋 Goodbye!")
            break
        if not text:
            print("Please enter some text.")
            continue

        print("🔄 Translating...")
        translated = translate_text(text, source_lang, target_lang)
        print(f"📝 Translation ({LANGUAGES_CODES[target_lang]}): {translated}")

if __name__ == "__main__":
    main()
