# Gap AI: Knowledge Gap Detector & Adaptive Learning Coach

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An experimental AI system that identifies knowledge gaps and provides adaptive learning resources using local LLMs via Ollama and CUDA acceleration.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Features ✨

### Core Capabilities
- **Adaptive Question Selection**  
  Prioritizes weak areas using performance metrics
  ```python
  def select_question(topic_accuracy):
      return "hard" if topic_accuracy < 0.5 else "medium"

    User Performance Tracking
    Persistent storage of learning progress (JSON)

    Proactive Coaching
    Suggests review sessions based on spaced repetition

Technical Highlights

    🚀 Local LLM Inference via Ollama

    🔥 CUDA-accelerated GPU processing

    🧠 Vector Store Integration (ChromaDB)

    📊 Progress Visualization

Installation 🛠️
Prerequisites

    NVIDIA GPU with CUDA 12.2+

    Docker 24.0+

    Python 3.10+

Setup

    Start Ollama with GPU support:

bash
Copy

docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 ollama/ollama

    Install Python dependencies:

bash
Copy

conda create -n gap_ai python=3.10
conda activate gap_ai
pip install -r requirements.txt

Usage 🚀
Basic CLI Interaction
bash
Copy

python simple_qa.py --topic algebra

Sample output:
Copy

📚 Question: Solve for x: 2x + 5 = 15

Your answer: x=5
✅ Correct! The solution is x=5. (Current Accuracy: 82%)

Key Components
Component	Description	Example File
User Profiles	Persistent learning history	user_profile.py
Quiz Engine	Adaptive question generation	simple_qa.py
Knowledge Store	Vector embeddings of mistakes	vector_store.py
Architecture 🏗️
mermaid
Copy

graph TD
    A[User Interaction] --> B(Quiz Engine)
    B --> C{Assessment}
    C -->|Correct| D[Update Profile]
    C -->|Incorrect| E[Generate Tutorial]
    D --> F[Adaptive Selection]
    E --> F
    F --> B

Configuration ⚙️
Environment Variables
ini
Copy

# .env
OLLAMA_HOST=http://localhost:11434
KNOWLEDGE_STORE_PATH=./knowledge_db

Supported Topics

    Mathematics (Algebra, Calculus)

    Programming (Python, SQL)

    Language Learning (Spanish, French)

Contributing 🤝

    Fork the repository

    Create feature branch:

bash
Copy

git checkout -b feature/your-feature

    Submit PR with:

    Documentation updates

    Unit tests

    Type hints

License 📄

MIT License - See LICENSE for details
Copy


Key improvements made:
1. Added proper markdown formatting with emoji headers
2. Included installation instructions with code blocks
3. Added architecture diagram using mermaid syntax
4. Created clear component mapping table
5. Added license information
6. Improved navigation with TOC
7. Added badges for quick reference
8. Included sample configuration details
