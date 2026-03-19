# 🔍 AI GitHub Repo Analyzer

A web app that analyzes any public GitHub repository and returns an instant summary — including language, stars, popularity level, and improvement suggestions.

🌐 **Live Demo:** [ai-github-analyzer.netlify.app](https://ai-github-analyzer.netlify.app)

---

## ✨ Features

- Paste any public GitHub repo URL and get an instant analysis
- Displays repository name, primary language, and star count
- Generates a summary with popularity level and improvement suggestions
- Clean, responsive dark UI
- FastAPI backend with CORS support

---

## 🛠 Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Frontend  | HTML, CSS, JavaScript   |
| Backend   | Python, FastAPI         |
| API       | GitHub REST API         |
| Hosting   | Netlify + Render        |

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repo
```bash
git clone https://github.com/riyagoyal01/ai-github-analyzer.git
cd ai-github-analyzer
```

### 2. Set up the backend
```bash
cd backend
pip install -r requirements.txt
```

### 3. Run the backend
```bash
uvicorn main:app --reload
```

Backend will be live at `http://127.0.0.1:8000`

### 4. Open the frontend

Serve it locally:
```bash
cd frontend
python -m http.server 3000
```

Then visit `http://localhost:3000`

---

## 📁 Project Structure

```
ai-github-analyzer/
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── routes.py            # API route definitions
│   ├── github_service.py    # GitHub API integration
│   ├── repo_analyzer.py     # Repository analysis logic
│   ├── request_models.py    # Pydantic request/response models
│   └── requirements.txt     # Python dependencies
└── frontend/
    └── index.html           # Single page frontend
```

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` folder if needed:

```
OPENAI_API_KEY=your-key-here
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

---

## 🌍 Deployment

| Service  | Platform | URL |
|----------|----------|-----|
| Frontend | Netlify  | [ai-github-analyzer.netlify.app](https://ai-github-analyzer.netlify.app) |
| Backend  | Render   | [ai-github-analyzer.onrender.com](https://ai-github-analyzer.onrender.com) |

> ⚠️ Render free tier sleeps after 15 minutes of inactivity. The first request may take ~30 seconds to wake up.

---