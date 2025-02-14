import os
import streamlit as st
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Missing GROQ_API_KEY environment variable. Please set it in a .env file.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)
MODEL_NAME = "llama-3.3-70b-versatile"

def calculate_num_days(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    return (end_date - start_date).days + 1

def generate_itinerary(location, start_date, end_date, interests, budget):
    num_days = calculate_num_days(start_date, end_date)
    budget_prompt = f"The traveler has a {budget} budget." if budget else ""

    prompt = f"""
    Create a detailed daily itinerary for a {num_days}-day trip to {location} from {start_date} to {end_date}. 🛫🌍
    The traveler is interested in: {interests}. 🎭🎨🍽️
    {budget_prompt}
    Provide a day-by-day breakdown with specific activities, suggested times (using a 24-hour clock), and brief descriptions. 🕰️ Include realistic travel times between activities where appropriate.
    If a specific date falls on a day of the week where some attractions might be closed, make a note of that and suggest alternatives. 🚦
    Format the itinerary clearly and concisely using Markdown with relevant emojis to make it engaging. 😊
    DO NOT provide any extra or unrelated information beyond the request. 🔒
    """

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=MODEL_NAME,
    )
    return chat_completion.choices[0].message.content

st.set_page_config(page_title="Travel Itinerary Planner", page_icon="🌴", layout="wide")
st.markdown(
    """
    <style>
        .main {
            background-color: #e0f7fa;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput, .stDateInput, .stSelectbox, .stButton>button {
            border-radius: 12px;
            padding: 12px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #008080;
            color: white;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #004d40;
        }
        .itinerary-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏝️ Ultimate Travel Itinerary Planner ✈️")
st.write("Get a personalized travel plan tailored just for you! 🌍✨")

col1, col2 = st.columns(2)

with col1:
    location = st.text_input("📍 Enter your destination:")
    start_date = st.date_input("📅 Start Date:", min_value=datetime.today())
with col2:
    end_date = st.date_input("📅 End Date:", min_value=start_date)
    budget = st.selectbox("💰 Budget:", ["Low", "Mid", "High"])

interests = st.text_input("🎭 Interests (comma-separated):")

st.markdown("---")

if st.button("🎉 Plan My Trip"):
    if not location or not interests:
        st.error("⚠️ Please fill in all required fields.")
    elif calculate_num_days(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")) <= 0:
        st.error("⚠️ End date must be after start date.")
    else:
        with st.spinner("✨ Creating your dream itinerary... ✨"):
            itinerary = generate_itinerary(
                location, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), interests, budget
            )
        st.markdown("## 🌟 Your Custom Itinerary:")
        st.markdown(f"<div class='itinerary-box'>{itinerary}</div>", unsafe_allow_html=True)
