import streamlit as st
import requests

# API URL
API_URL = "http://127.0.0.1:8000/chain/invoke"

# List of languages for translation
languages = ["English", "Arabic", "French", "German", "Italian", "Japanese", 
             "Portuguese", "Russian", "Spanish", "Turkish"]


st.title("Language Translation App")

# Input field for text
input_text = st.text_area("Enter the text you want to translate:")

# Menu for selecting target language
target_language = st.selectbox("Select the target language: ", languages)

# Translation Button
if st.button("Translate"):
    if input_text:
        # Payload for API request
        payload = {
            "input": {
                "language": target_language,
                "text": input_text
            }
        }

        # POST request to FastAPI backend
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            # Display translated text
            translated_text = response.json().get("output", "Error: Could not"
                                                  " fetch the translation.")
            st.write(f"**Translated Text in {target_language}:**")
            st.write(translated_text)
        else:
            st.error("Error: Could not connect to the translation API.")
    else:
        st.warning("Please enter some text to translate.")
