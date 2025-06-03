# Jarvis Voice Assistant

Jarvis is a simple voice assistant written in Python. It uses speech
recognition to listen for voice commands and `pyttsx3` to speak
responses. The assistant can play YouTube videos, tell the current
time, perform Google searches, read short Wikipedia summaries and tell
jokes.

## Installation

1. Install Python 3.7 or higher.
2. Install the required packages:
   ```bash
   pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes
   ```
3. Ensure a working microphone is connected.

## Usage

Run the main script from the repository root:

```bash
python jarvis.py/main.py
```

Jarvis will greet you and start listening for commands. Speak
"Jarvis" followed by one of the supported commands.

## Function Reference

### `talk(text)`
Uses `pyttsx3` to speak the provided text aloud.

### `take_command()`
Listens to the microphone and returns the recognized command in
lowercase. The word "Jarvis" is removed from the returned text.

### `wishme()`
Speaks a greeting based on the current time of day (morning,
afternoon or evening).

### `run_jarvis()`
Parses the command returned by `take_command()` and performs one of
the following actions:

- **play** `<song>` – plays the song on YouTube
- **time** – announces the current time
- **search** `<query>` – performs a Google search and attempts to read a short summary
- **who/what/where** `<topic>` – reads a brief Wikipedia summary about the topic
- **funny/joke/sarcastic/silly/bored** – tells a random joke
- anything else – asks the user to repeat the command

## Voice Commands
The assistant understands commands that contain the keywords listed
above. Prefix your statement with "Jarvis" so the assistant knows to
respond.

## Documentation
Additional documentation is available in the `docs/` directory.
