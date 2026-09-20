from app.document_loader import load_document

def test_load_document():
    content = load_document("container_manual.txt")
    print("\nDocument content:")
    print(content)

    assert content  is not None
    assert len(content)>0