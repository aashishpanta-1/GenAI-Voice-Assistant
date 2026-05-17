from stt import transcribe_audio
from llm import chatbot_response
from tts import text_to_speech

def process_input(text_input, voice_input):

    # If voice input exists → convert to text
    if voice_input is not None:
        text_input = transcribe_audio(voice_input)

    if not text_input:
        text_input = "Hello"

    # AI response
    response = chatbot_response(text_input)

    # Convert to speech
    audio_file = text_to_speech(response)

    return response, audio_file