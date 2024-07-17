import os
import streamlit as st
from clarifai.client.model import Model

# Read API key from environment variable
api_key = os.getenv("CodestralPat")

# Function to get prediction from the model
def get_model_prediction(prompt):
    model_url = "https://clarifai.com/mistralai/completion/models/codestral-22b-instruct"
    model = Model(url=model_url, pat=api_key)
    model_prediction = model.predict_by_bytes(prompt.encode(), input_type="text")
    return model_prediction.outputs[0].data.text.raw

# Streamlit interface
st.title("Codestral Goal Creator with Clarifai")
st.write("Exam Data Analysis Example")

prompt = st.text_area("Enter your prompt:", "Generate 10 specific, industry-relevant goals for exam data analysis using Python and Pandas. Each goal should include a brief name and a one-sentence description of the task or skill. Focus on practical applications in educational assessment, covering areas such as data processing, statistical analysis, visualization, and advanced techniques.", height=70)

if st.button("Create Goals Using Codestral"):
    prediction = get_model_prediction(prompt)
    st.write("Model Prediction:")
    st.write(prediction)
