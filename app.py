import streamlit as st
# import requests
import speech_recognition as sr
import os
from dotenv import load_dotenv
from openai import OpenAI
# from pydub import AudioSegment
from deep_translator import GoogleTranslator
from gtts import gTTS
from audiorecorder import audiorecorder


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def translate_using_openai(text, source, target):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional translator."
            },
            {
                "role": "user",
                "content": f"Translate the following text from {source} to {target}. Return only the translated text.\n\n{text}"
            }
        ]
    )

    return response.choices[0].message.content.strip()

# def translate_using_api(text, source, target):

#     url = "https://libretranslate.de/translate"

#     payload = {
#         "q": text,
#         "source": source,
#         "target": target,
#         "format": "text"
#     }

#     response = requests.post(url, json=payload)

#     if response.status_code == 200:
#         return response.json()["translatedText"]
#     else:
#         raise Exception("API translation failed")
    
def translate_using_fallback(text, source, target):

    return GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

# Title
st.title("🌍 Language Translation Tool")

# Text input
text = st.text_area("Enter Text")

st.subheader("🎙️ Record Voice")

audio = audiorecorder(
    "Click to record",
    "Click to stop recording"
)

if len(audio) > 0:

    # Save recording
    audio.export("recorded_audio.wav", format="wav")

    recognizer = sr.Recognizer()

    with sr.AudioFile("recorded_audio.wav") as source:
        audio_data = recognizer.record(source)

    try:
        recognized_text = recognizer.recognize_google(audio_data)

        st.success("🎙️ Speech recognized successfully!")

        text = st.text_area(
            "Recognized Text",
            value=recognized_text,
            height=100
        )           

    except Exception as e:
        st.error("Could not recognize speech.")


# Language options
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh"
}

# Source language
source_lang = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

# Target language
target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

# Translate button
if st.button("Translate"):

    if text.strip() == "":
        st.warning("⚠ Please enter some text to translate.")

    elif source_lang == target_lang:
        st.warning("⚠ Source and target languages cannot be the same.")

    else:
        try:
            translated_text = translate_using_openai(
                text,
                source_lang,
                target_lang
            )               
            
            st.success("✅ Translation completed successfully!")
            st.info("🤖 Translation provided by OpenAI API")

        except Exception as e:

            translated_text = translate_using_fallback(
                text,
                languages[source_lang],
                languages[target_lang]
            )

            st.success("✅ Translation completed successfully!")
            st.info("🔄 API unavailable. Used backup translator.")

        st.subheader("Translated Text")

        st.text_area(
            "Output",
            value=translated_text,
            height=120
        )
        # Convert translated text to speech
        tts = gTTS(
            text=translated_text,
            lang=languages[target_lang]
        )
            
        
        # Save audio file
        tts.save("translated_audio.mp3")
        with open("translated_audio.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()
        
        st.subheader("🔊 Listen to Translation")
        
        st.audio(audio_bytes, format="audio/mp3")

        st.download_button(
        label="⬇️ Download Audio",
        data=audio_bytes,
        file_name="translated_audio.mp3",
        mime="audio/mp3"
        )

             