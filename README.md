# 📌 Mobile Banking Review Analysis

## Capstone Project – 10 Academy AI Mastery Program

This project analyzes **Google Play Store reviews** from Ethiopian mobile banking applications to transform unstructured customer feedback into structured, actionable business insights.

It implements a **production-style end-to-end data pipeline**, including:

* Data scraping
* Data cleaning & preprocessing
* Sentiment analysis (NLP)
* Thematic extraction
* PostgreSQL database integration
* Insight generation & visualization
* Engineering enhancements (modularization, testing, CI/CD)

The objective is to convert raw customer reviews into **data-driven product intelligence** for banking stakeholders.

---

# 🎯 Business Problem

Mobile banking platforms receive continuous user feedback highlighting issues such as:

* Application crashes
* Transaction failures
* Login difficulties
* Poor UI/UX
* Missing features

However, this feedback is unstructured and difficult to analyze at scale.

This project builds an automated NLP pipeline that converts raw review text into measurable:

* Sentiment metrics
* Recurring issue themes
* Comparative performance indicators across banks

Enabling product teams to prioritize improvements using structured evidence rather than anecdotal feedback.

---

# 🏗 Project Architecture

```
mobile-banking-review-analysis/
│
├── src/                             # Modular production-ready code
│   ├── scraping.py
│   ├── preprocessing.py
│   ├── sentiment.py
│   ├── themes.py
│   └── database.py
│
├── notebooks/                       # Exploratory analysis
├── data/
│   ├── raw/
│   └── processed/
├── tests/                           # Pytest unit tests
├── .github/workflows/               # CI/CD pipeline
├── reports/
│   └── Final_Report.pdf
├── requirements.txt
└── README.md
```

The structure separates data engineering logic from exploratory analysis, improving maintainability and scalability.

---

# 🚀 Project Components

---

## 1️⃣ Data Collection & Preprocessing

**Tools Used:**
Python, Pandas, `google_play_scraper`

### Process:

* Scraped 499 Google Play reviews across:

  * Commercial Bank of Ethiopia (CBE)
  * Bank of Abyssinia (BOA)
  * Dashen Bank
* Removed duplicate entries
* Cleaned null and empty reviews
* Standardized date formats
* Normalized text (lowercasing, whitespace cleaning)

**Output:**
Structured dataset ready for NLP processing.

---

## 2️⃣ Sentiment Analysis

**Method:** VADER (Valence Aware Dictionary for Sentiment Reasoning)

### Classification Thresholds:

* Positive → compound > 0.05
* Neutral → -0.05 ≤ compound ≤ 0.05
* Negative → compound < -0.05

### Results Summary:

| Sentiment | Count |
| --------- | ----- |
| Positive  | 250   |
| Neutral   | 190   |
| Negative  | 59    |

Dashen Bank shows the highest average sentiment score, indicating relatively stronger customer satisfaction compared to competitors.

---

## 3️⃣ Thematic Analysis

To identify recurring user concerns and satisfaction drivers:

* Extracted keywords using TF-IDF
* Performed noun-based theme grouping
* Categorized reviews into structured themes:

  * User Interface & Experience
  * Account Access Issues
  * Transaction Performance
  * Customer Support
  * Feature Requests
  * Technical Stability Issues

### Key Findings:

* **UI/UX quality** is the strongest satisfaction driver.
* **Login failures and technical instability** are recurring pain points across multiple banks.
* Transaction-related complaints significantly impact negative sentiment.

---

## 4️⃣ Database Integration (Task 3)

A relational PostgreSQL schema was designed to ensure scalable and structured storage.

### Implementation Highlights:

* Normalized tables for banks and reviews
* Foreign key constraints for referential integrity
* Conflict handling to prevent duplicate insertions
* Structured schema for future extensibility

This enables reliable long-term storage and advanced querying capabilities.

---

## 5️⃣ Insights & Recommendations (Task 4)

The analysis generated:

* Sentiment distribution comparison per bank
* Rating distribution trends
* Top recurring themes per institution
* Clear identification of drivers and pain points

### Example Recommendations:

* Improve technical stability to reduce crash-related complaints
* Strengthen authentication systems to minimize login issues
* Maintain and enhance intuitive UI features (Dashen advantage)
* Introduce budgeting and in-app tracking features

These recommendations align directly with observed user sentiment patterns.

---

# ⚙ Engineering Enhancements

This project was elevated beyond exploratory analysis into a production-style system.

### ✅ Modular Codebase

Refactored scripts into a `src/` structure for maintainability and reusability.

### ✅ Automated Testing

* 6 unit tests implemented using Pytest
* Validates preprocessing, sentiment classification, and theme extraction logic

### ✅ Continuous Integration

GitHub Actions pipeline:

* Installs dependencies
* Runs automated tests
* Prevents merging broken code

This ensures reliability, reproducibility, and professional development standards.

---

# 📊 Metrics of Success

* 100% of reviews classified into sentiment categories
* Zero duplicate database records
* All unit tests passing
* CI/CD pipeline stable and reproducible
* Clear identification of at least 2 drivers and 2 pain points per bank

---

# 🛠 How to Run

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.\.venv\Scripts\activate       # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Execute Pipeline

```bash
python -m src.scraping
python -m src.preprocessing
python -m src.sentiment
python -m src.themes
```

Alternatively, explore the notebooks for step-by-step analysis and visualizations.

---

# 📈 Future Improvements

* Expand dataset to 1500+ reviews
* Implement advanced topic modeling (LDA or BERTopic)
* Replace VADER with transformer-based models (e.g., fine-tuned BERT)
* Deploy as REST API
* Build a Streamlit dashboard for stakeholder visualization
* Add performance monitoring and logging

---

# 👩‍💻 Author

**Kalkidan Asdesach Tekle**
AI Engineer (NLP Focus)
10 Academy – AI Mastery Program

---

# 🌟 Project Impact

This capstone demonstrates:

* End-to-end NLP pipeline design
* Real-world business application of AI
* Relational database engineering
* Automated testing and CI/CD integration
* Scalable project architecture

It reflects both **technical capability and engineering discipline**, aligning AI solutions with measurable business value.
