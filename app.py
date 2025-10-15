import streamlit as st

st.title("🎈 Welcome to My First Streamlit App!")

st.write("This is a *Simple Streamlit Project* — running on GitHub + Streamlit Cloud without any installation!")

name = st.text_input("What is your name?")
if st.button("Say Hello"):
    st.success(f"Hello {name}! 👋 This app is running on Streamlit Cloud.")import streamlit as st

st.title("🎈 Welcome to My First Streamlit App!")

st.write("This is a *Simple Streamlit Project* — running on GitHub + Streamlit Cloud without any installation!")

name = st.text_input("What is your name?")
if st.button("Say Hello"):
    st.success(f"Hello {name}! 👋 This app is running on Streamlit Cloud.")
