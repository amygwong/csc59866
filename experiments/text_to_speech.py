import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using _google for Google Speech Recognition or _sphinx for Sphinx
            value = r.recognize_google(audio)
            print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
except KeyboardInterrupt:
    pass