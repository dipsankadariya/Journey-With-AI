import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.3
)


st.header("LangChain Google GenAI Research Bot")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)


prompt_template = load_prompt("template.json")

if st.button("Summarize"):

    chain = prompt_template | model

    with st.spinner("Researching and summarizing the paper..."):
        result = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })

    st.subheader("Summary")
    st.write(result.content[0]["text"])