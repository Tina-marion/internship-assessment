# Dictionary containing translation mappings
translations = {
    'English': {
        'Luganda': {
            'Hello': 'Nkulamusizza',
            'How are you?': 'Oli otya?',
            'Good morning': 'Wasuze otya?',
            'Thank you': 'Webale',
            'Goodbye': 'Weraba'
        },
        'Runyankole': {
            'Hello': 'Agandi',
            'How are you?': 'Ori ota?',
            'Good morning': 'Oraire ota?',
            'Thank you': 'Webare munonga',
            'Goodbye': 'Kare kare'
        },
        'Ateso': {
            'Hello': 'Ejoka',
            'How are you?': 'Ijoi noi?',
            'Good morning': 'Ijoi noi?',
            'Thank you': 'Eyalama',
            'Goodbye': 'Idaar'
        },
        'Lugbara': {
            'Hello': 'Drio',
            'How are you?': 'Ini dridri?',
            'Good morning': 'Mungu alu?',
            'Thank you': 'A\'di',
            'Goodbye': 'Eri'
        },
        'Acholi': {
            'Hello': 'Apwoyo',
            'How are you?': 'Itye maber?',
            'Good morning': 'Otyeno maber?',
            'Thank you': 'Apwoyo matek',
            'Goodbye': 'Bed mamaber'
        }
    },
    # Reverse translations (local language to English)
    'Luganda': {
        'English': {
            'Nkulamusizza': 'Hello',
            'Oli otya?': 'How are you?',
            'Wasuze otya?': 'Good morning',
            'Weebale': 'Thank you',
            'Weraba': 'Goodbye'
        }
    },
    'Runyankole': {
        'English': {
            'Agandi': 'Hello',
            'Oraire gye?': 'How are you?',
            'Oraire ota?': 'Good morning',
            'Webale': 'Thank you',
            'Kare kare': 'Goodbye'
        }
    },
    'Ateso': {
        'English': {
            'Ejoka': 'Hello',
            'Ijoi noi?': 'How are you?',
            'Ijoi noi?': 'Good morning',
            'Eyalama': 'Thank you',
            'Idaar': 'Goodbye'
        }
    },
    'Lugbara': {
        'English': {
            'Drio': 'Hello',
            'Ini dridri?': 'How are you?',
            'Mungu alu?': 'Good morning',
            'A\'di': 'Thank you',
            'Eri': 'Goodbye'
        }
    },
    'Acholi': {
        'English': {
            'Apwoyo': 'Hello',
            'Itye maber?': 'How are you?',
            'Otyeno maber?': 'Good morning',
            'Apwoyo matek': 'Thank you',
            'Bed mamaber': 'Goodbye'
        }
    }
}

def get_language_input(prompt, languages):
    """Helper function to get valid language input"""
    while True:
        lang = input(prompt).strip().capitalize()
        if lang in languages:
            return lang
        print(f"Invalid language. Please choose from: {', '.join(languages)}")

def translate_text():
    """Main translation function"""
    languages = ['English', 'Luganda', 'Runyankole', 'Ateso', 'Lugbara', 'Acholi']
    
    print("\nWelcome to the Uganda Language Translator!\n")
    
    # Get source language
    source = get_language_input(
        "Please choose the source language (English, Luganda, Runyankole, Ateso, Lugbara or Acholi): ",
        languages
    )
    
    # Get a different language
    while True:
        target = get_language_input(
            f"Please choose the target language (not {source}): ",
            languages
        )
        if target != source:
            break
        print(f"Target language cannot be the same as source ({source}). Please choose a different language.")
    
    # Get text to translate
    text = input("Enter the text to translate: ").strip()
    
    # Perform translation
    try:
        if source == 'English':
            translated = translations[source][target][text]
        else:
            translated = translations[source]['English'][text]
            if target != 'English':
                translated = translations['English'][target][translated]
        
        print(f"\nTranslation ({source} → {target}): {translated}")
    except KeyError:
        print("Sorry, translation not found for that text.")

if __name__ == "__main__":
    translate_text()