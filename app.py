import streamlit as st
import json
from main import run_pipeline

st.set_page_config(page_title="AI Platform Pipeline", layout="wide")

st.title("🚀 AI Platform Pipeline")

user_input = st.text_input("Enter your app idea:")

if st.button("Generate"):
    if user_input.strip():
        with st.spinner("Processing..."):
            output = run_pipeline(user_input)

        st.subheader("Result")

        # 🔹 If output is None
        if output is None:
            st.error("Pipeline returned no output")
        
        else:
            # 🔹 If dict
            if isinstance(output, dict):
                if "ERROR" in output:
                    st.error(output["ERROR"])
                else:
                    st.json(output)

            # 🔹 If string
            elif isinstance(output, str):
                try:
                    parsed = json.loads(output)
                    st.json(parsed)
                except:
                    st.error("Invalid JSON format")
                    st.text(output)

            # 🔹 Unexpected type
            else:
                st.warning("Unexpected output format")
                st.write(output)

    else:
        st.warning("Please enter a valid input")