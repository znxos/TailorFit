class Document:
    pass

class Resume(Document):
    def __init__(self):
        self.type = "Resume"

class CoverLetter(Document):
    def __init__(self):
        self.type = "CoverLetter"

class DocumentFactory:
    @staticmethod
    def create_document(doc_type: str) -> Document:
        if doc_type.lower() == 'resume':
            return Resume()
        elif doc_type.lower() == 'coverletter':
            return CoverLetter()
        raise ValueError(f"Unknown document type: {doc_type}")