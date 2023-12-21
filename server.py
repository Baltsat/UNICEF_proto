import streamlit as st
import os

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("uploaded_files", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except:
        return False

st.title("UNICEF GenAI Document Upload and Interaction")

st.header("Document Upload")
uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt'])
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        st.success("File Uploaded Successfully: " + uploaded_file.name)
    else:
        st.error("Error in Uploading File")

st.header("Interact with AI Model")
user_query = st.text_input("Enter your query:")
if st.button("Submit"):
    # AI Model Interaction Logic Goes Here
    # This is a placeholder for the integration with the AI model.
    # The actual implementation would depend on the specific requirements and the AI model's API.
    st.write("Response from AI model for the query: " + user_query)

st.header("Uploaded Documents")
# Display list of uploaded files
if os.path.exists("uploaded_files"):
    files = os.listdir("uploaded_files")
    for file in files:
        st.text(file)

