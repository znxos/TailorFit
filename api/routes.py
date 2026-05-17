from fastapi import APIRouter, HTTPException, status
from typing import List
from api.schemas import (
    CoverLetterCreate, CoverLetterUpdate, CoverLetterResponse,
    JobDescriptionCreate, JobDescriptionUpdate, JobDescriptionResponse,
    ResumeCreate, ResumeUpdate, ResumeResponse
)
from services.cover_letter_service import CoverLetterService
from services.job_description_service import JobDescriptionService
from services.resume_service import ResumeService

router = APIRouter(prefix="/api", tags=["TailorFit"])

# Dependency injection (you'll inject these in main.py)
cover_letter_service: CoverLetterService = None
job_description_service: JobDescriptionService = None
resume_service: ResumeService = None

# ==================== COVER LETTERS ====================

@router.get("/cover-letters", response_model=List[CoverLetterResponse], 
           summary="Get all cover letters",
           description="Retrieve all cover letters from the system")
async def get_all_cover_letters():
    """Fetch all cover letters."""
    return cover_letter_service.get_all_cover_letters()

@router.post("/cover-letters", response_model=CoverLetterResponse, 
            status_code=status.HTTP_201_CREATED,
            summary="Create a new cover letter",
            description="Create a new cover letter with initial content")
async def create_cover_letter(payload: CoverLetterCreate):
    """Create a new cover letter."""
    try:
        return cover_letter_service.create_cover_letter(
            payload.content, payload.status, payload.template_version
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/cover-letters/{letter_id}", response_model=CoverLetterResponse,
           summary="Get a cover letter by ID")
async def get_cover_letter(letter_id: str):
    """Retrieve a specific cover letter by ID."""
    letter = cover_letter_service.get_cover_letter(letter_id)
    if not letter:
        raise HTTPException(status_code=404, detail="Cover letter not found")
    return letter

@router.put("/cover-letters/{letter_id}", response_model=CoverLetterResponse,
           summary="Update a cover letter")
async def update_cover_letter(letter_id: str, payload: CoverLetterUpdate):
    """Update an existing cover letter."""
    try:
        return cover_letter_service.update_cover_letter(letter_id, payload.content)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/cover-letters/{letter_id}", status_code=status.HTTP_204_NO_CONTENT,
              summary="Delete a cover letter")
async def delete_cover_letter(letter_id: str):
    """Delete a cover letter."""
    letter = cover_letter_service.get_cover_letter(letter_id)
    if not letter:
        raise HTTPException(status_code=404, detail="Cover letter not found")
    cover_letter_service.delete_cover_letter(letter_id)

@router.post("/cover-letters/{letter_id}/finalize", response_model=CoverLetterResponse,
            summary="Finalize a cover letter",
            description="Business workflow: Mark cover letter as finalized")
async def finalize_cover_letter(letter_id: str):
    """Finalize a cover letter (business logic)."""
    try:
        return cover_letter_service.finalize_cover_letter(letter_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# ==================== JOB DESCRIPTIONS ====================

@router.get("/job-descriptions", response_model=List[JobDescriptionResponse],
           summary="Get all job descriptions")
async def get_all_job_descriptions():
    """Fetch all job descriptions."""
    return job_description_service.get_all_job_descriptions()

@router.post("/job-descriptions", response_model=JobDescriptionResponse,
            status_code=status.HTTP_201_CREATED,
            summary="Create a new job description")
async def create_job_description(payload: JobDescriptionCreate):
    """Create a new job description."""
    try:
        return job_description_service.create_job_description(payload.text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/job-descriptions/{jd_id}", response_model=JobDescriptionResponse,
           summary="Get a job description by ID")
async def get_job_description(jd_id: str):
    """Retrieve a specific job description by ID."""
    jd = job_description_service.get_job_description(jd_id)
    if not jd:
        raise HTTPException(status_code=404, detail="Job description not found")
    return jd

@router.put("/job-descriptions/{jd_id}", response_model=JobDescriptionResponse,
           summary="Update a job description")
async def update_job_description(jd_id: str, payload: JobDescriptionUpdate):
    """Update an existing job description."""
    try:
        return job_description_service.update_job_description(jd_id, payload.text)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/job-descriptions/{jd_id}", status_code=status.HTTP_204_NO_CONTENT,
              summary="Delete a job description")
async def delete_job_description(jd_id: str):
    """Delete a job description."""
    jd = job_description_service.get_job_description(jd_id)
    if not jd:
        raise HTTPException(status_code=404, detail="Job description not found")
    job_description_service.delete_job_description(jd_id)

# ==================== RESUMES ====================

@router.get("/resumes", response_model=List[ResumeResponse],
           summary="Get all resumes")
async def get_all_resumes():
    """Fetch all resumes."""
    return resume_service.get_all_resumes()

@router.post("/resumes", response_model=ResumeResponse,
            status_code=status.HTTP_201_CREATED,
            summary="Create a new resume")
async def create_resume(payload: ResumeCreate):
    """Create a new resume."""
    try:
        return resume_service.create_resume(payload.text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/resumes/{resume_id}", response_model=ResumeResponse,
           summary="Get a resume by ID")
async def get_resume(resume_id: str):
    """Retrieve a specific resume by ID."""
    resume = resume_service.get_resume(resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume

@router.put("/resumes/{resume_id}", response_model=ResumeResponse,
           summary="Update a resume")
async def update_resume(resume_id: str, payload: ResumeUpdate):
    """Update an existing resume."""
    try:
        return resume_service.update_resume(resume_id, payload.text)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/resumes/{resume_id}", status_code=status.HTTP_204_NO_CONTENT,
              summary="Delete a resume")
async def delete_resume(resume_id: str):
    """Delete a resume."""
    resume = resume_service.get_resume(resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    resume_service.delete_resume(resume_id)