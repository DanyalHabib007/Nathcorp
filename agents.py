from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq  # Import Groq API support
import os
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
import re
import streamlit as st

class TravelAgents:
    def __init__(self):
        # Use Groq API with LLaMA3 model
        self.OpenAIGPT35 = ChatGroq(model="llama3-70b-8192", temperature=0.7, api_key=os.environ['GROQ_API'])
        self.OpenAIGPT4 = ChatGroq(model="llama3-70b-8192", temperature=0.7, api_key=os.environ['GROQ_API'])

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""
                Expert in travel planning and logistics.
                I have decades of experience making travel itineraries.
            """),
            goal=dedent(f"""
                Create a 7-day travel itinerary with detailed per-day plans,
                budget, packing suggestions, and safety tips.
            """),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_agent(self):
        return Agent(
            role="City Selection Agent",
            backstory=dedent(f"""
                Expert at analyzing travel data to pick ideal destinations.
            """),
            goal=dedent(f"""
                Select the best cities based on weather, season, prices, and traveler interests.
            """),
            tools=[
                SearchTools.search_internet,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""
                Knowledgeable local guide with extensive information about the city, its attractions, and customs.
            """),
            goal=dedent(f"""
                Provide the BEST insights about the selected city.
            """),
            tools=[
                SearchTools.search_internet,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

class StreamToExpander:
    # Print agent process to Streamlit app container 
    # This portion of the code is adapted from @AbubakrChan; thank you!  
    
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  # Define a list of colors
        self.color_index = 0  # Initialize color index

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        if task_value:
            st.toast(":robot_face: " + task_value)

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            # Apply different color and switch color index
            self.color_index = (self.color_index + 1) % len(self.colors)  # Increment color index and wrap around if necessary

            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "City Selection Expert" in cleaned_data:
            # Apply different color 
            cleaned_data = cleaned_data.replace("City Selection Expert", f":{self.colors[self.color_index]}[City Selection Expert]")
        if "Local Expert at this city" in cleaned_data:
            cleaned_data = cleaned_data.replace("Local Expert at this city", f":{self.colors[self.color_index]}[Local Expert at this city]")
        if "Amazing Travel Concierge" in cleaned_data:
            cleaned_data = cleaned_data.replace("Amazing Travel Concierge", f":{self.colors[self.color_index]}[Amazing Travel Concierge]")
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []
