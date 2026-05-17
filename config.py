import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

print("ENV PATH:", ENV_PATH)

load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("GOOGLE_API_KEY")

print("DEBUG API KEY:", api_key)

if api_key is None:
    raise ValueError("API KEY NOT LOADED - .env issue")

genai.configure(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"