from typing import Optional, List
from src.models import Resume
from repositories.resume_repository import ResumeRepository
from uuid import uuid4

class ResumeService:
    """Service for resume business operations."""
    
    def __init__(self, repository: ResumeRepository):
        self.repository = repository
    
    def create_resume(self, text: str) -> Resume:
        """Create a new resume."""
        if not text or len(text.strip()) == 0:
            raise ValueError("Resume text cannot be empty")
        
        resume = Resume(text=text)
        if not resume.validate_length():
            raise ValueError(f"Resume exceeds {resume.max_limit} characters")
        
        resume.id = str(uuid4())
        self.repository.save(resume)
        return resume
    
    def get_resume(self, resume_id: str) -> Optional[Resume]:
        """Retrieve a resume by ID."""
        return self.repository.find_by_id(resume_id)
    
    def get_all_resumes(self) -> List[Resume]:
        """Retrieve all resumes."""
        return self.repository.find_all()
    
    def update_resume(self, resume_id: str, text: str) -> Resume:
        """Update an existing resume."""
        resume = self.repository.find_by_id(resume_id)
        if not resume:
            raise ValueError(f"Resume {resume_id} not found")
        
        if not text or len(text.strip()) == 0:
            raise ValueError("Resume text cannot be empty")
        
        if len(text) > resume.max_limit:
            raise ValueError(f"Resume exceeds {resume.max_limit} characters")
        
        resume.text = text
        self.repository.save(resume)
        return resume
    
    def delete_resume(self, resume_id: str) -> None:
        """Delete a resume."""
        self.repository.delete(resume_id)