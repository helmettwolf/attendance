import streamlit as st
from dotenv import load_dotenv
from google import genai
from PIL import Image
import json
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
    prompt = "Extract this timetable as JSON. For each class, include: week, day, period, subject. Return ONLY valid JSON, no explanation, no markdown formatting."
    response=client.models.generate_content(model="gemini-flash-lite-latest", contents=[img, prompt])
    data=json.loads(response.text)
    st.write(data)