from repositories.cover_letter_repository import CoverLetterRepository
from repositories.job_description_repository import JobDescriptionRepository
from repositories.resume_repository import ResumeRepository
from repositories.inmemory.in_memory_cover_letter_repository import InMemoryCoverLetterRepository
from repositories.inmemory.in_memory_job_description_repository import InMemoryJobDescriptionRepository
from repositories.inmemory.in_memory_resume_repository import InMemoryResumeRepository

class RepositoryFactory:
    """Factory for creating repository instances."""
    
    def __init__(self, storage_type: str = "inmemory"):
        self.storage_type = storage_type
    
    def create_cover_letter_repository(self) -> CoverLetterRepository:
        if self.storage_type == "inmemory":
            return InMemoryCoverLetterRepository()
        # Future: Add filesystem, SQL, etc.
    
    def create_job_description_repository(self) -> JobDescriptionRepository:
        if self.storage_type == "inmemory":
            return InMemoryJobDescriptionRepository()
    
    def create_resume_repository(self) -> ResumeRepository:
        if self.storage_type == "inmemory":
            return InMemoryResumeRepository()