from typing import Tuple
from textblob import TextBlob


def analyze_sentiment(text: str) -> Tuple[str, float]:
    """
    Analyze sentiment of a review using TextBlob.

    Args:
        text (str): Review text.

    Returns:
        Tuple[str, float]: Sentiment label and score.
    """
    blob = TextBlob(str(text))
    score = blob.sentiment.polarity

    if score > 0.05:
        label = "POSITIVE"
    elif score < -0.05:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    return label, score
