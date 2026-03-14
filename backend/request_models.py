from pydantic import BaseModel, HttpUrl


class RepoRequest(BaseModel):
    repo_url: HttpUrl


class RepoAnalysisResponse(BaseModel):
    name: str
    language: str
    stars: int
    summary: str
