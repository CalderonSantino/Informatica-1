import openai

#Convertir audio en texto
class Transcriber:
    def __init__(self):
        pass
        
    #Siempre guarda y lee del archivo audio.mp3
    #Utiliza whisper en la nube :) puedes cambiarlo por una impl local
    def transcribe(self, audio):
        audio_file= open(audio, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript.text