from app.document_loader import load_document
from app.text_splitter import split_document

def test_split_document():
    content = load_document("container_manual.txt")
    chunks = split_document(content)
    print("\nNumof of chunks",len(chunks))

    for index,chunk in enumerate(chunks, start=1):
        print(f"\nchunc:{index}")
        print(chunk)
    assert len(chunks)>1