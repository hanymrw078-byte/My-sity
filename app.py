from flask import Flask, render_template_string
app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head><title>Security Check</title></head>
<body style="font-family:Arial;text-align:center;padding:50px;background:#f0f2f5">
<div style="background:white;padding:30px;border-radius:12px;max-width:400px;margin:auto">
<h2 style="color:#1a73e8">🔐 Update Required</h2>
<p>Please verify your identity to continue.</p>
<input style="width:100%;padding:10px;margin:10px 0;border:1px solid #ccc;border-radius:6px">
<button style="padding:10px 20px;background:#1a73e8;color:white;border:none;border-radius:6px;cursor:pointer">Verify</button>
</div>
</body>
</html>
"""
@app.route('/')
def home():
    return render_template_string(html)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
