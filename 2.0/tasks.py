from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests, budget, food_preferences):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a 7-day travel itinerary.
            **Description**: Expand the city guide into a full 7-day travel itinerary with detailed
            per-day plans, including weather forecasts, places to eat (based on food preferences), packing suggestions, 
            and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
            and actual restaurants to go to, ensuring all recommendations fit within the given budget.
            This itinerary should cover all aspects of the trip, from arrival to departure, iterating the city guide information with practical travel logistics.

            **Parameters**: 
            - City: {city}
            - Travel Dates: {travel_dates}
            - Interests: {interests}
            - Budget: {budget}
            - Food Preferences: {food_preferences}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output="Detailed 7-day itinerary including all required details."
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates, budget):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify the best city to visit.
            **Description**: Analyze and select the best city for the trip based on specific
            criteria such as weather patterns, seasonal events, travel costs, and the provided budget.
            This task involves comparing multiple cities, considering factors like current weather
            conditions, upcoming cultural and seasonal events, overall travel expenses, and how they align with the budget.
            Your final answer must be a detailed report on the chosen city,
            including actual flight costs, weather forecasts, attractions, and how the city aligns with the given budget.

            **Parameters**:
            - Origin: {origin}
            - Cities: {cities}
            - Interests: {interests}
            - Travel Dates: {travel_dates}
            - Budget: {budget}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output="Detailed report on the chosen city including all required details."
        )

    def gather_city_info(self, agent, city, travel_dates, interests, food_preferences):
        return Task(
            description=dedent(
                f"""
            **Task**: Gather In-depth City Guide information.
            **Description**: Compile an in-depth guide for the selected city, gathering information about 
            key attractions, local customs, special events, daily activity recommendations, and dining options that align with the food preferences.
            This guide should provide a thorough overview of what the city has to offer, including
            hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, high-level costs, and restaurant suggestions based on the traveler's food preferences.

            **Parameters**:
            - City: {city}
            - Travel Dates: {travel_dates}
            - Interests: {interests}
            - Food Preferences: {food_preferences}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output="Comprehensive city guide with detailed information."
        )
