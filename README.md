# 📊 Yelp Review Sentiment Analysis

This project leverages the Yelp Open Dataset to build an interactive Streamlit app that helps business owners understand customer feedback, predict sentiment trends, and visualize user connections. It combines NLP, predictive modeling, and network analysis to deliver actionable insights.

## 🎯 Objective
To analyze Yelp reviews for sentiment, identify influential reviewers, and predict customer satisfaction using business attributes and engagement metrics.

## 🔍 Key Business Questions
- How do review counts, check-ins, and amenities impact customer ratings?
- What is the overall sentiment of customer reviews, and can it predict performance?
- Which cities and business categories receive the most reviews?
- How are users interconnected, and what categories are commonly co-reviewed?

## 🧠 Steps Taken

### 🗂 Data Sourcing & Cleaning
- **Source:** Yelp Open Dataset
- **Data Types:** Business, Reviews, Users, Check-ins
- **Processing:** Cleaned and loaded data into **PostgreSQL** using **Python** and **PySpark**

### 🧱 Database Integration
- Combined JSON files into a relational schema using PostgreSQL
- Constructed user-business-review relationships
- Built user connection graphs in **Neo4j** (friends, fans, influencers)

### 💬 Sentiment Analysis
- Performed sentiment scoring on individual reviews using **TextBlob**
- Aggregated sentiment scores by business location and category
- Analysis led by **HaEun Yoon**

### ✂️ Text Summarization
- Used **T5-small** transformer model to summarize long reviews
- Future potential: upgrading to **BERT** for improved contextual summaries

### 🤖 Predictive Modeling
- **Features Used:** Wi-Fi availability, parking, food category, review count, check-ins, sentiment score
- **Models Tested:** Linear Regression (best performer), Random Forest, Gradient Boosting
- Built and evaluated models using **PySpark**

### 📊 Visualization
- **Neo4j:** Mapped reviewer influence and user networks
- **Streamlit App:** Deployed interactive dashboard for business insights

## 🧰 Tools & Technologies
- **Languages:** Python, PySpark, SQL
- **Database:** PostgreSQL
- **Modeling & NLP:** TextBlob, Hugging Face T5, scikit-learn
- **Graph DB:** Neo4j
- **Dashboard:** Streamlit

---

> 👨‍💻 Developed by HaEun Yoon and team — as part of Columbia University's Applied Analytics program
