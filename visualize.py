import matplotlib.pyplot as plt

def plot_sentiment_distribution(data):
    """Plots the distribution of sentiments."""
    data['Analyzed_Sentiment'].value_counts().plot(kind='bar')
    plt.title('Sentiment Analysis Results')
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.show()
