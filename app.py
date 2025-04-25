import streamlit as st
from utils.suggest_tests import suggest_tests

# Setup
st.set_page_config(layout="wide", page_title="🐺 QA Helper")
st.title("🌟🐺 Smart QA Helper - Small pup, big future!🐾🌟")

# URL input
url = st.text_input("Enter a website URL to suggest tests:")

if url:
    with st.spinner("🐾 Sniffing around the page..."):
        try:
            sections, starter_script = suggest_tests(url)

            st.subheader("🐺 Suggested Tests")
            for section, tests in sections.items():
                with st.expander(f"📂 {section}"):
                    for test_title, test_description, snippet in tests:
                        st.markdown(f"**{test_title}**: {test_description}")
                        st.code(snippet, language="python")

            st.subheader("📜 Starter Playwright Test Script Example")
            st.code(starter_script, language="python")

            st.success("🌟 Copy the starter code above and extend it into your Playwright suite!")

        except Exception as e:
            st.error(f"❌ Error analyzing page: {e}")
else:
    st.info("👀 Enter a URL above and I'll help you create tests!")