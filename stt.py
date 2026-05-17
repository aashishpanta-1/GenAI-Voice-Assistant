from faster_whisper import WhisperModel
import soundfile as sf

whisper_model = WhisperModel("base")

def transcribe_audio(audio_path):
    audio, sr = sf.read(audio_path)

    temp_path = "temp/audio.wav"
    sf.write(temp_path, audio, sr)

    segments, _ = whisper_model.transcribe(temp_path)

    text = " ".join([segment.text for segment in segments])
    return text