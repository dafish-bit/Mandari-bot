import speech_recognition as speech_recog
from pydub import AudioSegment
import os

def speech_from_audio_file(ruta_archivo):
    # 1. Convertir a WAV si no lo es (para compatibilidad)
    if not ruta_archivo.endswith(".wav"):
        try:
            print(f"🔄 Convirtiendo {ruta_archivo} a WAV...")
            audio = AudioSegment.from_file(ruta_archivo)
            ruta_archivo_wav = "temp_audio.wav"
            audio.export(ruta_archivo_wav, format="wav")
            ruta_archivo = ruta_archivo_wav
        except Exception as e:
            print(f"Error convirtiendo audio: {e}")
            return ""
    
    # 2. Procesar el audio
    recog = speech_recog.Recognizer()
    try:
        with speech_recog.AudioFile(ruta_archivo) as audio_file:
            print(f"🎧 Leyendo el archivo {ruta_archivo}...")
            audio = recog.record(audio_file)

            print("Reconociendo texto...")
            # Usamos recognize_google
            texto = recog.recognize_google(audio, language="es-ES")
            return texto

    except Exception as e:
        print(f"Error al procesar el audio: {e}")
        return ""