from typing import Optional, List
from repositories.resume_repository import ResumeRepository
from src.models import Resume

class InMemoryResumeRepository(ResumeRepository):
    """In-memory implementation of ResumeRepository."""
    
    def __init__(self):
        self._storage: dict[str, Resume] = {}
    
    def save(self, entity: Resume) -> None:
        self._storage[entity.id] = entity
    
    def find_by_id(self, entity_id: str) -> Optional[Resume]:
        return self._storage.get(entity_id)
    
    def find_all(self) -> List[Resume]:
        return list(self._storage.values())
    
    def delete(self, entity_id: str) -> None:
        self._storage.pop(entity_id, None)