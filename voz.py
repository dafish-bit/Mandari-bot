import speech_recognition as speech_recog
#### V1 - función
def speech():
    try:
        mic = speech_recog.Microphone()
        recog = speech_recog.Recognizer()
        with mic as audio_file:
            print("Habla ):<")
            recog.adjust_for_ambient_noise(audio_file)
            audio = recog.listen(audio_file)
            return recog.recognize_google(audio, language="es-GB")
    except Exception as e:
        return f"Ni idea ¯\_(ツ)_/¯ {e}"
import pyttsx3
def talk(text):
# Inicializar el motor

    engine = pyttsx3.init()
    
    # Configurar parámetros

    engine.setProperty('rate', 150) # Tasa de habla

    engine.setProperty('volume', 0.9) # Volumen

    # Selecciona una voz

    voices = engine.getProperty('voices')

    for v in range(len(voices)): 
        print(voices[v].name,v )
    engine.setProperty('voice', voices[27].id) # 0 - hombre, 1 - mujer (depende del sistema)

    # Texto a vocalizar



    # Vocalizar el texto

    engine.say(text)

    # Ejecutar la síntesis

    engine.runAndWait()
talk("ODA A LAS PAPAS FRITAS Chisporrotea en el aceite hirviendo la alegría del mundo las papas fritas entran en la sartén como nevadas plumas de cisne matutino y salen semidoradas por el crepitante ámbar de las olivas. El ajo les añade su terrenal fragancia, la pimienta, polen que atravesó los arrecifes, y vestidas de nuevo con traje de marfil, llenan el plato con la repetición de su abundancia y su sabrosa sencillez de tierra.")
