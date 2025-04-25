import streamlit as st
from run_tests import run_tests
from suggest_tests import suggest_tests

# Streamlit setup
st.set_page_config(layout="wide", page_title="Netflix QA Demo")
st.title("🎬 Netflix QA Demo: Automated QA Scripts")

# --- SECTION 1: Run Playwright tests
st.header("▶️ Automated Playwright QA Tests")

if st.button("Run Tests"):
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


# --- SECTION 2: Suggest New Tests
st.header("💡 Suggest QA Tests From a Web Page")

url = st.text_input("Enter a page URL to analyze:")
if st.button("Suggest QA Tests"):
    if url:
        with st.spinner("Scraping page and suggesting tests..."):
            suggested_tests = suggest_tests(url)
            for i, (description, code_snippet) in enumerate(suggested_tests, 1):
                st.markdown(f"**Test {i}: {description}**")
                st.code(code_snippet, language="python")
    else:
        st.warning("Please enter a valid URL before running suggestions!")
