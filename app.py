import streamlit as st

st.set_page_config(page_title="AI Interview System")

# Login system
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

# After login
st.title("AI Interview Dashboard")
st.write("Welcome:", st.session_state.user)
st.write("Next step → Select Job Role")
