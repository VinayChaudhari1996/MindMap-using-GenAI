import streamlit as st
from streamlit_markmap import markmap
import google.generativeai as genai

def main():
    """
    Main function to create a Streamlit app for generating markdown content with markmap visualization.
    """

    # Set page config and sidebar
    st.set_page_config(page_title="markmap", layout="wide")

    # Create or get the session state to store API key
    session_state = st.session_state
    if 'google_api_key' not in session_state:
        session_state.google_api_key = ""

    st.sidebar.header('Google API Configuration')
    google_api_key = st.sidebar.text_input('Enter your Google API Key', type='password', value=session_state.google_api_key)

    # Configure generative AI with API key
    genai.configure(api_key=google_api_key)

    # Add input text box for data with smaller size
    data_input = st.text_area("Write down topic here", value='', height=100)

    @st.cache_data
    def create_markdown(input_data):
        """
        Function to generate detailed markdown content based on the input data.

        Parameters:
            input_data (str): The topic provided by the user.

        Returns:
            str: Generated markdown content.
        """
        prompt = """
        You are a research markdown expert. Create detailed information for the following topic in markdown format.
        Note: Add parent node in bold, use bold/italic/highlight whenever necessary **strong** *italic* ==highlight==.
        I need very detailed context and many nested points, use ==highlight==
        [Topic] => 
        """
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt + input_data)
            return response.text

        except:
            return "Invalid"

    # Add a submit button
    if st.button("Submit"):
        # Render markmap with the input data
        if create_markdown(data_input) == 'Invalid':
            st.error("Invalid API Key")
        else:
            markmap(create_markdown(data_input))

    # Save the API key to the session state
    session_state.google_api_key = google_api_key

if __name__ == "__main__":
    main()
