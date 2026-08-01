import streamlit as st
from dotenv import load_dotenv
from google import genai
from PIL import Image
from datetime import date
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

    choice=st.radio("Select your group", ["GRP-A", "GRP-B"])
    filter_data=[]
    for sub in data:
        if "GRP-" in sub["subject"]:
            if choice in sub["subject"]:
                filter_data.append(sub)
        else:
            filter_data.append(sub)
    st.write(filter_data)
    count={}
    for sub in filter_data:
        if sub["subject"] in count:
            count[sub["subject"]]+=1
        else:
            count[sub["subject"]]=1
    st.write(count)
    today=date.today()
    lastdate=st.date_input("Last Date of semester (Date before ESA)")
    difference=((lastdate - today).days)//7
    st.write(difference)