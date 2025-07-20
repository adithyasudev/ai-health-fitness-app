import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

api_key = st.secrets["api_keys"]["openai"]



# Initialize OpenAI client with API key
client = OpenAI(api_key=api_key)

# App title and configuration 
st.set_page_config(page_title="AI Health & Fitness Plan Generator")
st.title("🏋️ AI Health & Fitness Plan Generator")

# Sidebar - User Inputs
st.sidebar.header("💡 Enter Your Details")
goal = st.sidebar.text_input("Your fitness goal (e.g., lose weight, build muscle):")
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)
weight = st.sidebar.number_input("Current Weight (kg)", min_value=30, max_value=200, value=70)
activity = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
food = st.sidebar.text_input("Food preferences (e.g., vegetarian, keto, no sugar):")

# Generate Button
if st.sidebar.button("Generate Plan"):
    with st.spinner("Generating your custom health & fitness plan..."):
        # Prompt for GPT
        prompt = f"""
        Create a 1-week health and fitness plan for the following person:
        - Goal: {goal}
        - Age: {age}
        - Weight: {weight} kg
        - Activity level: {activity}
        - Food preferences: {food}

        The plan should include:
        1. A daily workout plan (simple & actionable)
        2. A daily meal plan (breakfast, lunch, dinner)
        3. One motivational health tip with a quote of health experts

        Format the output clearly with titles for each day.
        """

        try:
            # Call OpenAI GPT-4 using new SDK
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful health and fitness assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=1500
            )

            generated_text = response.choices[0].message.content
            st.success("✅ Plan Generated Successfully!")
            st.markdown(generated_text)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
