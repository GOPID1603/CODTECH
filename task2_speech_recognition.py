import speech_recognition as sr

def transcribe_audio_file(file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    try:
        print(f"Reading audio file: {file_path}")
        with sr.AudioFile(file_path) as source:
            # Load the audio to memory
            audio_data = recognizer.record(source)

            print("Recognizing speech...")
            # Use Google Web Speech API (does not require API key for basic usage)
            text = recognizer.recognize_google(audio_data)
            return text
            
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    except FileNotFoundError:
        return f"File {file_path} not found. Please ensure the file exists."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("=== CODTECH Task 2: Speech Recognition System ===")
    # Note: Requires a sample_audio.wav in the same directory.
    # To run this properly, ensure you have a valid wav file.
    audio_file = "sample_audio.wav" 
    
    transcription = transcribe_audio_file(audio_file)
    print("\n--- Transcription ---")
    print(transcription)
