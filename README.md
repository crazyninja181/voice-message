# 🎙️ Voice Message System

A **voice-controlled messaging system built with Python** that enables users to send and receive messages through voice commands.

The project combines **speech recognition, text-to-speech, audio recording, and client-server communication** to create a hands-free messaging experience.

## 🚀 Features

* 🎤 Voice-controlled commands
* 🎙️ Record voice messages using a microphone
* 📤 Upload voice recordings to a server
* 📥 Receive messages from the server
* 🔊 Convert received text into speech
* 🗣️ Google Speech Recognition for voice input
* 📴 Sphinx fallback for offline speech recognition
* 🌐 HTTP-based client-server communication
* 🔄 Automatic message checking
* 🗑️ Confirmation of received messages

## 🛠️ Tech Stack

| Technology                | Purpose                             |
| ------------------------- | ----------------------------------- |
| Python                    | Core programming language           |
| SpeechRecognition         | Speech-to-text                      |
| Google Speech Recognition | Online voice recognition            |
| CMU Sphinx                | Offline speech recognition fallback |
| pyttsx3                   | Text-to-speech                      |
| SoundDevice               | Audio recording                     |
| NumPy                     | Audio data processing               |
| SciPy                     | WAV/audio processing                |
| Requests                  | HTTP communication                  |
| Playsound                 | Audio playback                      |

## 📂 Project Structure

```text
voice-message/
│
├── pi.py
├── client.py.py
└── README.md
```

### `pi.py`

Main voice-controlled client responsible for:

* Processing voice commands
* Recognizing speech
* Converting text to speech
* Recording voice messages
* Uploading audio
* Receiving messages
* Confirming received messages

### `client.py.py`

A basic audio client that:

1. Records audio from the microphone.
2. Saves it as a WAV file.
3. Uploads the recording to the server.
4. Receives the server response.
5. Plays the returned audio.
6. Removes temporary files.

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/crazyninja181/voice-message.git
cd voice-message
```

### Install dependencies

```bash
pip install requests pyttsx3 SpeechRecognition numpy scipy sounddevice playsound pocketsphinx
```

> Depending on your operating system, additional audio/microphone dependencies may be required.

## ▶️ Usage

Start the main application:

```bash
python pi.py
```

The program starts listening for voice commands.

### Receive a message

Say:

```text
receive audio
```

The application checks the server for a new message and reads the received text aloud.

### Send a message

Say:

```text
send audio
```

The application records your voice and uploads the resulting WAV file to the server.

### Exit

You can say:

```text
stop
```

```text
exit
```

or

```text
quit
```

## 🔄 System Workflow

```text
                 ┌──────────────┐
                 │     User     │
                 └──────┬───────┘
                        │
                        ▼
                🎤 Voice Command
                        │
                        ▼
              Speech Recognition
                        │
               ┌────────┴────────┐
               │                 │
               ▼                 ▼
           SEND AUDIO        RECEIVE AUDIO
               │                 │
               ▼                 ▼
         Record Voice        Check Server
               │                 │
               ▼                 ▼
           WAV File          Get Message
               │                 │
               ▼                 ▼
        Upload to Server     Text-to-Speech
               │                 │
               ▼                 ▼
             Server          🔊 User hears
```

## 🌐 API Communication

The voice client communicates with the backend using HTTP requests.

The main endpoints include:

```text
GET  /get
POST /upload
POST /confirm_text
```

The server address is configured inside `pi.py`.

To connect the project to another backend, update the server configuration:

```python
SERVER_BASE = "YOUR_SERVER_URL"
```

## 🧠 Speech Recognition

The application uses **Google Speech Recognition** with the `en-IN` language configuration.

If online recognition fails, the application attempts to use **CMU Sphinx** as a fallback.

This gives the system basic offline speech-recognition capability.

## 🔊 Text-to-Speech

`pyttsx3` is used to convert text into speech.

This allows the user to interact with the application without constantly looking at a screen.

## 🎯 Applications

The project can serve as a foundation for:

* ♿ Accessibility-focused communication
* 🎙️ Hands-free messaging
* 🥧 Raspberry Pi projects
* 📡 IoT communication
* 🤖 Voice-controlled applications
* 🔊 Audio messaging systems

## 🔮 Future Improvements

* 🔐 User authentication
* 🔒 End-to-end message encryption
* 👥 Multi-user messaging
* 🗄️ Database integration
* 🔔 Real-time notifications
* 📱 Mobile application
* 🌍 Multi-language support
* 🧠 AI-powered message processing
* 📊 Message history
* 🎨 Graphical user interface
* 🛜 Better network-error handling
* 🥧 Raspberry Pi optimization

## 👨‍💻 Author

**crazyninja181**

[GitHub Profile](https://github.com/crazyninja181)

## 📄 License

This project is created for **educational and development purposes**.
