from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_document(content):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 300, chunk_overlap = 50)
    return splitter.split_text(content)