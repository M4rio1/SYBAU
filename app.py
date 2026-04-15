from flask import Flask, render_template, request, Response, stream_with_context
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    
    def generate():
        try:
            # THE OVERRIDE: We hit the raw engine port directly. No middlemen.
            url = 'http://127.0.0.1:11434/api/chat'
            payload = {
                "model": data.get('model', 'deepseek-r1:8b'),
                "messages": data.get('messages', [])
            }
            
            # stream=True rips the data out of the port packet-by-packet
            with requests.post(url, json=payload, stream=True) as r:
                for line in r.iter_lines():
                    if line:
                        # Decode the raw JSON machine code and extract just the text
                        chunk = json.loads(line)
                        content = chunk.get('message', {}).get('content', '')
                        if content:
                            yield content.encode('utf-8')
                            
        except Exception as e:
            print(f"Engine Error: {e}")
            yield f"\n\nSystem Error: {e}".encode('utf-8')

    # THE ANTI-BUFFER SHIELD: These headers forbid Windows and Web Browsers from holding the data
    headers = {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'X-Accel-Buffering': 'no'
    }

    return Response(stream_with_context(generate()), headers=headers)

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)