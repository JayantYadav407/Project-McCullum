import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

def listen_and_translate(src_lang='en', dest_lang='hi'):
    recognizer = sr.Recognizer()
    translator = Translator()

    with sr.Microphone() as source:
        print("Please speak now (English)...")
        audio = recognizer.listen(source)

    try:
        # Convert speech to text (English)
        text = recognizer.recognize_google(audio, language=src_lang)
        print(f"You said ({src_lang}): {text}")

        # Translate text to Hindi
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        print(f"Translation ({dest_lang}): {translated.text}")

        # Convert translated Hindi text to speech
        tts = gTTS(translated.text, lang=dest_lang)
        filename = "temp_output.mp3"
        tts.save(filename)

        # Play Hindi audio
        playsound.playsound(filename)

        # Remove temporary audio file
        os.remove(filename)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    listen_and_translate('en', 'hi')
