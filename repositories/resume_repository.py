from abc import ABC
from repositories.base_repository import Repository
from src.models import Resume

class ResumeRepository(Repository[Resume, str], ABC):
    """Entity-specific repository interface for Resumes."""
    pass