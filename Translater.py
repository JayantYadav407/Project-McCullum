import speech_recognition as sr
import pyttsx3
from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import tempfile
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

def listen():
    """
    Listen to voice input and convert it to text using SpeechRecognition.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now:")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
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
    print("Voice-based English to Hindi Translator")
    speak("Welcome to the voice-based English to Hindi translator. Speak your English sentence after the beep.")

    while True:
        print("\nSay 'quit' to exit.")
        english_text = listen()
        if not english_text:
            continue
        if english_text.lower() == "quit":
            speak("Goodbye!")
            print("Goodbye!")
            break
        
        # Translate and speak the Hindi translation
        try:
            hindi_translation = translate_to_hindi(english_text)
            print(f"Hindi Translation: {hindi_translation}")
            speak(hindi_translation, lang="hi")
        except Exception as e:
            error_message = f"Error during translation: {e}"
            print(error_message)
            speak(error_message)

if __name__ == "__main__":
    main()
