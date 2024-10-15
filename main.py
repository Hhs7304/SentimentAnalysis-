from src.data_preprocessing import load_data, preprocess_data
from src.sentiment_analysis import apply_sentiment_analysis
from src.visualize import plot_sentiment_distribution

def main():
    # Load the data
    file_path = 'data/Reviews.csv'
    data = load_data(file_path)

    # Preprocess the data
    data = preprocess_data(data)

    # Perform sentiment analysis
    data = apply_sentiment_analysis(data)

    # Visualize the results
    plot_sentiment_distribution(data)

if __name__ == '__main__':
    main()
