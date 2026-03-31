import streamlit as st

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
        st.write("### Question:")
        st.write(q_list[q_index])

        if st.button("Next Question"):
            st.session_state.q_index += 1
            st.rerun()
    else:
        st.write("Interview Finished")
