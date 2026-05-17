import google.generativeai as genai
from config import MODEL_NAME

model = genai.GenerativeModel(MODEL_NAME)

def chatbot_response(text):
    try:
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"