# dashboard/app.py
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ----------------------
# Clear previous cache
# ----------------------
st.cache_data.clear()

# ----------------------
# Page Config
# ----------------------
st.set_page_config(
    page_title="Ethiopian Bank Reviews Dashboard",
    layout="wide"
)

st.title("Ethiopian Bank Mobile App Reviews Dashboard")
st.markdown(
    """
This dashboard shows **user reviews and sentiment analysis** for BOA, CBE, and Dashen bank mobile apps.
Filter by bank and rating, view metrics, distribution charts, sentiment, and a word cloud.
"""
)

# ----------------------
# Data Loader
# ----------------------
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    main_file = os.path.join(base_path, "../data/ethopian_bank_reviews.csv")
    sample_file = os.path.join(base_path, "../sample_reviews.csv")  # fallback in project root

    if os.path.exists(main_file):
        df = pd.read_csv(main_file)
        st.success("Loaded full dataset")
    elif os.path.exists(sample_file):
        df = pd.read_csv(sample_file)
        st.warning("Full dataset not found. Using sample CSV instead.")
    else:
        st.error("No data file found. Please add CSV to `data/` folder or project root.")
        return pd.DataFrame()
    return df

df = load_data()
if df.empty:
    st.stop()

# ----------------------
# Sidebar Filters
# ----------------------
st.sidebar.header("Filters")
banks = df['bank'].unique()
selected_banks = st.sidebar.multiselect("Select Bank(s)", banks, default=banks)

ratings = sorted(df['rating'].unique())
selected_ratings = st.sidebar.multiselect("Select Rating(s)", ratings, default=ratings)

filtered_df = df[(df['bank'].isin(selected_banks)) & (df['rating'].isin(selected_ratings))]

# ----------------------
# Summary Metrics
# ----------------------
st.subheader("Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", len(filtered_df))
col2.metric("Average Rating", round(filtered_df['rating'].mean(), 2))
col3.metric("Median Rating", filtered_df['rating'].median())

# ----------------------
# Sentiment Metrics (if available)
# ----------------------
if 'sentiment_label' in filtered_df.columns:
    sentiment_counts = filtered_df['sentiment_label'].value_counts()
    col4, col5, col6 = st.columns(3)
    col4.metric("Positive Reviews", sentiment_counts.get("POSITIVE", 0))
    col5.metric("Neutral Reviews", sentiment_counts.get("NEUTRAL", 0))
    col6.metric("Negative Reviews", sentiment_counts.get("NEGATIVE", 0))

    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis", ax=ax)
    ax.set_ylabel("Number of Reviews")
    st.pyplot(fig)
    plt.clf()

if 'sentiment_score' in filtered_df.columns:
    avg_sentiment = round(filtered_df['sentiment_score'].mean(), 2)
    st.info(f"Average Sentiment Score: {avg_sentiment}")

# ----------------------
# Rating Distribution Chart
# ----------------------
st.subheader("Rating Distribution per Bank")
plt.figure(figsize=(8,4))
sns.countplot(data=filtered_df, x='rating', hue='bank')
plt.title("Rating Distribution")
st.pyplot(plt.gcf())
plt.clf()

# ----------------------
# Word Cloud
# ----------------------
st.subheader("Reviews Word Cloud")
if st.checkbox("Show Word Cloud"):
    text = " ".join(filtered_df['review'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    st.image(wordcloud.to_array(), use_column_width=True)

# ----------------------
# Show Raw Data
# ----------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
