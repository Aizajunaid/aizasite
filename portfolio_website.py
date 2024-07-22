import streamlit as st
import google.generativeai as genai
#api_key = st.secrets["GOOGLE_API_KEY"]
#genai.configure(api_key=api_key)
genai.configure(api_key="AIzaSyA2JOVwQCH2_LTI9nLBUKgxq9pBqx8309E")
model =genai.GenerativeModel('gemini-1.5-flash')
 

 
col1, col2 = st.columns(2)
 
with col1:
    st.subheader("Hi :wave:")
    st.title("I am aiza junaid")
 
with col2:
    st.image("images/2.jpeg")
 
st.title(" ")
persona = """
        I am aiza, an accomplished Educator, Youtuber, and Entrepreneur with a deep expertise in Computer Vision, Generative AI, and Data Analytics. Currently,i am learning online. 
I hold a Bachelor's degree in software engineering from Mirpur University of Science & technology, Pakistan, where I developed a strong foundation in Computer Vision. As an expert in Generative AI, I have made significant contributions to both educational and industrial applications. I specialize in Prompt Engineering, catering to the needs of educators, marketers, and industry professionals.
My technical prowess extends to web frameworks such as React, NextJS, and Javascript, and I am proficient in multiple programming languages, including C, C#, Java, Python, and Javascript. I have created advanced AI curriculums for the 3-year DAE program in AI for the Pakistani education system, and I have been involved in developing board papers for various IT courses in Pakistan. Additionally, I have developed frameworks for the federal board and won multiple international online hackathons, including lablab.ai and Ultrahack Online Hackathon.
Apart from my professional achievements, I am a hosewife and mother of two, i love cooking . I enjoy sports like badminton and cricket and prioritize my fitness through regular walks and exercises. Traveling is another passion of mine, allowing me to explore new places and cultures.
For collaborations, educational content, or industry projects, feel free to reach out to me via
Aiza's Email: Aizajunaid189@gmail.com
Aiza's Instagram: https://www.instagram.com/aiza.9?utm_source=qr&igsh=MXNuODF0NmQwMms2ag==
Aiza's Github :https://github.com/Aizajunaid
        """
st.title("aiza's AI Bot")


user_question=st.text_input("Ask anything about me")
if st.button("ASK❓", use_container_width=400):
    prompt = persona + "here is the question the user asked"+user_question
    response = model.generate_content(prompt)
    st.write(response.text)
 
st.title(" ")
 
col1, col2 = st.columns(2)
with col1:
    st.subheader("Aiza junaid")
    st.write("Best channel for toddlers")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")
 
 
st.title(" ")
 
st.title("My Setup")
st.image("images/setup3.jpeg")

st.write("")
st.title("My skills")
st.slider("programming",0,100,70)
st.slider("Teaching",0,100,85)
st.slider("Robotics",0,100,75)

st.write("")
st.title("Gallery")

col1, col2, col3 =st.columns(3)

with col1:
    st.image("images/1.jpeg")
    st.image("images/3.jpeg")
    st.image("images/4.jpeg")
with col2:
  st.image("images/5.jpeg")
  st.image("images/6.jpeg")
  st.image("images/7.jpeg")
 
with col3:
   st.image("images/2.jpeg")
   st.image("images/3.jpeg")
   st.image("images/6.jpeg")

st.write("")
st.subheader("CONTACT")
st.title("For any queries,please contact me at")
st.write("Aizajunaid189@gmail.com")


