from pathlib import Path

def load_document(file_name):
    file_path = Path("knowledgebase")/file_name

    with open(file_path,"r",encoding="utf-8") as file:
        return file.read()