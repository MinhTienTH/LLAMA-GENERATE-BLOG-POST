import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
import os 


HUGGINGFACEHUB_API_TOKEN = "" # Fill in with your own token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN


def generate_blog_post(style, topic, num_words):
    template = """
    You are a helpful assistant that can help with writing a blog post.

    Style: {style}

    Blog Post Title: {topic}

    Number of words: {num_words}

    Write a blog post on the given topic, in the specified style, with approximately the number of words requested.
    """
    prompt = PromptTemplate(input_variables=["style", "topic", "num_words"], template=template)
    
    llm = HuggingFaceHub(
        repo_id="meta-llama/Llama-2-7b-chat-hf",
        model_kwargs={"temperature": 0.3, "max_new_tokens": 1024}
    )
    
    response = llm(prompt.format(style=style, topic=topic, num_words=num_words))
    return response

st.title("Generative Blog Post Creator")

num_words = st.number_input("Enter number of words", min_value=50, max_value=1000, value=300, step=50)
topic = st.text_input("Enter blog post title", "Data Scientist")
style = st.selectbox("Select writing style", ["Professional", "Casual", "Funny", "Sad", "Motivational"])

if st.button("Generate Blog Post"):
    with st.spinner("Generating blog post..."):
        blog_post = generate_blog_post(style, topic, num_words)
        st.markdown(blog_post)

