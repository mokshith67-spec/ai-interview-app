import streamlit as st
from streamlit_mic_recorder import mic_recorder
from openai import OpenAI
import os

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Interview System")

# ---------------- LOGIN ----------------
if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.title("AI Interview Login")

    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if email and password:
            st.session_state.user = email
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Enter email and password")

    st.stop()

# ---------------- DASHBOARD ----------------
st.title("AI Interview Dashboard")
st.write("Welcome:", st.session_state.user)

role = st.selectbox(
    "Select Job Role",
    ["Software Developer", "HR", "Marketing", "Data Analyst"]
)

if st.button("Start Interview"):
    st.session_state.role = role
    st.session_state.q_index = 0
    st.session_state.start_interview = True
    st.rerun()

# ---------------- QUESTIONS ----------------
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

# ---------------- INTERVIEW ----------------
if "start_interview" in st.session_state and st.session_state.start_interview:
    st.title("Interview Round")
    st.write("Role:", st.session_state.role)

    q_list = questions[st.session_state.role]
    q_index = st.session_state.q_index

    if q_index < len(q_list):
        question = q_list[q_index]
        st.write("### Question:")
        st.write(question)

        # Instead of Whisper, user types answer (fallback)
        answer = st.text_area("Type your answer (or paste voice-to-text)")

        if st.button("Get AI Feedback"):
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

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            feedback = response.choices[0].message.content
            st.write("### AI Feedback:")
            st.write(feedback)

        if st.button("Next Question"):
            st.session_state.q_index += 1
            st.rerun()

    else:
        st.write("## Interview Finished")
        st.write("You have completed the interview.")
