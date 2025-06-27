🎙️ Nova – Voice Assistant in Python
Nova is a simple voice-activated personal assistant built with Python. It can open websites, fetch news, play specific music tracks, and even answer general questions using OpenAI's GPT-4 API.

🚀 Features
✅ Wake word detection ("Nova")
🌐 Opens websites (Google, YouTube, Instagram, LinkedIn)
🎵 Plays predefined music from YouTube
📰 Speaks news headlines from News API
💬 Answers general questions using GPT-4
🗣️ Voice output using pyttsx3 or gTTS + pygame

📁 Project Structure
├── main.py              # Main program with voice recognition and assistant logic
├── client.py            #OpenAI code
├── musiclibrary.py      # Dictionary mapping song names to YouTube links
├── venv/                # Python virtual environment (not included in repo)


🔧 Requirements
Install dependencies using pip:
pip install speechrecognition pyttsx3 pygame gTTS openai requests
Make sure you also have:
Python 3.x
Microphone access enabled
Internet connection for API calls

🔑 Setup
Replace the following API keys with your own:
OpenAI API key in the aiprocess function.
NewsAPI key in the newsapi variable.
Optionally, customize songs in musiclibrary.py

🔑 API Keys
Update main.py:
Replace the OpenAI API key in the aiprocess() function.
Replace the News API key in the newsapi variable.

🧠 Usage
Run the assistant:
python main.py
Say "Nova" to activate, then speak a command such as:
"Open Google"
"Play stealth"
"News"
"What is the capital of India?"

🛠️ Notes
The project uses Google Speech Recognition (via speech_recognition) and may not perform well without internet.
gTTS + pygame are included as an alternative TTS engine (speak_old), but not used by default.
Ensure your mic input is working correctly.

📜 License
Open-source for learning and personal use. Attribution is appreciated.
