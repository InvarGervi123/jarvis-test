# Jarvis Test

This is a basic personal assistant project inspired by "Jarvis" from the Marvel universe. It was originally created based on a [YouTube tutorial](https://www.youtube.com/watch?v=pTDTIkLRQKQ&ab_channel=%D0%A5%D0%B0%D1%83%D0%B4%D0%B8%D0%A5%D0%BE%E2%84%A2-%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%BE%D0%BC%D0%B8%D1%80%D0%B5IT%21) by **Howdy Ho™ – Просто о мире IT!**, and has been further improved using both **AI assistance** and manual adjustments.

The last time this code was written and modified was on **09/08/2023**.

---

## 🧠 What This Project Does

This assistant listens to your voice and executes basic commands based on speech recognition. It replies using text-to-speech technology and is capable of:

* Greeting the user
* Recognizing basic commands
* Responding vocally using a TTS engine

---

## 🛠️ Requirements

To run this project, you'll need:

* **Python 3.7+**
* **Packages**:

  ```bash
  pip install SpeechRecognition
  pip install pyttsx3
  pip install pyaudio  # May require additional setup depending on OS
  ```

> If you're using Linux or having trouble with PyAudio, try:
>
> ```bash
> sudo apt install python3-pyaudio
> ```

---

## 📁 File Overview

* `main.py` – The core logic of the assistant. It handles voice input, response generation, and command handling.
* `voice.py` *(if exists)* – Likely a helper file managing speech input/output functions.
* `requirements.txt` – (You can create one if it doesn't exist yet to simplify installation)

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/InvarGervi123/jarvis-test
   cd jarvis-test
   ```

2. Install the required packages (as shown above).

3. Run the assistant:

   ```bash
   python main.py
   ```

> Make sure your microphone is connected and accessible by Python.

---

## 🧠 Improvements

This project was not only based on the original video but was also:

* Modified manually to clean up and improve structure
* Enhanced with AI help for logic, clarity, and performance
* Tested and reviewed for basic functionality

---

## 👤 Author

**Invar Gervi** – Passionate about AI, software development, and voice interfaces.

---

## 🧠 Ideas for the Future

* Add GUI using Tkinter or PyQt
* Add support for additional commands like weather updates or opening websites
* Add memory/state so it can remember previous interactions

Feel free to fork, explore, and expand!
