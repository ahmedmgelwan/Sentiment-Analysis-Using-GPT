# Sentiment Analysis Using GPT

## Overview

This project utilizes FastAPI to create a web API for sentiment analysis using the GPT-3.5 Turbo model from OpenAI. The sentiment analysis is performed on user input sentences, and the results are displayed using a Streamlit prototype.

## Project Structure

- **main.py**: FastAPI application defining API routes.
- **utils.py**: Contains utility functions, including the function for sentiment analysis using the OpenAI GPT-3.5 Turbo model.
- **streamlit_app.py**: Streamlit prototype for user interaction and displaying sentiment analysis results.

## Dependencies

- FastAPI
- OpenAI GPT-3.5 Turbo
- Streamlit
- Requests
- Python-dotenv

## Setup

1. Install dependencies using the following command:
    ```bash
    pip install fastapi openai streamlit requests python-dotenv
    ```

2. Create a `.env` file in the project root directory and add your OpenAI API key:
    ```env
    OpenAI_API_KEY=your_api_key_here
    ```

## Running the Application

1. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. In a separate terminal, run the Streamlit prototype:
    ```bash
    streamlit run streamlit_app.py
    ```

   This will open a local Streamlit server and allow users to input sentences for sentiment analysis.

## API Endpoint

- **POST /emotion**
  - **Description**: Endpoint for sentiment analysis.
  - **Request Body**:
    - `user_prompt`: String - The user input sentence for sentiment analysis.
  - **Response**:
    - JSON object containing the sentiment analysis result.

## Example Usage

1. Access the Streamlit app at `http://localhost:8501` in your web browser.

2. Enter a sentence in the input field and click the "Classify" button.

3. The sentiment analysis result will be displayed on the Streamlit app.

## Notes

- Ensure that the OpenAI API key is correctly set in the `.env` file.
- This is a prototype, and additional error handling and security measures should be implemented before deploying to production.


