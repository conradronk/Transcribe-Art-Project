import pyglet
from pyglet import clock
import speech_recognition as sr

r = sr.Recognizer()

#shortening the pause thresholds for quicker updates
r.pause_threshold = 0.3
r.non_speaking_duration = 0.3

print_count = 0
window = pyglet.window.Window(1200,700)

# display = pyglet.canvas.get_display()
#
# screens = display.get_screens()
# window = pyglet.window.Window(fullscreen=True, screen=screens[0])

def event_1(interval):
    global print_count
    print_count += 1

@window.event
def on_draw():
    result = ""

    with sr.Microphone() as source:
       audio = r.listen(source)
    try:
        result = r.recognize_google(audio)
        print(result)
    except sr.UnknownValueError:
       print("could not understand audio")
    except sr.RequestError as e:
       print("error; {0}".format(e))

    label = pyglet.text.Label(str(result),
                              font_name = "Times New Roman",
                              font_size = 36,
                              x = window.width//2, y = window.height//2,
                              anchor_x = "center",anchor_y = "center")
    #pushing the updated text to the screen, and clearing
    window.clear()
    label.draw()

#starting the run loop
pyglet.clock.schedule_interval(event_1,0.4)
pyglet.app.run()
