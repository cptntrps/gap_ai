import requests
from generate_question import generate_question
from user_profile import UserProfile

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def check_answer(question, user_answer):
    """
    Sends the question and the user's answer to the LLM
    and asks it to generate initial feedback.
    """
    prompt = f"""
    You are a tutor. 
    The question was: "{question}"
    The user's answer is: "{user_answer}"
    
    Instructions:
    1. Generate a comment on the user's answer.
    2. Keep feedback to 1-2 sentences
    """

    payload = {
        "model": "llama3.2:latest",
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
        return "Could not generate feedback at this time."

def main():
    user = UserProfile(user_id="demo_user")

    # Example question setup
    question = "What is 3 - 2?"
    correct_answer = "1"  # Set the correct answer for demonstration
    user_answer = input(f"Question: {question}\nYour answer: ")

    # Generate initial feedback (not shown to the user in this version)
    feedback = check_answer(question, user_answer)  # Optional usage for logging

    # Display formatted output as requested
    print("\nQuestion:", question)
    print("Your answer:", user_answer)
    print("Correct answer:", correct_answer)

    # Ask user to confirm if the answer was correct or incorrect
    confirmation = input("Was this answer right or wrong? Enter 'r' for right and 'w' for wrong: ").strip().lower()
    is_correct = confirmation == 'r'

    # Update user profile based on user confirmation
    user.update_topic(topic="arithmetic", is_correct=is_correct)
    print(f"Answer recorded as {'correct' if is_correct else 'incorrect'}.")

if __name__ == "__main__":
    main()
