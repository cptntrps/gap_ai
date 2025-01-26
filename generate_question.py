# generate_question.py
import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def generate_question(topic="arithmetic"):
    """
    Asks the LLM to create a simple question on the given topic.
    """
    prompt = f"""
    You are a tutor specializing in {topic}.
    Generate one simple question, for example: "What is 2 + 2?" 
    Do not provide the answer yet. Just the question.
    """

    payload = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        question = data.get("response", "").strip()
        return question
    except requests.exceptions.RequestException as e:
        print(f"Error generating question: {e}")
        return "Could not generate question at this time."