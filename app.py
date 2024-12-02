import streamlit as st
from langchain.llms import Ollama

# Initialize Llama 3.1 via Ollama
llm = Ollama(model="llama3.1")  

# Function to generate a detailed story
def generate_story(topic, location, age_group, genre, tone):
    story_prompt = f"""
    You are a masterful storyteller. Write a detailed story with at least 2000 words.
    The story is based on the topic '{topic}' and is set in a '{location}' setting.
    It is intended for an audience aged '{age_group}' and belongs to the '{genre}' genre.
    The tone of the story should be '{tone}'.
    Ensure the story is captivating, imaginative, and appropriate for the specified audience.
    """
    response = llm(story_prompt)
    return response.strip()

# Streamlit Layout and Customization
st.set_page_config(page_title="Dynamic AI Story Generator", layout="wide")

# Adding a background
st.markdown(
    """
    <style>
    body {
        background-color: #f7f3e9;
        background-image: url('https://www.transparenttextures.com/patterns/paper.png');
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📖 Dynamic AI-Powered Story Generator")
st.markdown("### Create captivating stories tailored to your preferences! Let your imagination run wild.")

# Sidebar for Customization
st.sidebar.header("🎨 Customize Your Story")

# Expanded options for story topic, location, and genre
story_topic = st.sidebar.selectbox(
    "Select Story Topic:",
    [
        "Real World", "Dragons", "Mythological", "Elves", 
        "Prince & Princess", "Superheroes", "Space Adventures",
        "Pirates", "Time Travel", "Haunted Mansions"
    ]
)
story_location = st.sidebar.selectbox(
    "Select Story Location:",
    [
        "Urban", "Medieval", "Rustic", "Fantasy", 
        "Futuristic", "Underwater", "Outer Space", "Jungle"
    ]
)
age_group = st.sidebar.selectbox(
    "Select Age Group:",
    ["3-5 years", "6-8 years", "9-12 years", "Teens", "Adults"]
)
genre = st.sidebar.selectbox(
    "Select Genre:",
    [
        "Romance", "Fantasy", "Adventure", "Mystery", 
        "Sci-Fi", "Horror", "Comedy", "Drama"
    ]
)
tone = st.sidebar.radio(
    "Select Story Tone:",
    ["Lighthearted", "Serious", "Humorous", "Suspenseful", "Inspirational"]
)

# Generate Story Button
if st.sidebar.button("✨ Generate Story"):
    with st.spinner("Generating your story..."):
        # Generate the story
        story = generate_story(story_topic, story_location, age_group, genre, tone)
        st.success("Your story is ready! Scroll down to read it.")

    # Display the Book Cover Image with reduced size
    st.image("images/book_cover.jpg", width=300, caption="Book Cover")

    # Display the Story
    st.subheader(f"📜 Story: {story_topic}")
    st.markdown(
        f"""
        <div style="background-color: #ffffff; padding: 15px; border-radius: 10px; 
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <p style="font-family: 'Arial', sans-serif; font-size: 18px; color: #333333;">
                {story}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("""
    ---
    Made with ❤️ using [Streamlit](https://streamlit.io/) and Llama 3.1.
""")