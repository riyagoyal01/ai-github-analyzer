# AI GitHub Repository Analyzer

A Python-based application that analyzes a GitHub repository and generates a summary of the project using repository metadata.

The application allows users to enter a GitHub repository URL through a simple HTML interface. The backend fetches repository information using the GitHub API and analyzes key details such as the programming language, number of stars, and overall popularity of the repository.

---

## Features

* Analyze a GitHub repository using its URL
* Fetch repository metadata using the GitHub API
* Identify the primary programming language used in the project
* Determine repository popularity based on star count
* Generate a structured summary of the repository
* Backend API built using FastAPI
* Simple HTML frontend interface for user input

---

## Tech Stack

* Python
* FastAPI
* GitHub REST API
* Requests
* Pydantic
* HTML (Frontend)

---

## How It Works

1. User enters a GitHub repository URL in the frontend interface.
2. The frontend sends a request to the backend API.
3. The backend extracts the repository owner and name from the URL.
4. The application fetches repository information from the GitHub API.
5. The repository data is analyzed to generate a summary.
6. The analysis results are returned and displayed to the user.

---

## Example Output

```json
{
  "name": "flask",
  "language": "Python",
  "stars": 65000,
  "summary": "Project Name: flask ... Popularity Level: Highly popular repository"
}
```

---

## Use Cases

* Quickly understand the basic details of a GitHub repository
* Analyze open source projects before exploring the code
* Get a quick summary of repository popularity and technology