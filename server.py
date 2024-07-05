import gradio as gr
from utils.utils import query_engine

def predict(message, history):
    streaming_response = query_engine.query(message)
    partial_message = ""
    for r in streaming_response.response_gen:
        if r is not None:
            partial_message = partial_message + r
            yield partial_message

gr.ChatInterface(predict).launch(server_name="192.168.0.154", server_port=7860)