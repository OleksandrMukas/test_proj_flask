from flask import Flask, jsonify, render_template_string
import datetime
import platform

app = Flask(__name__)

START_TIME = datetime.datetime.now()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask CI/CD Demo</title>
</head>
<body>
    <h1>🚀 Flask CI/CD Demo App</h1>

    <p><b>Server time:</b> {{ time }}</p>
    <p><b>Hostname:</b> {{ hostname }}</p>
    <p><b>Python version:</b> {{ python_version }}</p>

    <hr>
    <p>Цей сайт використовується для тренування CI/CD pipeline (Jenkins).</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        time=datetime.datetime.now(),
        hostname=platform.node(),
        python_version=platform.python_version()
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/info")
def info():
    return jsonify({
        "app": "flask-ci-demo",
        "status": "running",
        "start_time": str(START_TIME),
        "current_time": str(datetime.datetime.now())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
