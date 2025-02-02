from transformers import pipeline
import gradio as gr

caption_generation = pipeline("text-generation", model="distilgpt2")

def caption_gen (prompt):
    result = caption_generation(prompt, max_length=30,num_return_sequences=1, temperature=0.9, top_k=50, top_p=0.9)
    return result[0]['generated_text']

interface = gr.Interface(
    fn=caption_gen,
    inputs=gr.Textbox(lines=2,placeholder="یک کلمه یا یک جمله را وارد کنید."),
    outputs="text",
    title="تولید کپشن برای فضای مجازی",
    description="یک کلمه یا یک جمله وارد کنید تا کپشن جذاب دریافت کنید.",
)

interface.launch()