import requests

def get_repo_data(owner: str, repo: str):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return {
            "name": data.get("name"),
            "description": data.get("description"),
            "language": data.get("language"),
            "stars": data.get("stargazers_count"),
            "topics": data.get("topics", [])
        }

    elif response.status_code == 404:
        raise Exception("Repository not found")

    elif response.status_code == 403:
        raise Exception("GitHub API rate limit exceeded")

    else:
        raise Exception(f"Unexpected error: {response.status_code}")
