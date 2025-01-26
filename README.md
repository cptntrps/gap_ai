Gap AI

Gap AI (Knowledge Gap Detector & Adaptive Learning Coach) is an experimental AI system designed to identify weak areas in a user’s knowledge and adaptively serve quizzes, resources, and mini-tutorials to help the user improve. Leveraging a local Large Language Model (LLM) via Ollama and GPU acceleration (CUDA), Gap AI aims to provide a responsive, privacy-friendly learning assistant.
Table of Contents

Overview

Overview

Gap AI’s mission is to detect and address the “knowledge gaps” learners may have in any given domain—whether it’s language learning, data science, or mathematics. By tracking user performance and analyzing past mistakes, Gap AI adapts its questions, difficulty levels, and tutorials to each individual. The system ultimately acts as a personal coach, proactively suggesting new modules, generating flashcards, and fetching relevant study material to reinforce and solidify understanding.
How It Works

User Performance Tracking: Gap AI quizzes users and evaluates their answers, logging correct and incorrect responses.
Adaptive Quiz Generation: Based on user performance metrics, the system tailors future questions to focus on weak areas.
 Mini-Tutorials: When users struggle with certain topics, Gap AI generates concise tutorials or explanations to clarify misunderstandings.
Proactive Coaching: The system can suggest new topics, modules, or flashcards for spaced repetition if it detects recurring mistakes.
Local LLM & Embeddings: Gap AI uses Ollama (running locally) and a vector store for storing
