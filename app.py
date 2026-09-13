from flask import Flask, request, jsonify, render_template_string, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Queue for text messages (stores ALL messages)
message_queue = []
latest_voice = None


# ---------- Home Page ----------
page = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Assistive Device Message Center</title>
<style>
  body {font-family:Arial;background:#f3f4f6;display:flex;
        flex-direction:column;align-items:center;justify-content:center;height:100vh;}
  .card {background:white;padding:30px;border-radius:15px;
         box-shadow:0 0 15px rgba(0,0,0,0.1);width:340px;text-align:center;}
  input,button{padding:10px;margin:8px;width:90%;border-radius:6px;border:1px solid #ccc;}
  button{background:#2563eb;color:white;border:none;cursor:pointer;}
  button:hover{background:#1d4ed8;}
</style>
</head>
<body>
  <div class="card">
    <h2>📨 Send Text Message to Raspberry Pi</h2>
    <form method="POST" action="/send">
      <input type="text" name="message" placeholder="Enter your message" required />
      <button type="submit">Send</button>
    </form>
    <hr>
    <a href="/voice">🎧 Listen to Latest Voice Message</a>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page)


# ---------- WEB → SERVER: Store text in queue ----------
@app.route("/send", methods=["POST"])
def send_message():
    msg = request.form.get("message", "")
    if msg:
        message_queue.append(msg)
        print(f"📩 Stored: {msg}")
    return f"<h3>✅ Message Stored!</h3><p>{msg}</p><a href='/'>Back</a>"


# ---------- PI → GET next text message ----------
@app.route("/get", methods=["GET"])
def get_message():
    if message_queue:
        return jsonify({"message": message_queue[0]})  # send oldest first
    return jsonify({"message": ""})


# ---------- PI confirms message was spoken ----------
@app.route("/confirm_text", methods=["POST"])
def confirm_text():
    if message_queue:
        msg = message_queue.pop(0)  # remove only the one spoken
        print(f"✅ Deleted after speaking: {msg}")
    return "Deleted"


# ---------- PI uploads voice ----------
@app.route("/upload", methods=["POST"])
def upload_voice():
    global latest_voice

    if "file" not in request.files:
        return "No file", 400

    f = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, f.filename)
    f.save(filepath)

    latest_voice = f.filename
    print(f"🎤 New voice message: {f.filename}")
    return "Voice uploaded"


# ---------- Web plays voice ----------
@app.route("/voice")
def play_voice():
    if not latest_voice:
        return "<h3>No voice message yet.</h3><a href='/'>Back</a>"

    return f"""
    <h3>🎧 Latest Voice Message:</h3>
    <audio controls onended="fetch('/confirm_voice', {{method:'POST'}});">
      <source src="/uploads/{latest_voice}" type="audio/wav">
    </audio>
    <p>✅ After playback, message will be deleted.</p>
    <a href="/">Back</a>
    """


# ---------- Delete voice only after playback ----------
@app.route("/confirm_voice", methods=["POST"])
def confirm_voice():
    global latest_voice
    if latest_voice:
        filepath = os.path.join(UPLOAD_FOLDER, latest_voice)
        if os.path.exists(filepath):
            os.remove(filepath)
            print("✅ Voice deleted after playback.")
    latest_voice = None
    return "Voice deleted"


# ---------- Serve audio files ----------
@app.route("/uploads/<filename>")
def serve_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# ---------- Run server ----------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
