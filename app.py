import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

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
    st.session_state.question_number = 1
    st.session_state.start_interview = True
    st.rerun()

# ---------------- AI INTERVIEW ----------------
if "start_interview" in st.session_state and st.session_state.start_interview:
    st.title("AI Interview Round")
    st.write("Role:", st.session_state.role)

    prompt = f"Ask a simple interview question for a {st.session_state.role}. Question number {st.session_state.question_number}."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    question = response.choices[0].message.content
    st.write("### AI Question:")
    st.write(question)
