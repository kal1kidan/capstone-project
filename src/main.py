from preprocessing import clean_text
from sentiment import predict_sentiment

def run_pipeline():
    sample = "Great banking app!"
    cleaned = clean_text(sample)
    sentiment = predict_sentiment(cleaned)
    print(sentiment)

if __name__ == "__main__":
    run_pipeline()
