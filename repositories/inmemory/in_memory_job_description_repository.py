from typing import Optional, List
from repositories.job_description_repository import JobDescriptionRepository
from src.models import JobDescription

class InMemoryJobDescriptionRepository(JobDescriptionRepository):
    """In-memory implementation of JobDescriptionRepository."""
    
    def __init__(self):
        self._storage: dict[str, JobDescription] = {}
    
    def save(self, entity: JobDescription) -> None:
        self._storage[entity.id] = entity
    
    def find_by_id(self, entity_id: str) -> Optional[JobDescription]:
        return self._storage.get(entity_id)
    
    def find_all(self) -> List[JobDescription]:
        return list(self._storage.values())
    
    def delete(self, entity_id: str) -> None:
        self._storage.pop(entity_id, None)