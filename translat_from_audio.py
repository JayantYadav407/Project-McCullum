import speech_recognition as sr

def transcribe_audio(wav_path):
    """
    Transcribe text from a WAV file using SpeechRecognition.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_path) as source:
            print("Processing the WAV file...")
            audio = recognizer.record(source)  # Read the entire WAV file
            text = recognizer.recognize_google(audio)  # Recognize speech using Google Web Speech API
            return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Error with the speech recognition service: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("WAV File Transcription Tool")
    while True:
        wav_path = input("\nEnter the path to the WAV file or type 'quit' to exit:\nWAV File Path: ")
        if wav_path.lower() == 'quit':
            print("Exiting...")
            break
        
        transcription = transcribe_audio(wav_path)
        print("\nTranscription:")
        print(transcription)

if __name__ == "__main__":
    main()
