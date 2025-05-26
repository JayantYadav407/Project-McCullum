import os
import requests
import tempfile
import speech_recognition as sr
import pyttsx3
from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import playsound

# Initialize English text-to-speech engine
engine = pyttsx3.init()

def speak(text, lang="en"):
    """
    Convert text to speech.
    If the language is Hindi, use gTTS for text-to-speech and playsound.
    """
    if lang == "hi":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            tts = gTTS(text=text, lang="hi")
            tts.save(temp_audio.name)
            temp_audio.close()
            try:
                playsound.playsound(temp_audio.name)
            finally:
                os.remove(temp_audio.name)
    else:
        engine.say(text)
        engine.runAndWait()

def download_audio_from_url(audio_url):
    """
    Download an audio file from a given URL and save it as a temporary file.
    """
    response = requests.get(audio_url, stream=True)
    if response.status_code == 200:
        temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        with open(temp_audio_file.name, 'wb') as file:
            file.write(response.content)
        return temp_audio_file.name
    else:
        raise Exception(f"Failed to download audio file. Status code: {response.status_code}")

def transcribe_audio(audio_path):
    """
    Transcribe audio to text using SpeechRecognition.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        print("Transcribing audio...")
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Transcribed Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def translate_to_hindi(text):
    """
    Translate English text to Hindi using Helsinki-NLP's opus-mt-en-hi model.
    """
    # Load the pre-trained model and tokenizer
    model_name = "Helsinki-NLP/opus-mt-en-hi"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Perform translation
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translated_text

def main():
    print("Audio File-Based English to Hindi Translator")
    speak("Welcome to the audio file-based English to Hindi translator. Provide an audio file URL to begin.")

    while True:
        print("\nEnter an audio file URL or type 'quit' to exit.")
        audio_url = input("Audio URL: ").strip()
        if audio_url.lower() == "quit":
            speak("Goodbye!")
            print("Goodbye!")
            break
        
        try:
            # Download and transcribe audio
            audio_path = download_audio_from_url(audio_url)
            english_text = transcribe_audio(audio_path)

            if not english_text:
                continue
            
            # Translate and speak the Hindi translation
            hindi_translation = translate_to_hindi(english_text)
            print(f"Hindi Translation: {hindi_translation}")
            speak(hindi_translation, lang="hi")

        except Exception as e:
            error_message = f"Error: {e}"
            print(error_message)
            speak(error_message)

        finally:
            # Clean up downloaded audio file
            if os.path.exists(audio_path):
                os.remove(audio_path)

if __name__ == "__main__":
    main()
