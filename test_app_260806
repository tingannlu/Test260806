import streamlit as st

st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="🚀",
)

st.title("🚀 My First Streamlit App")

st.write("This app is running for free using GitHub and Streamlit Community Cloud.")

name = st.text_input("What is your name?")

if name:
    st.success(f"Hello, {name}!")

number = st.slider(
    "Choose a number",
    min_value=1,
    max_value=100,
    value=50,
)

st.write(f"You selected: **{number}**")

