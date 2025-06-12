import gradio as gr
from physis_parser import parse_physis_expression

def interpret_physis(input_text):
    try:
        return parse_physis_expression(input_text)
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks() as demo:
    gr.Markdown("## 🌱 Physis Language Interpreter")
    with gr.Row():
        with gr.Column():
            input_box = gr.Textbox(label="Enter Physis Expression")
            interpret_btn = gr.Button("Interpret")
        with gr.Column():
            output_box = gr.Textbox(label="Output")
    interpret_btn.click(interpret_physis, input_box, output_box)
