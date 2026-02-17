import pandas as pd


def clean_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw review dataframe.

    - Remove duplicates
    - Remove missing reviews
    - Convert date column

    Args:
        df (pd.DataFrame): Raw reviews dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    df = df.copy()

    df.drop_duplicates(subset="review", inplace=True)
    df.dropna(subset=["review"], inplace=True)
    df["date"] = pd.to_datetime(df["date"]).dt.date

    return df
