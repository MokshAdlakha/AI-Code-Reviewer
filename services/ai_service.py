import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def analyze_code(code):

    if not API_KEY:
        return "API Key not found. Check your .env file."

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a senior competitive programming mentor.

Analyze this code:
{code}

Provide:
1. Time Complexity
2. Space Complexity
3. Possible Issues
4. Edge Cases
5. Optimization Suggestions
"""

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error from API: {response.text}"

    result = response.json()

    return result["choices"][0]["message"]["content"]
