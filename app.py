# Import necessary libraries
import streamlit as st
import json
import helper,pii_entries_validation,pii_entries_detection
import warnings
warnings.filterwarnings("ignore")

model_name = 'gpt-3.5-turbo'
temperature = 0.0

# Streamlit App
def main():
    st.title("PII Detection App")
    st.write("This app detects personally identifiable information (PII) in a given text.")

    openai_api_key = st.text_input("Enter your OpenAI API Key:")

    text_input = st.text_area("Enter the text for PII detection:")

    if st.button("Detect PII"):
        chat_model = helper.get_chat_model(openai_api_key,model_name,temperature,max_retries=5)
        pii_entries = pii_entries_detection.get_pii_entries(chat_model,text_input)

        st.subheader("PII Detected:")
        st.json(json.dumps(pii_entries))
        
        pii_validation = pii_entries_validation.get_pii_entries_validation(chat_model,pii_entries)

        st.subheader("PII validation:")
        st.json(json.dumps(pii_validation))
            
# Run the Streamlit app
if __name__ == "__main__":
    main()
