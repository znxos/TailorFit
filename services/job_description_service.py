from typing import Optional, List
from src.models import JobDescription
from repositories.job_description_repository import JobDescriptionRepository
from uuid import uuid4

class JobDescriptionService:
    """Service for job description business operations."""
    
    def __init__(self, repository: JobDescriptionRepository):
        self.repository = repository
    
    def create_job_description(self, text: str) -> JobDescription:
        """Create a new job description."""
        if not text or len(text.strip()) == 0:
            raise ValueError("Job description text cannot be empty")
        
        jd = JobDescription(text=text)
        if not jd.validate_length():
            raise ValueError(f"Job description exceeds {jd.max_limit} characters")
        
        # Store as dict-like entity with ID
        jd.id = str(uuid4())
        self.repository.save(jd)
        return jd
    
    def get_job_description(self, jd_id: str) -> Optional[JobDescription]:
        """Retrieve a job description by ID."""
        return self.repository.find_by_id(jd_id)
    
    def get_all_job_descriptions(self) -> List[JobDescription]:
        """Retrieve all job descriptions."""
        return self.repository.find_all()
    
    def update_job_description(self, jd_id: str, text: str) -> JobDescription:
        """Update an existing job description."""
        jd = self.repository.find_by_id(jd_id)
        if not jd:
            raise ValueError(f"Job description {jd_id} not found")
        
        if not text or len(text.strip()) == 0:
            raise ValueError("Job description text cannot be empty")
        
        if len(text) > jd.max_limit:
            raise ValueError(f"Job description exceeds {jd.max_limit} characters")
        
        jd.text = text
        self.repository.save(jd)
        return jd
    
    def delete_job_description(self, jd_id: str) -> None:
        """Delete a job description."""
        self.repository.delete(jd_id)