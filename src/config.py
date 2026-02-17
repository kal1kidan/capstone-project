from dataclasses import dataclass

@dataclass
class AppConfig:
    database_url: str
    sentiment_model: str
    min_review_length: int = 3
