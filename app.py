import json
import os 
import sys
import boto3
import streamlit as st

from langchain_aws import BedrockEmbeddings
# from langchain_community.llms import Bedrock

from langchain.prompts import PromptTemplate
# from langchain.chains import RetrievalQA

from langchain_community.vectorstores import FAISS

from QASystem.ingestion import data_ingestion,get_vector_store

from QASystem.retrievalandgeneration import get_llm, get_response_llm

bedrock=boto3.client(service_name="bedrock-runtime")
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0",client=bedrock)

def main():
    st.set_page_config(page_title="QA with Doc", page_icon="📄", layout="wide")
    st.title("📚 QA with Documents using LangChain + AWS Bedrock")

    # Main question input
    st.markdown("### ❓ Ask a Question")
    user_question = st.text_input("Enter your question about the PDF documents:")

    # Button & Answer in main area (below the question bar)
    if st.button("Run Query with LLaMA 3"):
        if not user_question.strip():
            st.warning("⚠️ Please enter a question first!")
        else:
            with st.spinner("Generating response..."):
                faiss_index = FAISS.load_local(
                    "faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True
                )
                llm = get_llm()
                response = get_response_llm(llm, faiss_index, user_question)
                st.write("### 📌 Answer")
                st.success(response)

    # Sidebar for actions (only vector store here now)
    with st.sidebar:
        st.header("⚙️ Vector Store & Model Controls")

        # Vector Store Section
        st.subheader("🔄 Vector Store")
        if st.button("Update / Create Vectors", use_container_width=True):
            with st.spinner("Processing documents..."):
                docs = data_ingestion()
                get_vector_store(docs)
                st.success("✅ Vector store updated!")
                
if __name__=="__main__":
    main()
    