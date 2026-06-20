# 🌍 AI-Powered Language Translation Tool

An AI-powered multilingual language translation application built using **Python** and **Streamlit**. The project supports text translation, voice input, speech recognition, text-to-speech conversion, and audio download with secure OpenAI API integration and a backup translation mechanism.

---

## 🚀 Features

* 🌐 Translate text between multiple languages.
* 🎙️ Voice input using microphone recording.
* 🗣️ Speech-to-text conversion.
* 🤖 OpenAI API integration with secure `.env` configuration.
* 🔄 Automatic fallback to Google Translator when OpenAI API is unavailable.
* 🔊 Text-to-speech conversion using gTTS.
* 🎧 Audio playback inside the application.
* ⬇️ Download translated audio as MP3.
* 🎨 User-friendly Streamlit interface.
* ⚡ Error handling and fault-tolerant architecture.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* OpenAI API
* SpeechRecognition
* deep-translator
* gTTS
* streamlit-audiorecorder
* python-dotenv

---

## 📂 Project Structure

```text
CodeAlpha_Language_Translator
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── recorded_audio.wav
└── translated_audio.mp3
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/TanishaKrishnamurthi/CodeAlpha_Language_Translator.git
```

Move into the project directory:

```bash
cd CodeAlpha_Language_Translator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🏗️ Architecture

```text
Voice Input
     ↓
Speech Recognition
     ↓
Recognized Text
     ↓
OpenAI API (Primary Translator)
     ↓
Failure?
 ↙             ↘
No               Yes
↓                 ↓
Translation    Google Translator
     ↓
Translated Text
     ↓
gTTS
     ↓
Audio Output
     ↓
Download MP3
```

---

## 📸 Demo

* Text → Text Translation
* Voice → Text Translation
* Text → Speech Conversion
* Audio Playback
* Audio Download

---

## 📌 Internship Project

This project was developed as **Task 1** of the **CodeAlpha Artificial Intelligence Internship**.

---

## 👩‍💻 Author

**Tanisha Krishnamurthi**

* GitHub: https://github.com/TanishaKrishnamurthi
* LinkedIn: [www.linkedin.com/in/tanishka-krishnamurthi-kairamkonda](http://www.linkedin.com/in/tanishka-krishnamurthi-kairamkonda)

---

⭐ If you found this project useful, consider giving it a star!
