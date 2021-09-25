import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

def listen():
    with mic as source:
        try:
            print("Listening")
            r.adjust_for_ambient_noise(source)
            audio_text = r.listen(source)
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text)
            print(text)

        except:
            print('Sorry.. run again...')
    return str(text)