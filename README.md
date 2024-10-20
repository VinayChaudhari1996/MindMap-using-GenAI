![image](https://github.com/VinayChaudhari1996/MindMap-using-GenAI/assets/42869040/fa548c21-186a-489b-9c7c-8bd890583a19)

# AI-Powered Markmap Visualization App
![image](https://github.com/user-attachments/assets/ec2ed024-af43-4ebe-8501-1f772203412a)

Demo : https://mindmapgenrator.streamlit.app/
## Overview
This Streamlit application generates detailed, hierarchical mind maps using Google's Generative AI (Gemini Pro) and visualizes them using Markmap. The app takes a topic as input and creates an interactive, expandable mind map with rich markdown formatting.

## Features
- 🤖 Powered by Google's Gemini Pro AI model
- 📊 Interactive mind map visualization
- 🎨 Rich markdown formatting support
- 🔒 Secure API key handling
- 📱 Responsive layout
- 💾 Session state persistence

## Prerequisites
- Python 3.7+
- Google API key (Gemini Pro access)
- Internet connection

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Dependencies
```
streamlit
streamlit-markmap
google-generativeai
```

## Configuration
1. Obtain a Google API key for Gemini Pro access:
   - Visit the [Google AI Studio](https://makersuite.google.com/)
   - Create an API key for Gemini Pro
   
2. The API key can be:
   - Entered directly in the application sidebar
   - Set as an environment variable:
     ```bash
     export GOOGLE_API_KEY='your-api-key'
     ```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Access the application in your web browser (typically http://localhost:8501)

3. Enter your Google API key in the sidebar

4. Input your topic in the text area

5. Click "Submit" to generate and visualize the mind map

## Application Structure

### Main Components:

1. **Page Configuration**
   - Wide layout
   - Custom page title

2. **Sidebar**
   - Google API key input
   - Secure password field

3. **Main Interface**
   - Topic input text area
   - Submit button
   - Markmap visualization

4. **Session State Management**
   - Persistent API key storage
   - Cache for markdown generation

### Key Functions:

#### `main()`
- Initializes the Streamlit application
- Manages session state
- Handles user interface elements

#### `create_markdown(input_data)`
- Cached function for markdown generation
- Parameters:
  - `input_data`: User-provided topic string
- Returns:
  - Generated markdown content or "Invalid" on error
- Uses Gemini Pro for content generation

## Markdown Formatting

The application generates markdown with:
- **Bold** text for parent nodes
- *Italic* text for emphasis
- ==Highlighted== text for important points
- Nested hierarchical structure

## Error Handling
- Invalid API key detection
- Error message display
- Graceful failure handling

## Security Considerations
- API key is never displayed
- Password field for secure input
- Session state for temporary storage

## Customization
You can modify the prompt template in `create_markdown()` to adjust:
- Content structure
- Formatting style
- Detail level
- Language style

## Performance
- Uses `@st.cache_data` for efficient markdown generation
- Minimizes API calls
- Optimized for responsiveness

## Limitations
- Requires active internet connection
- API key required for operation
- Rate limits based on Google API quota

## Troubleshooting

Common issues and solutions:

1. **Invalid API Key Error**
   - Verify API key is correct
   - Check Google Cloud Console for API activation
   - Ensure Gemini Pro API access is enabled

2. **Visualization Not Loading**
   - Check internet connection
   - Clear browser cache
   - Refresh the page

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments
- Streamlit team for the framework
- Markmap developers
- Google Generative AI team
