# Translation and Text Summarization App

This is a simple Streamlit app that provides translation and text summarization functionalities. The app leverages the power of OpenAI's language model to deliver accurate translations and generate summaries of text.

## Features

- Translate text to Arabic, English, or French.
- Automatic language detection for the source text.
- Easy-to-use interface with select boxes and buttons.
- Dynamic translation and summarization output displayed instantly.
- Handles grammar correction, typos, and factual errors.
- Generates professional email formats.
- Supports different tones and dialects for email generation.

## Installation

1. Install the necessary dependencies by running `pip install -r requirements.txt`.
2. Set up your OpenAI API key by creating a `.env` file and adding `OPENAI_API_KEY=your_api_key`.
3. Run the app using the command `streamlit run app.py`.
4. Access the app through the provided URL in your browser.

## Usage

The app offers the following functionalities:

### Translation

1. Select the "Translator" option from the navigation menu.
2. Enter the text you want to translate in the text area.
3. Choose the language you want to translate to from the dropdown menu.
4. Click the "Translate" button to generate the translation.
5. The translated text will be displayed below the button.

### Email Generation

1. Select the "Email" option from the navigation menu.
2. Choose the tone you want for your email (Formal or Informal) from the first dropdown menu.
3. Select the dialect you prefer (American, British, French, or Arabic) from the second dropdown menu.
4. Enter your email content in the text area.
5. Click the "Generate" button to generate the formatted email.
6. The formatted email will be displayed below the button.

### Text Summarization

1. Select the "Summarizing text" option from the navigation menu.
2. Enter the text you want to summarize in the text area.
3. Click the "Generate" button to generate the summary.
4. The summarized text will be displayed below the button.

## About

This app was created as a demonstration project by [@Elaarbi](mailto:bdabve@gmail.com). It utilizes OpenAI's language model and Streamlit framework to provide translation and text summarization capabilities. Feel free to explore and modify the app according to your needs.

For more information, visit [LangChain](https://langchain.com/) and [OpenAI](https://openai.com).

## Dependencies

The app relies on the following Python libraries:

- dotenv
- langchain
- streamlit

You can install these dependencies by running `pip install -r requirements.txt`.

## Acknowledgments

We would like to thank OpenAI for their language model and the Streamlit community for their excellent framework that made building this app possible.

Happy translating and summarizing!
