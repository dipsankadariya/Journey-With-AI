import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash",temperature=0.3)

st.header("LangChain Google GenAI Research bot")
user_input = st.text_input("Enter your research question here:")


if st.button("summarize"):
    if not user_input.strip():
        st.warning("Enter a research question first.")
    else:
        with st.spinner("Generating summary..."):
            result = model.invoke(user_input)
        st.write(result.content[0]["text"])
