from flask import Flask, render_template_string
import os
from datetime import datetime, timezone

application = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Python Web Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            text-align: center;
            padding: 70px 15px;
        }
        .card {
            background: white;
            max-width: 600px;
            margin: auto;
            padding: 35px;
            border-radius: 14px;
            box-shadow: 0 5px 20px #00000012;
        }
        h1 { color: #1d4ed8; }
        .status {
            color: #15803d;
            font-weight: bold;
            font-size: 18px;
        }
        button {
            background: #2563eb;
            color: white;
            border: 0;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
        }
        #result { color: #15803d; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h1>My Python Web Application</h1>
        <p class="status">✓ Application is running successfully!</p>
        <p>Built with Python and Flask.</p>
        <p>Hosted on AWS Elastic Beanstalk.</p>
        <button onclick="showMessage()">Test Application</button>
        <p id="result"></p>
        <hr>
        <p>Server time: {{ server_time }}</p>
    </div>
    <script>
        function showMessage() {
            document.getElementById("result").innerText =
                "Success! Your web page is working.";
        }
    </script>
</body>
</html>
"""

@application.route("/")
def home():
    return render_template_string(
        HTML,
        server_time=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@application.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    application.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
