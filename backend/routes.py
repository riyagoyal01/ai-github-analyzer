from fastapi import APIRouter
from request_models import RepoRequest, RepoAnalysisResponse
from github_service import get_repo_data
from repo_analyzer import analyze_repo


router = APIRouter()


def extract_repo(repo_url):
    parts = str(repo_url).rstrip("/").split("/")
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo



@router.post("/analyze", response_model=RepoAnalysisResponse)
def analyze_repository(request: RepoRequest):

    owner, repo = extract_repo(request.repo_url)

    repo_data = get_repo_data(owner, repo)

    summary = analyze_repo(repo_data)

    return {
        "name": repo_data["name"],
        "language": repo_data["language"],
        "stars": repo_data["stars"],
        "summary": summary
    }