# 🏝️ Travel Itinerary Planner

## 🌍 Overview
The **Travel Itinerary Planner** is a Streamlit web application that generates a detailed and personalized travel itinerary based on user preferences. It leverages **Groq's Llama 3.3-70B model** to create customized travel plans including activities, travel times, and suggestions tailored to the traveler's interests and budget.

## 🚀 Features
- **Interactive UI**: A visually appealing interface with easy input fields.
- **Personalized Itinerary**: Generates a daily itinerary based on destination, interests, and budget.
- **Realistic Travel Plans**: Includes activity suggestions with time slots and travel durations.
- **Smart Adjustments**: Takes into account closed attractions and suggests alternatives.
- **Emoji-Rich Markdown Output**: The itinerary is formatted with relevant emojis to make it engaging.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/travel-itinerary-planner.git
   cd travel-itinerary-planner
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   - Create a `.env` file in the root directory and add:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     ```

## 🎮 Usage
Run the application using:
```bash
streamlit run app.py
```

Then, open the browser and start planning your next adventure!

## 🏗️ Project Structure
```
travel-itinerary-planner/
│── app.py                 # Main Streamlit application
│── requirements.txt       # List of dependencies
│── .env                   # Environment variables
│── README.md              # Project documentation
```

## 🤝 Contributing
Feel free to contribute by submitting issues or pull requests!

## 📜 License
This project is licensed under the MIT License.

