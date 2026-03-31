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

st.subheader("Select Job Role")

role = st.selectbox(
    "Choose role",
    ["Software Developer", "HR", "Marketing", "Data Analyst"]
)

if st.button("Start Interview"):
    st.session_state.role = role
    st.session_state.start_interview = True
    st.rerun()

# ---------------- INTERVIEW START ----------------
if "start_interview" in st.session_state and st.session_state.start_interview:
    st.title("Interview Started")
    st.write("Role:", st.session_state.role)
    st.write("Next step → AI will ask question")
