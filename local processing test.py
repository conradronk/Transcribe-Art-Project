import speech_recognition as sr

 # obtain audio from the microphone
r = sr.Recognizer()

r.pause_threshold = 0.1
r.non_speaking_duration = 0.1
 # recognize speech using Sphinx

while True:
    with sr.Microphone() as source:
       audio = r.listen(source)
    try:
        print(r.recognize_sphinx(audio))
    except sr.UnknownValueError:
       print("Sphinx could not understand audio")
    except sr.RequestError as e:
       print("Sphinx error; {0}".format(e))
