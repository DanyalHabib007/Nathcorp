import sys
import streamlit as st
from datetime import datetime, timedelta
from crewai import Crew, Process
from agents import TravelAgents, StreamToExpander  # Updated imports
from tasks import TravelTasks  # Updated imports

# Configure Streamlit page settings
st.set_page_config(page_icon="✈️", page_title="TravelPlanner", layout="wide")

# Define the TravelCrew class
class TravelCrew:
    def __init__(self, from_city, destination_city, interests, date_from, date_to):
        self.from_city = from_city
        self.destination_city = destination_city
        self.interests = interests
        self.date_from = date_from
        self.date_to = date_to
        self.output_placeholder = st.empty()

    def run(self):
        agents = TravelAgents()
        tasks = TravelTasks()

        # Assign the appropriate experts and tasks
        city_selection_agent = agents.city_selection_agent()
        local_tour_guide = agents.local_tour_guide()
        expert_travel_agent = agents.expert_travel_agent()

        identify_city_task = tasks.identify_city(
            agent=city_selection_agent,
            origin=self.from_city,
            cities=[self.destination_city],
            interests=self.interests,
            travel_dates=(self.date_from, self.date_to)
        )

        gather_city_info_task = tasks.gather_city_info(
            agent=local_tour_guide,
            city=self.destination_city,
            travel_dates=(self.date_from, self.date_to),
            interests=self.interests
        )

        plan_itinerary_task = tasks.plan_itinerary(
            agent=expert_travel_agent,
            city=self.destination_city,
            travel_date=(self.date_from, self.date_to),
            interests=self.interests
        )

        # Assemble the crew and run the tasks
        crew = Crew(
            agents=[city_selection_agent, local_tour_guide, expert_travel_agent],
            tasks=[identify_city_task, gather_city_info_task, plan_itinerary_task],
            process=Process.sequential,
            full_output=True,
            share_crew=False,
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown("Processing complete...")
        
        return result

# Streamlit app header
st.header("✈️ 🎫 Travel Planner :orange[Ai]gent 🏝️ 🗺️", divider="orange")

# Sidebar with instructions
with st.sidebar:
    st.caption("Travel Planner Agent")
    st.markdown(
        """
        # 🏝️ Travel Planner 🗺️
        1. Pick your dream destination
        2. Provide your interests
        3. Set your travel dates
        4. Bon voyage !!
        """
    )
    st.divider()
    st.caption("Created by @danyal")

st.session_state.plan_pressed = False

# Main content: User input
st.caption("🗺️ Let's plan your Travel")

# User Details container
C = st.container()
X1, X2 = C.columns(2)
from_city = X1.text_input("📍 From :", placeholder="Paris, France")
destination_city = X2.text_input("🏝️ Your Destination :", placeholder="London, UK")

interests = C.text_input("🍹🛍️ Your interests :",  placeholder="Cultural, hotspots, Food, Shopping..")

Y1, Y2 = C.columns(2)
today = datetime.now()
seven_days_from_now = today + timedelta(days=7)

date_from = Y1.date_input(
    "📅 Vacation Start ✈️",
    today,
    format="DD/MM/YYYY",
)
date_to = Y2.date_input(
    "📅 Vacation End 🧳",
    seven_days_from_now,
    format="DD/MM/YYYY",
)
travel_period = (date_to - date_from).days

# Display recap and generate plan button
if from_city and destination_city and date_from and date_to and interests:
    st.caption("👌 Let's recap your Travel Plan :")
    st.write(f":sparkles: Your 🎫 :blue[{travel_period}-Days] Voyage from 📍 :blue[{from_city}] is starting the ✈️ {date_from} to 🧳 {date_to}. 🗺️ You're heading to 🏝️ :orange[{destination_city}], to enjoy 🍹 :orange[{interests}] 📸.")

    if plan := st.button("💫 Sounds Good! 🗺️ Generate The Travel Plan", use_container_width=True, key="plan"):
        with st.spinner(text="🤖 Agents working for the best Travel Plan 🔍 ..."):
            with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
                with st.container(height=200, border=False):
                    sys.stdout = StreamToExpander(st)  # Updated to use StreamToExpander from the new import
                    travel_crew = TravelCrew(from_city, destination_city, interests, date_from, date_to)
                    result = travel_crew.run()

                status.update(label="✅ Trip Plan Ready!", state="complete", expanded=False)

            st.subheader("🗺️ Here is your Trip Plan 🎫 🏝️", anchor=False, divider="rainbow")

            # Print the result object directly
            st.write(result)
            st.divider()
