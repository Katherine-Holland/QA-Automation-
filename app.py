# app.py

import streamlit as st
from utils.suggest_tests import suggest_tests

# Setup
st.set_page_config(layout="wide", page_title="🌟🐺 QA Helper - Small pup, big future!🐾🌟")
st.title("Smart QA Test Suggestion + Playwright Starter")

# URL input
url = st.text_input("Enter a website URL to suggest tests:")

if url:
    with st.spinner("🐾 Sniffing around the page..."):
        try:
            suggestions, starter_script = suggest_tests(url)

            st.subheader("🐺 Suggested Tests")
            for suggestion in suggestions:
                st.markdown(f"- {suggestion}")

            st.subheader("📜 Playwright Test Script Example")
            st.code(starter_script, language="python")

            st.success("🌟 Copy the starter code above and extend it into your Playwright suite!")

        except Exception as e:
            st.error(f"❌ Error analyzing page: {e}")
else:
    st.info("👀 Enter a URL above and I'll help you create tests!")
