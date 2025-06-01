import streamlit as st

def input_api_key():
    key = st.text_input('Enter Gemini API token:', type='password')
    if key and len(key) > 10:
        st.success('API key accepted.')
        return key
    else:
        st.warning('Please enter a valid API key.')
        return None
