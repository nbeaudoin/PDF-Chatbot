#!pip install -r requirements.txt
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
    
def get_text_chunks(raw_text):


def main():
    load_dotenv()   

    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents")
    
    with st.sidebar:
        st.subheader("Add your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get PDF text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store







if __name__ == '__main__':
    main()