from fastapi import APIRouter
from request_models import RepoRequest
from github_service import get_repo_data
from nova_service import analyze_repo


router = APIRouter()


def extract_repo(repo_url: str):

    parts = repo_url.rstrip("/").split("/")
    owner = parts[-2]
    repo = parts[-1]

    return owner, repo


@router.post("/analyze")
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
