# Dynamic AI Story Generator 📖

## Overview
Dynamic AI Story Generator is an interactive web application that uses the power of OpenAI's Llama 3.1 language model and Streamlit to create engaging and personalized stories. The application allows users to select story parameters such as topic, location, target age group, genre, and tone to generate a captivating story of at least 2000 words.

---

## Features
- **Customizable Story Parameters**: Tailor the story to your preferences by selecting:
  - **Story Topic**: From dragons to haunted mansions.
  - **Location**: Settings like fantasy worlds, medieval towns, or outer space.
  - **Age Group**: Stories for kids, teens, or adults.
  - **Genre**: Adventure, mystery, fantasy, and more.
  - **Tone**: Lighthearted, suspenseful, humorous, and others.
- **Book Cover Display**: Adds a visual touch with a customizable book cover image.
- **Responsive Design**: Built using Streamlit for a sleek and user-friendly experience.

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/dynamic-ai-story-generator.git
   cd dynamic-ai-story-generator
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
3. Place your book cover image in the images folder with the name book_cover.jpg.
4. Run the application:
    ```bash
    streamlit run app.py
5. Open your browser and navigate to:
    ```bash
    http://localhost:8501
---

## Usage
1. Customize your story using the options in the sidebar:
   - Select the **Story Topic**: Choose themes like "Dragons," "Haunted Mansions," or "Space Adventures."
   - Choose the **Location**: Settings such as "Fantasy," "Outer Space," or "Urban."
   - Specify the **Age Group**: Stories tailored for kids, teens, or adults.
   - Pick a **Genre**: Options like "Romance," "Fantasy," "Adventure," and more.
   - Define the **Tone**: Choose from "Lighthearted," "Suspenseful," or "Inspirational."
2. Click the **"✨ Generate Story"** button to create your story.
3. The app will:
   - Display a **Book Cover Image** at the top of the story.
   - Generate and display a **Story Title** based on the topic and genre.
   - Render a **detailed 2000-word story** under the title.

---

## Screenshot

![sample_interface](https://github.com/user-attachments/assets/39fbd2e5-c72c-4b19-b8c2-e2c8bd5a6fe0)

---

## Project Structure

    ├── app.py                   # Main application script
    ├── images/
    │   └── book_cover.jpg       # Customizable book cover image
    ├── requirements.txt         # Required Python libraries
    ├── README.md                # Project documentation

---

## Requirements
- **Python**: Version 3.9 or higher
- **Dependencies**:
  - `streamlit`: For building the web interface.
  - `langchain`: For prompt template handling.
  - `ollama`: For integrating with the Llama 3.1 language model.
---

## Future Enhancements
- **Expanded Customization**:
  - More genres and tones.
  - User-uploaded custom book cover images.
- **Multilingual Support**: Generate stories in different languages.
- **Story Saving**: Option to download generated stories as a PDF or text file.

---

## Credits
- **Streamlit**: Enables an intuitive, responsive interface.
- **Llama 3.1**: Powers the AI-driven storytelling.
- **OpenAI**: Underlying technology behind the language model.

---

## Contributing
I welcome contributions! To suggest new features or report bugs:
1. Fork this repository.
2. Submit a pull request with your changes.
3. Open an issue for discussions or feedback.

---

**Built with ❤️ by [Amey Ghate]**

---
