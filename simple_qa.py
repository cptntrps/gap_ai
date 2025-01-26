# simple_qa.py
import requests
from generate_question import generate_question

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def check_answer(question, user_answer):
    """
    Sends the question and the user's answer to the LLM
    and asks it to evaluate correctness.
    """
    prompt = f"""
    You are a tutor. 
    The question was: "{question}"
    The user's answer is: "{user_answer}"
    
    Instructions:
    1. Check if the user is correct
    2. If correct, say "Correct!" and explain why
    3. If incorrect, say "Incorrect." and provide the correct answer
    4. Keep feedback to 1-2 sentences
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
        feedback = data.get("response", "").strip()
        return feedback
    except requests.exceptions.RequestException as e:
        print(f"Error checking answer: {e}")
        return "Could not evaluate answer at this time."

def main():
    # 1. Generate a question
    question = generate_question(topic="arithmetic")
    print(f"\nQuestion: {question}")

    # 2. Accept user input
    user_answer = input("Your answer: ")

    # 3. Evaluate correctness
    feedback = check_answer(question, user_answer)
    print(f"\nFeedback:\n{feedback}\n")

if __name__ == "__main__":
    main()