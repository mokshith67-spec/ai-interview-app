import streamlit as st
import openai
import speech_recognition as sr
import tempfile
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Voice Interview System")

name = st.text_input("Enter your name")
role = st.selectbox("Select Job Role", ["Software Developer", "HR", "Marketing", "Data Analyst"])

question = "Tell me about yourself"

if st.button("Start Interview"):
    st.write("AI Question:", question)

    audio_file = st.file_uploader("Upload your answer (audio .wav)", type=["wav"])

    if audio_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(audio_file.read())
            audio_path = tmp.name

        r = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
            answer = r.recognize_google(audio)

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
