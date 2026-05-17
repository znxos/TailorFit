import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestCoverLetterAPI:
    def test_get_all_cover_letters(self):
        response = client.get("/api/cover-letters")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_create_cover_letter(self):
        payload = {
            "content": "Dear Hiring Manager...",
            "status": "draft",
            "template_version": "1.0"
        }
        response = client.post("/api/cover-letters", json=payload)
        assert response.status_code == 201
        assert response.json()["content"] == "Dear Hiring Manager..."
    
    def test_get_cover_letter(self):
        # First create
        payload = {"content": "Test letter"}
        create_response = client.post("/api/cover-letters", json=payload)
        letter_id = create_response.json()["id"]
        
        # Then retrieve
        response = client.get(f"/api/cover-letters/{letter_id}")
        assert response.status_code == 200
        assert response.json()["id"] == letter_id
    
    def test_update_cover_letter(self):
        payload = {"content": "Test letter"}
        create_response = client.post("/api/cover-letters", json=payload)
        letter_id = create_response.json()["id"]
        
        update_payload = {"content": "Updated letter"}
        response = client.put(f"/api/cover-letters/{letter_id}", json=update_payload)
        assert response.status_code == 200
        assert response.json()["content"] == "Updated letter"
    
    def test_finalize_cover_letter(self):
        payload = {"content": "Test letter"}
        create_response = client.post("/api/cover-letters", json=payload)
        letter_id = create_response.json()["id"]
        
        response = client.post(f"/api/cover-letters/{letter_id}/finalize")
        assert response.status_code == 200
        assert response.json()["status"] == "finalized"

class TestJobDescriptionAPI:
    def test_create_job_description(self):
        payload = {"text": "Senior Python Developer needed"}
        response = client.post("/api/job-descriptions", json=payload)
        assert response.status_code == 201
        assert response.json()["text"] == "Senior Python Developer needed"

class TestResumeAPI:
    def test_create_resume(self):
        payload = {"text": "5 years of software development"}
        response = client.post("/api/resumes", json=payload)
        assert response.status_code == 201
        assert response.json()["text"] == "5 years of software development"