import streamlit as st
import openai
import os
from streamlit_mic_recorder import mic_recorder
import tempfile
import speech_recognition as sr

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Voice Interview System")

name = st.text_input("Enter your name")
role = st.selectbox("Select Job Role", ["Software Developer", "HR", "Marketing", "Data Analyst"])

question = "Tell me about yourself"

if st.button("Start Interview"):
    st.write("AI Question:", question)

    audio = mic_recorder(start_prompt="🎤 Start Recording", stop_prompt="⏹ Stop Recording", key="recorder")

    if audio:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio['bytes'])
            audio_path = f.name

        r = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = r.record(source)
            answer = r.recognize_google(audio_data)

        st.write("Your Answer:", answer)

        prompt = f"""
        Evaluate this interview answer.

        Question: {question}
        Answer: {answer}

        Give:
        Communication Score
        Confidence Score
        Grammar Score
        Content Score
        Overall Score
        Emotion (Confident/Nervous/Average)
        One improvement tip
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write("AI Feedback:")
        st.write(response.choices[0].message.content)
