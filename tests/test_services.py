import pytest
from services.cover_letter_service import CoverLetterService
from services.job_description_service import JobDescriptionService
from services.resume_service import ResumeService
from repositories.inmemory.in_memory_cover_letter_repository import InMemoryCoverLetterRepository
from repositories.inmemory.in_memory_job_description_repository import InMemoryJobDescriptionRepository
from repositories.inmemory.in_memory_resume_repository import InMemoryResumeRepository

class TestCoverLetterService:
    @pytest.fixture
    def service(self):
        repo = InMemoryCoverLetterRepository()
        return CoverLetterService(repo)
    
    def test_create_cover_letter(self, service):
        letter = service.create_cover_letter("Dear Hiring Manager...")
        assert letter.id is not None
        assert letter.content == "Dear Hiring Manager..."
        assert letter.status == "draft"
    
    def test_create_empty_cover_letter_fails(self, service):
        with pytest.raises(ValueError, match="content cannot be empty"):
            service.create_cover_letter("")
    
    def test_get_cover_letter(self, service):
        letter = service.create_cover_letter("Content")
        retrieved = service.get_cover_letter(letter.id)
        assert retrieved.id == letter.id
        assert retrieved.content == "Content"
    
    def test_update_cover_letter(self, service):
        letter = service.create_cover_letter("Initial")
        updated = service.update_cover_letter(letter.id, "Updated")
        assert updated.content == "Updated"
    
    def test_finalize_cover_letter(self, service):
        letter = service.create_cover_letter("Content")
        finalized = service.finalize_cover_letter(letter.id)
        assert finalized.status == "finalized"
    
    def test_delete_cover_letter(self, service):
        letter = service.create_cover_letter("Content")
        service.delete_cover_letter(letter.id)
        assert service.get_cover_letter(letter.id) is None

class TestJobDescriptionService:
    @pytest.fixture
    def service(self):
        repo = InMemoryJobDescriptionRepository()
        return JobDescriptionService(repo)
    
    def test_create_job_description(self, service):
        jd = service.create_job_description("Must have Python skills")
        assert jd.id is not None
        assert jd.text == "Must have Python skills"
    
    def test_create_empty_jd_fails(self, service):
        with pytest.raises(ValueError, match="cannot be empty"):
            service.create_job_description("")

class TestResumeService:
    @pytest.fixture
    def service(self):
        repo = InMemoryResumeRepository()
        return ResumeService(repo)
    
    def test_create_resume(self, service):
        resume = service.create_resume("5 years of Python experience")
        assert resume.id is not None
        assert resume.text == "5 years of Python experience"
    
    def test_create_empty_resume_fails(self, service):
        with pytest.raises(ValueError, match="cannot be empty"):
            service.create_resume("")