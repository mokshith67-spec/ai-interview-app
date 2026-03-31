import streamlit as st
import openai
import os
from streamlit_mic_recorder import mic_recorder
import tempfile

openai.api_key = os.getenv("OPENAI_API_KEY")

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login - AI Interview System")
    username = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Enter login details")

    st.stop()

# ---------------- INTERVIEW ----------------
st.title("AI Voice Interview System")

questions = {
    "Software Developer": [
        "Tell me about yourself",
        "What is OOP?",
        "Explain your project"
    ],
    "HR": [
        "Tell me about yourself",
        "What are your strengths?",
        "How do you handle stress?"
    ],
    "Marketing": [
        "Tell me about yourself",
        "How will you sell a product?",
        "What is digital marketing?"
    ],
    "Data Analyst": [
        "Tell me about yourself",
        "What is Excel?",
        "What is data cleaning?"
    ]
}

name = st.text_input("Enter your name")
role = st.selectbox("Select Job Role", list(questions.keys()))

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if st.button("Start Interview"):
    st.session_state.question_index = 0

if st.session_state.question_index < len(questions[role]):
    question = questions[role][st.session_state.question_index]
    st.write("### AI Question:", question)

    audio = mic_recorder(start_prompt="🎤 Start Recording", stop_prompt="⏹ Stop Recording", key=str(st.session_state.question_index))

    if audio:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio['bytes'])
            audio_path = f.name

        # Speech to text using Whisper
        audio_file = open(audio_path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        answer = transcript["text"]

        st.write("Your Answer:", answer)

        # AI Feedback
        prompt = f"""
        Evaluate this interview answer.

        Question: {question}
        Answer: {answer}

        Give:
        Communication Score (out of 10)
        Confidence Score (out of 10)
        Grammar Score (out of 10)
        Content Score (out of 10)
        Overall Score (out of 10)
        Emotion (Confident/Nervous/Average)
        One improvement tip
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        feedback = response.choices[0].message.content
        st.write("### AI Feedback:")
        st.write(feedback)

        if st.button("Next Question"):
            st.session_state.question_index += 1
            st.rerun()

else:
    st.write("## Interview Finished")
    st.write("Thank you for attending the AI Interview")
