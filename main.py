from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from factories.repository_factory import RepositoryFactory
from services.cover_letter_service import CoverLetterService
from services.job_description_service import JobDescriptionService
from services.resume_service import ResumeService

# Initialize FastAPI app
app = FastAPI(
    title="TailorFit API",
    description="Service layer and REST API for TailorFit cover letter generation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize repositories and services
factory = RepositoryFactory(storage_type="inmemory")
cover_letter_repo = factory.create_cover_letter_repository()
job_description_repo = factory.create_job_description_repository()
resume_repo = factory.create_resume_repository()

cover_letter_service = CoverLetterService(cover_letter_repo)
job_description_service = JobDescriptionService(job_description_repo)
resume_service = ResumeService(resume_repo)

# Inject services into routes
from api import routes
routes.cover_letter_service = cover_letter_service
routes.job_description_service = job_description_service
routes.resume_service = resume_service

# Include routes
app.include_router(router)

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint - API is running."""
    return {
        "message": "TailorFit API is running",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health", tags=["Health"])
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)