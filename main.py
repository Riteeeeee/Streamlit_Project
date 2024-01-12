from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My vWebpage", page_icon=":tada:", layout="wide" )
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css (file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
lottie_coding =load_lottieurl("https://lottie.host/2822fa6f-41ce-4ad7-8f40-740a56a930dd/WA8Ml4qacn.json")
img_contact_from = Image.open("images/OIP.jpg")
img_lottie_animation = Image.open("images/alexa.jpg")
st.subheader("Hello world! Ritee Sharma here 💁‍♀️💻")
st.title("Ready to rock my role as an Amazon Software Engineering Intern! 🌟")
st.write(" I am passionate about Generative AI. Eager to delve deep into this fascinating field, I am committed to learning and building as much as I can. I love exploring AI tools and can't wait to contribute to the world of artificial intelligence. Let the journey into the realm of Generative AI begin! 🌐💡 #AIEnthusiast")
st.write("[Learn More >](https://github.com/Riteeeeee)")

with st.container():

    st.write("___")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write(
            """
             I am a third-year college student pursuing my B. Tech in Electronics and Communication Engineering at Indian Institute of Information Technology Allahabad.  I started my coding journey since the start of my college and have honed my DSA skills in cpp. I have been actively participating in coding contests on various platforms like leetcode, codechef, codeforces. I am also exploring the development domain and  have build projects using different tech stacks and have also participated in various hackathons. 
            """
        )
        with right_column:
            st.lottie(lottie_coding, height=300, key="coding")

    with st.container():
        st.write("___")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 5))

        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("ECHO (A machine-human interaction)")
            st.write(
                """ In a Hackathon conducted by Headout dated Oct12,2022. I
developed a program which aimed at allowing the user to interact
with the machine (aim is to build a machine model with involvement
or robotics) the program was based on talkback feature.
Additional security features like face verification and otp verification
were also implemented. had the full access of the system and hence
and send mails and set reminders, the program was also capable to
open or install an application, play music, and do normal conversation
with the user.
Some modules like face recognition, pyttsx3 and tkinter was also
used.
Tech Stacks: Python3"""
            )
            st.markdown("[Visit This Website...](https://in.pinterest.com/)")
    with st.container():
        image_column, text_column = st.columns((1, 5))
        with image_column:
            st.image(img_contact_from)
        with text_column:
             st.subheader("Conversational Fashion Outfit Generator powered by GenA")
             st.write(
                """
                Implemented an innovative solution to convert users’ conceptualized
thoughts about clothing into dynamic images. Leveraged artificial
intelligence and generative technologies, specifically employing the
Stable Diffusion Model for highly accurate text-to-image conversion.
Managed images using MySQL, enabling training and fine-tuning.
            """
             )
             st.markdown("[Visit This Website...](https://in.pinterest.com/)")
    with st.container():
        st.write("___")
        st.header("Let's chat! 🚀✨ #GetInTouch")
        st.write("##")
        contact_form = """
                <form action ="https://formsubmit.co/riteesharma53@gmail.com" method="POST">
                     <input type ="hidden" name ="_captcha" value="false" >
                     <input type ="text" name ="name" placeholder="Your name" required>
                     <input type ="email" name ="email" placeholder="Your email" required>
                     <textarea name ="message" placeholder="Your message here" required></textarea>
                     <button type ="submit">Send</button>
                 </form>
                 """

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
                st.empty()



