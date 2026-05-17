import gradio as gr
from utils import process_input

with gr.Blocks() as voice_assistant:

    gr.Markdown("""
    # 🤖 AI Voice Assistant
    Type or speak your question and get AI voice response.
    """)

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(label="Text Input")
            voice_input = gr.Audio(type="filepath", label="Voice Input")
            btn = gr.Button("Submit")

        with gr.Column():
            response_box = gr.Textbox(label="AI Response")
            audio_output = gr.Audio(label="Voice Output")

    btn.click(
        fn=process_input,
        inputs=[text_input, voice_input],
        outputs=[response_box, audio_output]
    )

if __name__ == "__main__":
    voice_assistant.launch(share=True)