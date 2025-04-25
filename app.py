import streamlit as st
from run_tests import run_tests

# Streamlit setup
st.set_page_config(layout="wide", page_title="Netflix QA Demo")
st.title("🎬 Netflix Login QA Test")

# Run the full test suite
if st.button("▶️ Run Script"):
    with st.spinner("Running Playwright tests..."):
        results = run_tests()

    # Display results
    st.subheader("✅ Test Results")
    for name, result in results:
        status = "✅ Passed" if result else "❌ Failed - Manual review needed"
        st.markdown(f"- **{name}**: {status}")

    # Show the script as a reference
    st.subheader("📜 Script Summary")
    with st.expander("Show Playwright Test Code"):
        with open("run_tests.py", "r") as f:
            st.code(f.read(), language="python")
