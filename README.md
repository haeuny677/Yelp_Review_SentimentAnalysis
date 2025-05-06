# Yelp_Review_SentimentAnalysis
This project uses Yelp JSON data in a Streamlit app to analyze review sentiment, predict sentiment by business type, and visualize user networks. It helps business owners understand feedback and improve performance on Yelp.

🔍 Key Business Questions:
How do features like review counts, check-ins, and amenities impact customer ratings?

What is the sentiment of customer reviews—and can it predict future performance?

What cities and business categories receive the most reviews?

How are customers interconnected (friends/fans), and which categories are co-reviewed?

🧠 Steps Taken:
Data Sourcing & Cleaning:

Source: Yelp Open Dataset

Data Types: Business, Reviews, Users, Check-ins

Preprocessing done using Python (PySpark) and stored using PostgreSQL

Database Integration:

Combined JSON files into PostgreSQL for structured querying

Used Neo4j to build relationship graphs (reviewers’ friends, fans, businesses)

Sentiment Analysis:

Used TextBlob to assign sentiment scores to individual reviews

Averaged sentiment by location/category

Modeled by HaEun Yoon

Text Summarization:

Used T5-small transformer model to generate concise summaries of long reviews

Explored future upgrade to BERT for enhanced summarization

Predictive Modeling:

Features: Wi-Fi, parking, food category, review count, check-ins, sentiment score

Models Tested: Linear Regression (best), Random Forest, Gradient Boosting

Conducted using PySpark

Visualization:

Neo4j used for real-time influencer graphs and network mapping

Streamlit used to build an interactive dashboard

