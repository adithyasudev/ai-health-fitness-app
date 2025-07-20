# 🏋️ AI Health & Fitness Plan Generator

This is a **Streamlit-powered AI app** that generates a custom 1-week health & fitness plan using **OpenAI GPT models** based on user input like age, weight, activity level, goals, and food preferences.

---

## 🚀 How It Works

The user provides their fitness-related details via the sidebar:

- 🏁 **Goal** (e.g., lose weight, build muscle)
- 🎂 **Age**
- ⚖️ **Weight**
- 🏃‍♂️ **Activity level**
- 🍴 **Food preferences**

The app sends these details to **OpenAI GPT-3.5** using a structured prompt.

GPT responds with:

- 🏋️ **Daily Workout Plan**
- 🍱 **Meal Plan** (Breakfast, Lunch, Dinner)
- 💡 **Motivational Health Tip**

All results are displayed in a clean, structured format within the app.

---

## 🔑 Setting the OpenAI API Key

To use this app, you need an **OpenAI API key that you have to purchase from https://platform.openai.com/settings/organization/billing/overview **.

### 🔐 Step-by-step:

1. Create a `.streamlit/secrets.toml` file in your project root (for local development):
   ```toml
   [api_keys]
   openai = "your_openai_api_key_here"
### 🌐 For Streamlit Cloud Deployment:

1. Visit [Streamlit Cloud](https://streamlit.io)
2. Open your deployed app → Click **"Manage app"**
3. Go to the **"Secrets"** tab
4. Paste the following content:

   ```toml
   [api_keys]
   openai = "your_openai_api_key_here"
   
###📦 Installation & Running Locally
✅ Prerequisites:
Python 3.10+

An OpenAI API key

🔧 Installation:
bash
Copy
Edit
git clone https://github.com/adithyasudev/ai-health-fitness-app.git
cd ai-health-fitness-app
pip install -r requirements.txt

###▶️ Run the App:
in bash
streamlit run app.py

###🌐 Deployment
The app is deployed using Streamlit Cloud.

🔗 Live App: [Click to Launch](https://ai-health-fitness-app-awuowcwhtjbviax9d739ky.streamlit.app/)

###🌐 For Streamlit Cloud Deployment
🔗 Visit Streamlit Cloud  [Click to Launch](https://streamlit.io/)]

Open your deployed app → Click "Manage app"

Go to the "Secrets" tab

Paste the following content:

toml
Copy
Edit
[api_keys]
openai = "your_openai_api_key_here"
Click Save and redeploy the app.

ai-health-fitness-app/
│
├── app.py                  # Main Streamlit app  
├── requirements.txt        # Python dependencies  
├── README.md               # Project documentation  
└── .streamlit/
    └── secrets.toml        # (NOT pushed to GitHub) API keys for local use


###🧠 Powered By
Streamlit

OpenAI GPT-4

###📬 Contact
Made with 💪 by Adithya Sudev
🔗 GitHub Profile [Click to Launch]((https://github.com/adithyasudev))

## 🖼️ Screenshots

### 🏠 Home Page with Input Sidebar  
![Home Page](https://i.ibb.co/JW1YFGZG/Ai-health-app-screenshot.png)

### 📋 Generated Weekly Plan  
![Weekly Plan](https://i.ibb.co/PzvsHKGt/generated-query-screenshot.png)

### ✅ Motivational Tips Displayed  
![Motivational Tip](https://i.ibb.co/ns6RcbQz/motivation-ai-generted.png)




---

## 🎥 Demo Video

Watch a full walkthrough of the app:  
👉 [Click here to watch on Vimeo](https://vimeo.com/1102866319)












