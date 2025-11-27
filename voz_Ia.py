import pyttsx3

# Inicializar el motor
engine = pyttsx3.init()

# Configurar parámetros
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

# Selecciona una voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Texto a convertir
def texto_ia (texto):
    engine.save_to_file(texto, 'audio.mp3')
    engine.runAndWait()
