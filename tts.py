import edge_tts
import asyncio
import os

OUTPUT_FILE = "temp/response.mp3"

def text_to_speech(text):

    # AUTO CREATE FOLDER (IMPORTANT FIX)
    os.makedirs("temp", exist_ok=True)

    async def generate():
        communicate = edge_tts.Communicate(
            text,
            "en-US-AriaNeural"
        )
        await communicate.save(OUTPUT_FILE)

    asyncio.run(generate())

    return OUTPUT_FILE