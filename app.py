import streamlit as st
from dotenv import load_dotenv
from google import genai
from PIL import Image
st.title("Attendance Tracker: ")
tt=st.file_uploader("Upload Timetable :" \
"", type=["png", "jpg", "jpeg"])
import os
load_dotenv()
api=os.getenv("GOOGLE_API_KEY")
if tt:
    st.image(tt)
    client=genai.Client(api_key=api)
    img=Image.open(tt)
    response=client.models.generate_content(model="gemini-flash-latest", contents=[img, "describe the image"])
    st.write(response.text)