import json
from settings import client

MODEL_ID = "amazon.nova-lite-v1:0"


def build_prompt(repo_data):

    prompt = f"""
Analyze this GitHub repository.

Name: {repo_data['name']}
Description: {repo_data['description']}
Language: {repo_data['language']}
Stars: {repo_data['stars']}

Provide:
1. Project purpose
2. Technologies used
3. Possible improvements
"""

    return prompt


def analyze_repo(repo_data):

    prompt = build_prompt(repo_data)

    body = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 300,
            "temperature": 0.5
        }
    }

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())

    return result["results"][0]["outputText"]