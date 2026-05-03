class CoverLetterDocument:
    def __init__(self):
        self.contact_info = ""
        self.body = ""
        self.tone = "Standard"

class CoverLetterBuilder:
    def __init__(self):
        self.document = CoverLetterDocument()

    def add_contact_info(self, name: str, email: str):
        self.document.contact_info = f"{name} | {email}"
        return self

    def add_body(self, content: str):
        self.document.body = content
        return self

    def apply_tone(self, tone: str):
        self.document.tone = tone
        return self

    def build(self) -> CoverLetterDocument:
        return self.document