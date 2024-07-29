import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize Groq API key
api_key = os.getenv("GROQ_API_KEY")

# Define the Groq client
client = Groq(api_key=api_key)

# Streamlit UI
st.title("Book Recommendations")

# User input
topic = st.text_input("Enter a topic you are interested in:")

# When the user submits a topic
if st.button("Get Recommendations"):
    if topic:
        # Prepare the request payload
        messages = [
            {
                "role": "user",
                "content": f"I am looking for book recommendations on the topic: {topic}. Please provide a list of books along with their authors and a brief description of each."
            }
        ]

        # Send a request to the Groq API
        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192"  # Replace with the desired model
            )

            recommendations = chat_completion.choices[0].message.content
            st.write("### Recommendations:")
            st.write(recommendations)
        except Exception as e:
            st.write("Error: Could not fetch recommendations.")
            st.write(str(e))
    else:
        st.write("Please enter a topic to get recommendations.")