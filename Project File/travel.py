import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
import time

st.set_page_config(page_title="TravelGuideAI", layout="centered")

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def generate_itinerary(destination, days, nights):
    prompt = f"""
    Create a detailed {days}-day and {nights}-night travel itinerary for {destination}.
    Include:
    - Day-wise breakdown
    - Major attractions
    - Food recommendations
    - Travel tips
    - Best time to visit
    - Transportation suggestions
    Format clearly with headings.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Remove weird empty top block */
.block-container {
    padding-top: 2rem;
}

/* Card style */
.main-card {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 18px;
    backdrop-filter: blur(15px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}

/* Result floating card */
.result-card {
    background: rgba(255,255,255,0.07);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 35px rgba(0,0,0,0.6);
    margin-top: 20px;
    animation: floatUp 0.5s ease-in-out;
}

@keyframes floatUp {
    from {opacity:0; transform: translateY(25px);}
    to {opacity:1; transform: translateY(0);}
}

/* Input labels white */
label {
    color: white !important;
    font-weight: 500 !important;
}

/* Input fields */
.stTextInput>div>div>input {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
}

.stNumberInput>div>div>input {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
}

/* Button */
.stButton>button {
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 20px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(45deg, #ff4b2b, #ff416c);
}

/* Title styling */
.title-text {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle-text {
    text-align: center;
    font-size: 16px;
    opacity: 0.75;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="title-text">🌍 TravelGuideAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">AI-Powered Smart Travel Planner</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    destination = st.text_input("Destination", placeholder="Enter destination")

    col1, col2 = st.columns(2)

    with col1:
        days = st.number_input("Days", min_value=1, value=3)

    with col2:
        nights = st.number_input("Nights", min_value=1, value=2)

    st.markdown("<br>", unsafe_allow_html=True)

    generate = st.button("✨ Generate Itinerary", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


if generate:
    if destination.strip() == "":
        st.warning("Please enter a destination.")
    else:
        with st.spinner("✨ Creating your AI travel experience..."):
            time.sleep(1)
            itinerary = generate_itinerary(destination, days, nights)

        st.markdown(f"""
        <div class="result-card">
        <h2 style="color:white;">{destination} – {days} Days & {nights} Nights</h2>
        <div style="color:white;">{itinerary}</div>
        </div>
        """, unsafe_allow_html=True)
