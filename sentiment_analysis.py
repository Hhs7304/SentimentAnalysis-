from textblob import TextBlob

def analyze_sentiment(text):
    """Analyzes sentiment using TextBlob."""
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def apply_sentiment_analysis(data):
    """Applies sentiment analysis to the text column."""
    data['Analyzed_Sentiment'] = data['Text'].apply(analyze_sentiment)
    return data
