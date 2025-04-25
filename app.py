import streamlit as st
from run_tests import run_tests

st.set_page_config(layout="wide", page_title="Playwright QA Demo")
st.title("🔐 Login Flow QA Test")

if st.button("▶️ Run Script"):
    with st.spinner("Running Playwright tests..."):
        results = run_tests()

    st.subheader("✅ Test Results")
    for name, result in results:
        status = "✅ Passed" if result else "❌ Failed - Manual review needed"
        st.markdown(f"- **{name}**: {status}")

    st.subheader("📜 Script Summary")
    with st.expander("Show Playwright Test Code"):
        with open("run_tests.py", "r") as f:
            st.code(f.read(), language="python")
