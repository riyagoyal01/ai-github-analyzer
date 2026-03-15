def analyze_repo(repo_data):

    name = repo_data.get("name")
    description = repo_data.get("description")
    language = repo_data.get("language")
    stars = repo_data.get("stars") or 0

    if stars > 500:
        popularity = "Highly popular repository"
    elif stars > 100:
        popularity = "Moderately popular repository"
    else:
        popularity = "New or niche repository"

    summary = f"""
Project Name: {name}

Description:
{description}

Primary Language:
{language}

Stars:
{stars}

Popularity Level:
{popularity}

Possible Improvements:
- Improve documentation
- Add more tests
- Optimize performance
- Add contribution guidelines
"""

    return summary