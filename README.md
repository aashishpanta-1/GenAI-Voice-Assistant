# GenAI Voice Assistant

A lightweight AI-powered voice assistant built using Python, Gemini API, Whisper STT, and Edge-TTS.  
It accepts voice or text input and responds with both text and speech output.

---

## Features

- Voice input support using Whisper (speech-to-text)
- Text input support
- AI responses using Google Gemini API
- Natural speech output using Edge-TTS
- Simple web interface using Gradio
- Runs efficiently on CPU (no GPU required)

---

## Tech Stack

- Python
- Gradio
- faster-whisper
- Google Generative AI (Gemini)
- Edge-TTS
- Soundfile
- SciPy

---

## Project Structure

```text
voice-assistant/
│
├── app.py
├── config.py
├── llm.py
├── stt.py
├── tts.py
├── utils.py
│
├── requirements.txt
├── .env
│
├── temp/
│   ├── audio.wav
│   ├── response.mp3
