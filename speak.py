import requests
import simpleaudio as sa
def speak(message):
  response = requests.post("http://localhost:8000/tts", json={"text": message})
  if response.status_code == 200:
      audio_data = response.content
      play_obj = sa.WaveObject.from_wave_file(audio_data).play()
      play_obj.wait_done()
  else:
      print("Error: Unable to get TTS audio")
