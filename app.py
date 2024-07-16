from flask import Flask, render_template, request
import yfinance as yf
import datetime
import matplotlib.pyplot as plt
from langchain_community.llms import Ollama

app = Flask(__name__)

def fetch_and_plot_stock_data(ticker_symbol):
    # Define the time period
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=5*365)
    
    # Fetch the stock data
    ticker_data = yf.Ticker(ticker_symbol)
    stock_data = ticker_data.history(start=start_date, end=end_date)
    
    # Generate a chart
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'], label='Close Price')
    plt.title(f'{ticker_symbol} Stock Price Over the Last 5 Years')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.grid(True)
    plot_filename = f'static/{ticker_symbol}_stock_price_last_5_years.png'
    plt.savefig(plot_filename)  # Save plot to static directory
    plt.close()  # Close plot to free up memory
    
    return stock_data, plot_filename

def summarize_stock_data(stock_data):
    # Prepare the data summary
    stock_summary = stock_data.describe().to_dict()
    
    return stock_summary

def generate_description(summary_text, base_url='http://localhost:11434', model="llama3"):
    # Initialize the Llama3 instance with the base URL and model name
    llama = Ollama(base_url=base_url, model=model)
    
    # Prepare the input text for the model
    input_text = f"Generate one paragraph description for the following stock summary:\n\n{summary_text}\n But Don't mention total counts each time."
    
    # Generate the description using the model
    generated_description = llama(input_text)
    
    # Format the generated description with headings, paragraphs, and bullet points
    formatted_description = f"""
    <h2>Generated Description:</h2>
    <ul>
        <li>{generated_description}</li>
    </ul>
    """
    
    return formatted_description

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker_symbol = request.form['ticker_symbol'].upper()
        if ticker_symbol:
            try:
                # Fetch and plot the stock data
                stock_data, plot_filename = fetch_and_plot_stock_data(ticker_symbol)
                
                # Summarize the stock data
                stock_summary = summarize_stock_data(stock_data)
                
                # Generate a detailed description
                summary_text = f"Summary statistics of {ticker_symbol} stock data over the last 5 years:\n\n{stock_summary}"
                generated_description = generate_description(summary_text)
                
                return render_template('result.html', ticker_symbol=ticker_symbol, plot_filename=plot_filename, generated_description=generated_description)
            except Exception as e:
                return render_template('index.html', error_message=f"Error fetching data for {ticker_symbol}: {e}")
        else:
            return render_template('index.html', error_message="Please enter a valid ticker symbol.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
