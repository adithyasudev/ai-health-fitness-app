# 🏋️ AI Health & Fitness Plan Generator

This is a Streamlit-powered AI app that generates a **custom 1-week health & fitness plan** using OpenAI GPT models based on user input like age, weight, activity level, goals, and food preferences.

---

## 🚀 How It Works

1. User enters their fitness-related details in the sidebar:
   - Goal (e.g., lose weight, build muscle)
   - Age
   - Weight
   - Activity level
   - Food preferences

2. The app sends these details to **OpenAI GPT-3.5** via a structured prompt.

3. GPT generates:
   - 🏃 Daily workout plan  
   - 🍽️ Daily meal plan (breakfast, lunch, dinner)  
   - 💡 Daily motivational health tip  

4. The output is shown in a clear, structured format inside the app.

---

## 🔑 Setting the OpenAI API Key

To use this app, you need an OpenAI API key.

### 🔐 Step-by-step:

1. **Create a `.streamlit/secrets.toml` file** in your project directory:
