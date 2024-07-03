from flask import Flask, stream_template, request, Response
import openai
import os
import time

def mock_send_messages(messages):
    fake_responses = [
        {"choices": [{"delta": {"content": "Hello"}}]},
        {"choices": [{"delta": {"content": " How"}}]},
        {"choices": [{"delta": {"content": " are"}}]},
        {"choices": [{"delta": {"content": " you?"}}]}
    ]
    for response in fake_responses:
        yield response
        time.sleep(2)

app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        # messages = request.json['messages']
        messages = 'aaa'
        print("start")

        def event_stream():
            for line in mock_send_messages(messages=messages):
                text = line['choices'][0]['delta'].get('content', '')
                if len(text): 
                    yield text

        return Response(event_stream(), mimetype='text/event-stream')
    else:
        return stream_template("")

if __name__ == '__main__':
    app.run()
