from pyttsx3 import init

engine = init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.say("Eccomi! dimmi di cosa hai bisogno.")
engine.runAndWait()
