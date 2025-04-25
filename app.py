# app.py

import streamlit as st
from utils.suggest_tests import suggest_tests

st.set_page_config(layout="wide", page_title= "🌟🐺 QA Helper - Small pup, big future!🐾🌟")
st.title("Smart QA Test Suggestion + Playwright Starter")

url = st.text_input("Enter a website URL to suggest tests:")

if url:
    with st.spinner("Analyzing page..."):
        suggestions, starter_script = suggest_tests(url)

    st.subheader("Suggested Tests")
    for suggestion in suggestions:
        st.markdown(f"- {suggestion}")

    st.subheader("📜 Playwright Test Script Example")
    st.code(starter_script, language="python")

    st.success("Copy the code above and paste into your test suite!")

    # (optional future button to 'Run' directly - manual for now)
