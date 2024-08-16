
# Trip Planner Crew

## Overview

**Trip Planner Crew** is an intelligent travel planning application designed to assist users in creating detailed travel itineraries. The app leverages a combination of AI agents to provide recommendations for city selection, generate in-depth city guides, and create comprehensive 7-day travel itineraries based on user preferences.

The application is powered by advanced AI models and tools, utilizing the Groq API with the LLaMA3 model and SERPER API to perform various tasks including searching the internet, calculating budgets, and gathering information.

## Features

- **City Selection**: Analyze and select the best city for travel based on weather, season, prices, and user interests.
- **Detailed Itinerary Creation**: Generate a 7-day itinerary with day-to-day plans, including accommodation, dining, activities, and budget details.
- **In-Depth City Guide**: Compile comprehensive information about cities, including attractions, cultural hotspots, hidden gems, and local customs.

## Technology Stack

- **Python**
- **Flask** - Web framework
- **CrewAI** - AI-powered task automation
- **Groq API** - AI model for intelligent decision-making
- - **SERPER API** - For getting information from Internet
- **HTML/CSS** - Frontend interface

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Virtualenv (optional, but recommended)

### Clone the Repository

```bash
git clone https://github.com/your-username/trip-planner-crew.git
cd trip-planner-crew
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add your Groq API and Serper API key:

```bash
GROQ_API=your_groq_api_key
SERPER_API=your_serper_api_key
```

### Run the Application

```bash
python app.py
```

This will start the Flask application on `http://localhost:5000`.

## Usage

1. **Start the Application**: Run the Flask app and navigate to `http://localhost:5000`.
2. **Enter Travel Details**: Fill in the travel form with your origin, desired cities, travel dates, and interests.
3. **View Your Itinerary**: Once submitted, the app will generate a detailed travel itinerary based on the input provided.

## Project Structure

```
trip-planner-crew/
│
├── agents.py                      # Defines AI agents for different roles
├── tasks.py                       # Contains task definitions for each agent
├── main.py                        # Central script for running the travel planning logic
├── app.py                         # Flask app entry point
├── templates/                     # HTML templates for the web interface
│   ├── index.html                 # Home page template
│   └── result.html                # Result display template
├── static/                        # Static assets (CSS, JS, etc.)
├── .env                           # Environment variables file
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```




## Architecture

![Architecture.png](https://i.ibb.co/Xj1B5vB/Version-1.png)

## Presentation

[Link to PPT](https://drive.google.com/file/d/1R4af9vPvucmJdyxNktGkKKrhRGybG5Qt/view?usp=sharing)

## Contributors
[@Amber Bagchi](https://github.com/amber-bagchi)
[@Ankit Kumar](https://github.com/iamankit7667)
[@Danyal Habib](https://github.com/DanyalHabib007)
[@Om Shankar Thakur](https://github.com/Om-Shankar-Thakur)
