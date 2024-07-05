from flask import Flask, stream_template, request, Response
from utils.utils import query_engine

def mock_send_messages(messages):
    fake_responses = [
        {"choices": [{"delta": {"content": "Hello"}}]},
        {"choices": [{"delta": {"content": " How"}}]},
        {"choices": [{"delta": {"content": " are"}}]},
        {"choices": [{"delta": {"content": " you?"}}]}
    ]
    for response in fake_responses:
        yield response
        time.sleep(1)

app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        messages = request.json['messages']
        print(messages)
        print("start")

        def event_stream():
            streaming_response = query_engine.query(messages)
            for r in streaming_response.response_gen:
                if r is not None:
                    yield r

        return Response(event_stream(), mimetype='text/event-stream')
    else:
        return stream_template("./chat.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)