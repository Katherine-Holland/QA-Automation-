import streamlit as st
from run_tests import run_tests

st.set_page_config(layout="wide", page_title="Netflix QA Demo")
st.title("🎬 Netflix Login QA Test")

if st.button("▶️ Run Script"):
    with st.spinner("Running tests..."):
        results = run_tests()

    st.subheader("✅ Test Results")
    for name, result in results:
        st.markdown(f"- **{name}**: {result}")

    st.subheader("📜 Script Summary")
    with st.expander("Show Playwright Test Code"):
        with open("run_tests.py", "r") as f:
            st.code(f.read(), language="python")
