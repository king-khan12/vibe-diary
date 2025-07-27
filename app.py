import streamlit as st
from dotenv import load_dotenv
from utils.emotion_analysis import get_sentiment
from utils.gpt_response import generate_reply
from utils.recommendations import get_quote, get_song

load_dotenv()

st.set_page_config(page_title="Vibe Diary 💖", layout="centered")
st.title("📝 Vibe Diary – The Journaling Bot That Feels You")

st.markdown("Talk to me. I’m here to feel with you. ✨")

user_input = st.text_area("Write your journal entry here:")

if st.button("Submit"):
    if not user_input.strip():
        st.warning("Please write something.")
    else:
        mood = get_sentiment(user_input)
        reply = generate_reply(user_input, mood)
        quote = get_quote(mood)
        song = get_song(mood)

        st.subheader("💬 My Response")
        st.write(reply)

        st.subheader("🎵 Song Suggestion")
        st.markdown(song, unsafe_allow_html=True)

        st.subheader("📝 A Quote for You")
        st.info(quote)
