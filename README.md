# 📌 Mobile Banking Review Analysis

## Capstone Project – 10 Academy AI Mastery Program

This project analyzes **Google Play Store reviews** from Ethiopian mobile banking applications to extract structured business insights from unstructured customer feedback.

It demonstrates a **full end-to-end data pipeline**, including:

* Data scraping
* Data cleaning & preprocessing
* Sentiment analysis (NLP)
* Thematic extraction
* Database integration (PostgreSQL)
* Insight generation & visualization
* Engineering improvements (modular code, testing, CI/CD)

The goal is to transform raw app reviews into **actionable product intelligence** for banking stakeholders.

---

# 🎯 Business Problem

Mobile banking users frequently report issues such as:

* App crashes
* Transaction failures
* Poor UI/UX
* Login problems
* Feature limitations

However, these reviews are unstructured and difficult to analyze at scale.

This project builds an automated NLP pipeline that converts customer reviews into measurable:

* Sentiment insights
* Recurring themes
* Comparative bank performance metrics

Enabling banks to prioritize improvements using data-driven decisions.

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
├── notebooks/                       # Exploratory & analysis notebooks
│
├── data/
│   ├── raw/
│   └── processed/
│
├── tests/                           # Pytest unit tests
│
├── .github/workflows/               # CI/CD configuration
│
├── reports/
│   └── Final_Report.pdf
│
├── requirements.txt
└── README.md
```

---

# 🚀 Project Components

---

## 1️⃣ Data Collection & Cleaning

**Tools Used:**

* `google_play_scraper`
* Python
* Pandas

### Process:

* Scraped 499 Google Play reviews across:

  * BOA
  * CBE
  * Dashen
* Removed duplicates
* Cleaned null/empty reviews
* Standardized date formats
* Normalized text (lowercase, cleaned whitespace)

**Output:**
`ethiopian_bank_reviews.csv`

---

## 2️⃣ Sentiment Analysis

**Method:** VADER Sentiment Analyzer

### Classification:

* Positive → compound > 0.05
* Neutral → -0.05 ≤ compound ≤ 0.05
* Negative → compound < -0.05

### Results:

| Sentiment | Count |
| --------- | ----- |
| Positive  | 250   |
| Neutral   | 190   |
| Negative  | 59    |

Dashen shows the highest average sentiment score, indicating relatively stronger customer satisfaction.

---

## 3️⃣ Thematic Analysis

To identify key user concerns and satisfaction drivers:

* Extracted keywords (TF-IDF + noun extraction)
* Grouped into structured themes:

  * User Interface & Experience
  * Account Access Issues
  * Transaction Performance
  * Customer Support
  * Feature Requests
  * Technical Issues

### Key Insight:

UI/UX is the dominant satisfaction driver across all banks.
Technical stability and login issues appear as recurring pain points.

---

## 4️⃣ Database Integration (Task 3)

* Designed relational PostgreSQL schema
* Structured tables for banks and reviews
* Implemented safe insert logic
* Enforced constraints to prevent duplicates

This ensures scalable storage and future extensibility.

---

## 5️⃣ Insights & Recommendations (Task 4)

The analysis generated:

* Comparative sentiment distribution per bank
* Top themes per bank
* Identification of customer pain points
* Actionable recommendations for product teams

Example:

* Improve UI/UX consistency for BOA and CBE
* Investigate recurring login and bug-related complaints
* Maintain Dashen’s strong design advantage

---

# ⚙ Engineering Improvements (Capstone Enhancement)

To elevate this project beyond analysis:

### ✅ Modular Code Architecture

Refactored into `src/` structure for maintainability.

### ✅ Automated Testing

* 6 unit tests implemented using pytest
* Validates cleaning, sentiment classification, and theme extraction

### ✅ CI/CD Integration

GitHub Actions pipeline:

* Installs dependencies
* Runs tests automatically
* Prevents broken commits

This ensures reliability and reproducibility.

---

# 📊 Metrics of Success

* 100% of reviews classified into sentiment categories
* 0 failing unit tests
* CI/CD passing consistently
* No duplicate database records
* Insights reproducible across runs

---

# 🛠 How to Run

### 1️⃣ Create Environment

```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.\.venv\Scripts\activate       # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Pipeline

```bash
python -m src.scraping
python -m src.preprocessing
python -m src.sentiment
python -m src.themes
```

Or explore the notebooks for step-by-step analysis.

---

# 📈 Future Improvements

* Expand dataset to 1500+ reviews
* Implement advanced topic modeling (LDA / BERTopic)
* Deploy as REST API
* Build Streamlit dashboard for stakeholders
* Add performance benchmarks

---

# 👩‍💻 Author

**Kalkidan Asdesach**
AI & Data Engineering Enthusiast
10 Academy – AI Mastery Program

---

# 🌟 Why This Project Matters

This capstone demonstrates:

* End-to-end data pipeline design
* NLP for real-world business applications
* Database engineering
* Testing & CI/CD best practices
* Project planning and iteration

It reflects both **technical capability and engineering maturity**.

