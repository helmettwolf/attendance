import streamlit as st
st.title("Attendance Tracker: ")
tt=st.file_uploader("Upload Timetable :" \
"", type=["png", "jpg", "jpeg"])
if tt:
    st.image(tt)
from dotenv import load_dotenv
import os
load_dotenv()
api=os.getenv("GOOGLE_API_KEY")