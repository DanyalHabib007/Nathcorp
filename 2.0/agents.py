from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq  # Import Groq API support
import os
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools


class TravelAgents:
    def __init__(self):
        # Use Groq API with LLaMA3 model
        self.OpenAIGPT35 = ChatGroq(model="llama3-70b-8192", temperature=0.7, api_key=os.environ['GROQ_API'])
        self.OpenAIGPT4 = ChatGroq(model="llama3-70b-8192", temperature=0.7, api_key=os.environ['GROQ_API'])

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""
                Expert in travel planning and logistics, with a keen sense of budgeting.
                I have decades of experience making travel itineraries that are both cost-effective and fulfilling.
            """),
            goal=dedent(f"""
                Create a 7-day travel itinerary with detailed per-day plans,
                budget, packing suggestions, and safety tips. Ensure all activities and accommodations fit within the specified budget.
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
                Knowledgeable local guide with extensive information about the city, its attractions, and local cuisine.
            """),
            goal=dedent(f"""
                Provide the BEST insights about the selected city, including dining options that match the traveler's food preferences.
            """),
            tools=[
                SearchTools.search_internet,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
