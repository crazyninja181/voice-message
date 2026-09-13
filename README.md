# 🎙️ Voice Message System

A **voice-controlled messaging system built with Python** that allows users to send and receive messages using their voice.

The application combines **speech recognition, text-to-speech, audio recording, and HTTP-based server communication** to create a hands-free messaging experience.

## ✨ Features

* 🎤 Voice-controlled interface
* 🎙️ Record voice messages directly from the microphone
* 📤 Upload recorded voice messages to a server
* 📥 Receive messages from the server
* 🔊 Read received text messages aloud
* 🗣️ Speech-to-text using Google Speech Recognition
* 📴 Offline speech recognition fallback using Sphinx
* 🚪 Voice commands to exit the application
* 🌐 Client-server communication using HTTP requests
* 🔄 Automatic message checking

## 🛠️ Technologies Used

* **Python**
* **SpeechRecognition**
* **pyttsx3**
* **NumPy**
* **SciPy**
* **SoundDevice**
* **Requests**
* **Playsound**
* **WAV Audio Processing**

## 📂 Project Structure

```text
voice-message/
│
├── pi.py
├── client.py.py
└── README.md
```

### `pi.py`

The main voice-controlled messaging client.

It handles:

* Voice commands
* Speech recognition
* Text-to-speech
* Receiving messages
* Recording voice messages
* Uploading audio to the server
* Confirming received messages

### `client.py.py`

A simpler audio client that:

1. Records audio for a fixed duration.
2. Uploads the WAV file to a server.
3. Receives the server response.
4. Plays the returned audio.
5. Deletes temporary audio files.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/crazyninja181/voice-message.git
cd voice-message
```

### 2. Install dependencies

```bash
pip install requests pyttsx3 SpeechRecognition numpy scipy sounddevice playsound pocketsphinx
```

Depending on your system, additional microphone/audio dependencies may be required.

## ▶️ Running the Voice Messaging System

Run the main program:

```bash
python pi.py
```

After starting, the application provides voice instructions and waits for a command.

## 🎤 Voice Commands

### Receive a message

Say:

```text
receive audio
```

The application checks the server for new messages. When a message is received, it is spoken aloud using text-to-speech.

### Send a voice message

Say:

```text
send audio
```

The application records your voice, saves it as a WAV file, and uploads the recording to the server.

### Exit

You can say:

```text
stop
```

or:

```text
exit
```

or:

```text
quit
```

## 🔄 How It Works

```text
                    USER
                      │
                      ▼
              🎤 Voice Command
                      │
                      ▼
             Speech Recognition
                      │
            ┌─────────┴─────────┐
            │                   │
         RECEIVE              SEND
            │                   │
            ▼                   ▼
      Check Server         Record Voice
            │                   │
            ▼                   ▼
      Receive Message       WAV File
            │                   │
            ▼                   ▼
       Text-to-Speech       Upload
            │                   │
            ▼                   ▼
       🔊 User hears        Server
         message            receives it
```

## 🌐 Server Communication

The application communicates with a backend server through HTTP endpoints.

The main client uses endpoints for:

```text
GET   /get
POST  /upload
POST  /confirm_text
```

The server URL is configured in `pi.py`.

Before using the project with your own backend, update:

```python
SERVER_BASE = "YOUR_SERVER_URL"
```

and configure the corresponding API endpoints.

## 🗣️ Speech Recognition

The system primarily uses **Google Speech Recognition** with the `en-IN` language setting.

If the Google recognition request fails, the application attempts to use **Sphinx** as an offline fallback.

This provides basic voice recognition even when the online recognition service is unavailable.

## 🔊 Text-to-Speech

The project uses **pyttsx3** to convert text into speech.

This allows the application to communicate with the user without requiring a graphical interface.

For example:

```text
Voice controlled message system activated.

Say receive audio to listen messages.

Say send audio to record voice.

Say stop or exit to quit.
```

## 🎯 Use Cases

This project can be used as a foundation for:

* ♿ Accessibility-focused communication
* 🎙️ Hands-free messaging
* 🥧 Raspberry Pi voice projects
* 🌐 Client-server communication
* 🤖 Voice-controlled applications
* 📡 IoT communication systems
* 🔊 Audio messaging platforms

## 🚀 Future Improvements

* 🔐 Add user authentication
* 🔒 Encrypt voice messages
* 👥 Support multiple users
* 💬 Support text and voice messages
* 🗄️ Add database storage
* 🔔 Real-time message notifications
* 📱 Build a mobile application
* 🌍 Add multilingual speech recognition
* 🧠 Add AI-based message processing
* 📊 Add message history
* 🛜 Improve handling of network failures
* 🎨 Add a graphical interface
* 🥧 Optimize specifically for Raspberry Pi

## 👨‍💻 Author

**crazyninja181**

GitHub:
https://github.com/crazyninja181

## 📄 License

This project is intended for educational and development purposes.
