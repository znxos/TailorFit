from abc import ABC
from repositories.base_repository import Repository
from src.models import JobDescription

class JobDescriptionRepository(Repository[JobDescription, str], ABC):
    """Entity-specific repository interface for JobDescriptions."""
    pass