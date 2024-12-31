# Stock Data Analyzer with Llama3 Integration

This repository contains a Flask web application that allows users to query historical stock data for any ticker symbol, visualize the data over the last 5 years, and generate a detailed description using the Llama3 language model. The application is built using `yfinance` for data retrieval, `matplotlib` for plotting, and `langchain_community.llms` for generating descriptions.

## Key Features
- **Fetch Historical Stock Data**: Retrieve and analyze stock data for the past 5 years using the Yahoo Finance API.
- **Visualize Stock Data**: Generate and display a line chart of the stock's closing prices over the selected period.
- **Generate Descriptions**: Utilize the Llama3 language model to create a detailed, human-readable description of the stock data summary.
- **User-Friendly Interface**: Interactive web interface for inputting ticker symbols and viewing results.

## Files
- **app.py**: Main application script that handles data fetching, plotting, and description generation.
- **templates/index.html**: Homepage template where users can input the ticker symbol.
- **templates/result.html**: Result page template displaying the stock chart and generated description.
- **requirements.txt**: List of required Python packages to run the application.

## Installation and Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/HussainNasirKhan/Stock-Data-Analyzer-with-Llama3-Integration.git
   cd Stock-Data-Analyzer-with-Llama3-Integration
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3. **Setting Up Ollama**

- Download Ollama from the following link: [Ollama Download](https://ollama.com/)

- Install the Llama3 model on your local system:
    ```bash
    ollama run llama3
    ```
4. **Run the Application**
- Start the Flask server:
   ```bash
   python app.py
- Open your web browser and navigate to http://127.0.0.1:5000/

## Usage
-  Enter the desired stock ticker symbol in the input field on the homepage.
-  Submit the form to fetch and visualize the stock data.
-  View the generated stock price chart and the detailed description on the result page.

## Technologies Used
- **Flask**: Web framework for building the application.
- **yfinance**: Library for fetching historical stock data.
- **matplotlib**: Plotting library for generating stock charts.
- **langchain_community.llms**: Language model for generating descriptive text.
- **HTML/CSS**: For the frontend templates.


