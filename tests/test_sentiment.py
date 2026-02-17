from src.sentiment import analyze_sentiment


def test_positive_sentiment():
    label, score = analyze_sentiment("This app is amazing and very useful")

    assert label == "POSITIVE"
    assert score > 0
def test_negative_sentiment():
    label, score = analyze_sentiment("This app is terrible and useless")

    assert label == "NEGATIVE"
    assert score < 0
def test_neutral_sentiment():
    label, score = analyze_sentiment("Bank application")

    assert label == "NEUTRAL"
