from typing import Optional, List
from src.models import CoverLetter
from repositories.cover_letter_repository import CoverLetterRepository
from uuid import uuid4

class CoverLetterService:
    """Service for cover letter business operations."""
    
    def __init__(self, repository: CoverLetterRepository):
        self.repository = repository
    
    def create_cover_letter(self, content: str, status: str = "draft", 
                          template_version: str = "1.0") -> CoverLetter:
        """Create a new cover letter."""
        if not content or len(content.strip()) == 0:
            raise ValueError("Cover letter content cannot be empty")
        
        cover_letter = CoverLetter(
            id=str(uuid4()),
            content=content,
            status=status,
            template_version=template_version
        )
        self.repository.save(cover_letter)
        return cover_letter
    
    def get_cover_letter(self, letter_id: str) -> Optional[CoverLetter]:
        """Retrieve a cover letter by ID."""
        return self.repository.find_by_id(letter_id)
    
    def get_all_cover_letters(self) -> List[CoverLetter]:
        """Retrieve all cover letters."""
        return self.repository.find_all()
    
    def update_cover_letter(self, letter_id: str, content: str) -> CoverLetter:
        """Update an existing cover letter."""
        cover_letter = self.repository.find_by_id(letter_id)
        if not cover_letter:
            raise ValueError(f"Cover letter {letter_id} not found")
        
        if not content or len(content.strip()) == 0:
            raise ValueError("Cover letter content cannot be empty")
        
        cover_letter.update_content(content)
        self.repository.save(cover_letter)
        return cover_letter
    
    def delete_cover_letter(self, letter_id: str) -> None:
        """Delete a cover letter."""
        self.repository.delete(letter_id)
    
    def finalize_cover_letter(self, letter_id: str) -> CoverLetter:
        """Business logic: Mark cover letter as finalized."""
        cover_letter = self.repository.find_by_id(letter_id)
        if not cover_letter:
            raise ValueError(f"Cover letter {letter_id} not found")
        
        if cover_letter.status == "finalized":
            raise ValueError("Cover letter is already finalized")
        
        cover_letter.status = "finalized"
        self.repository.save(cover_letter)
        return cover_letter