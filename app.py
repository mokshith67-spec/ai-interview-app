import streamlit as st
from ai_engine import analyze_answer, generate_question
from pdf_report import generate_pdf

st.set_page_config(page_title="AI Interview Trainer", layout="centered")

st.title("AI Interview Trainer")

name = st.text_input("Enter Your Name")

interview_type = st.selectbox(
    "Select Interview Type",
    ["HR Interview", "Technical Interview", "Group Discussion"]
)

if st.button("Start Interview"):
    question = generate_question(interview_type)
    st.session_state.question = question

if "question" in st.session_state:
    st.write("### Interview Question:")
    st.write(st.session_state.question)

    answer = st.text_area("Type Your Answer")

    if st.button("Submit Answer"):
        feedback, score = analyze_answer(answer)

        st.write("## Feedback")
        st.write(feedback)

        st.write("## Score:", score, "/ 10")

        generate_pdf(name, st.session_state.question, answer, feedback, score)

        with open("report.pdf", "rb") as file:
            st.download_button("Download Report PDF", file, file_name="Interview_Report.pdf")
