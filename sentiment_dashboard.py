import pandas as pd
import streamlit as st

# Load the saved final_df
@st.cache_data
def load_data():
    return pd.read_csv('/Users/haeunyoon/Desktop/SCHOOL/Spring 2025/MANAGING DATA/summarized_yelp_reviews.csv')

df = load_data()

st.title("📊 Yelp Review Sentiment Dashboard")

# Sidebar filters
st.sidebar.header("Filter Reviews")

# Dropdown for city
cities = df['city'].dropna().unique()
selected_city = st.sidebar.selectbox("Select a City", sorted(cities))

# Dropdown for attributes (based on string search)
attribute_input = st.sidebar.text_input("Search for Attribute or Category (optional)")

# Filter by city
filtered_df = df[df['city'] == selected_city]

# Optional: further filter by keyword in 'attributes' or 'categories'
if attribute_input:
    filtered_df = filtered_df[
        filtered_df['attributes'].astype(str).str.contains(attribute_input, case=False, na=False) |
        filtered_df['summary'].astype(str).str.contains(attribute_input, case=False, na=False)
    ]

# Show sentiment results
if not filtered_df.empty:
    avg_sentiment = filtered_df['sentiment_score'].mean().round(3)
    st.metric(label="Average Sentiment Score (−1 to 1)", value=avg_sentiment)

    st.write("### 🔍 Sample Summarized Reviews")
    st.dataframe(filtered_df[['name', 'summary', 'sentiment_score']].sort_values(by='sentiment_score', ascending=False).head(10))
else:
    st.warning("No results for the selected filters.")
