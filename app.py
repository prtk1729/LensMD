import streamlit as st # for UI
from openai import OpenAI
import os
from dotenv import load_dotenv
import base64
from src.helper import *

def encode_image(filepath):
    with open(filepath, "rb") as fp:
        return base64.b64encode( fp.read() ).decode('utf8')

def call_gpt4_vision_for_analysis(filepath, sample_prompt):
    base64_image = encode_image(filepath)

    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": sample_prompt},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64, {base64_image}",
                "detail": "high"
            },
            },
        ],
        }
    ],
    max_tokens=1500,
    )

    print(response.choices[0].message_content)
    return response.choices[0].message_content


def initialise_session_state_variables():
    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None

    if "result" not in st.session_state:
        st.session_state.result = None    
    return

if __name__ == '__main__':
    load_dotenv()
    os.environ['OPENAPI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    client = OpenAI()
    # print("OK")

    initialise_session_state_variables() # can take images from folders/ better prac is take from session_states

    st.title("Upload image for Medical Image Analysis")