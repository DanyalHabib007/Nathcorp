

# ✈️ TravelPlanner AI Agent 🗺️

**TravelPlanner AI Agent** is an AI-powered travel planning application built with Streamlit. This app leverages advanced AI models to help users plan their trips by selecting the best destinations, gathering city information, and generating detailed travel itineraries. It provides a seamless, interactive experience for users to plan their dream vacations effortlessly.

## 🌟 Features

- **📍 Destination Selection:** Choose your origin and destination cities, set your travel dates, and specify your interests.
- **🏙️ City Information Gathering:** Get in-depth information about your destination, including attractions, cultural hotspots, weather forecasts, and more.
- **📝 Itinerary Planning:** Generate a detailed travel itinerary, including daily activities, accommodation suggestions, and budgeting tips.
- **💻 Interactive User Interface:** Streamlit provides an intuitive, easy-to-use interface for planning and viewing your trip.
- **🔍 Serper API Integration:** Leverage the Serper API to enhance travel data search capabilities.

## 🛠️ Technologies Used

- **🎨 Streamlit:** For building the user interface and creating an interactive experience.
- **🤖 CrewAI:** To manage and coordinate the AI agents that handle different aspects of the travel planning process.
- **🧠 LLaMA3 (via Groq API):** Utilized for natural language processing and generating travel recommendations.
- **🐍 Python:** Core language used for development.
- **🔗 Serper API:** Enhances search functionality to provide better travel data insights.

## 🚀 How to Run

1. **📥 Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/travelplanner-ai-agent.git
   cd travelplanner-ai-agent
   ```

2. **📦 Install the Dependencies:**

   Ensure you have Python 3.8+ and pip installed. Then, run:

   ```bash
   pip install -r requirements.txt
   ```

3. **🔐 Set Up Environment Variables:**

   Create a `.env` file in the project root directory with your API keys:

   ```bash
   GROQ_API=<Your Groq API Key>
   SERPER_API=<Your Serper API Key>
   ```

4. **▶️ Run the Application:**

   Start the Streamlit app by running:

   ```bash
   streamlit run SApp.py
   ```

5. **🌐 Access the Application:**

   The app will run on `http://localhost:8501`. Open this link in your web browser to start planning your trip!

## 📂 Project Structure

- `SApp.py`: The main application file where the Streamlit app is defined.
- `agents.py`: Contains the AI agents responsible for various travel planning tasks.
- `tasks.py`: Defines the tasks that the AI agents will perform.
- `requirements.txt`: Lists all the Python dependencies required for the project.

## Architecture

![Architecture.png](https://i.ibb.co/4SdNmfX/Version-2.png)

## Presentation

[Link to PPT](https://drive.google.com/file/d/1R4af9vPvucmJdyxNktGkKKrhRGybG5Qt/view?usp=sharing)

## 🤝 Contributors
[@Amber Bagchi](https://github.com/amber-bagchi)
[@Ankit Kumar](https://github.com/iamankit7667)
[@Danyal Habib](https://github.com/DanyalHabib007)
[@Om Shankar Thakur](https://github.com/Om-Shankar-Thakur)




