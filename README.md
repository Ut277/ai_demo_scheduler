# AI Demo Scheduler

## Overview
AI Demo Scheduler is a voice-based AI agent designed to manage and schedule product demo sessions. The agent leverages various technologies and APIs to interact with users, provide product information, and handle demo scheduling.

## Features
- Voice recognition and interaction
- Integration with Google Calendar for scheduling
- Integration with fine tuned GPT 2

## Installation

### Prerequisites
- Python 3.x
- Virtual environment tool (optional but recommended)
- Required Python packages (listed in `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Ut277/ai_demo_scheduler.git
   cd ai_demo_scheduler
 
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

### Configuration
1. Set up Google Cloud credentials:

Ensure you have a Google Cloud project with the necessary APIs enabled.

Create a service account and download the credentials.json file.

Set the environment variable: export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"

### Usage
1. Run the main application:
   python main.py
2. Follow the voice prompts to interact with the AI agent.   
