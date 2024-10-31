import pandas as pd
import nltk 
import pyodbc 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
nltk.download('vader_lexicon')
#Define a function to fetch data from a SQL database using a SQL query 
def fetch_data_from_sql(): 
    # Define the connection string with parameters for the database connection
    conn_str = ( 
        "Driver={SQL SERVER};"
        "Server=LAPTOP-NE4OP95K;"
        "Database=PortfolioProject_MarketingAnalytics;"
        "Trusted_Connection=yes;")
    # Establish the connection to the database
    conn=pyodbc.connect(conn_str)
    # The query you need to make
    query="SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText from customer_reviews"
    # Execute the query and fetch the data into a DataFrame in Python
    df= pd.read_sql(query, conn)
    conn.close()
    return df 
customer_reviews_df=fetch_data_from_sql()

sia=SentimentIntensityAnalyzer()

def calculate_sentiment(review): 
    sentiment = sia.polarity_scores(review)
    return sentiment['compound']
def categorize_sentiment(score,rating): 
    if score>0.05: 
        if rating>=4: 
            return "Positive"
        elif rating == 3: 
            return "Mixed Positive"
        else:
            return "Mixed Negative"
    elif score <= -0.05: 
        if rating <= 2:
            return "Negative"
        elif rating == 3: 
            return "Mixed Negative"
        else:
            return "Mixed Positive"
    else: 
        if rating >= 4: 
            return "Positive"
        elif rating <= 2: 
            return "Negative"
        else:
            return "Neutral"
def sentiment_bucket(score): 
    if score >= 0.5: 
        return "0.5 to 1.0"
    elif 0.0 <= score <= 0.5: 
        return "0.0 to 0.49"
    elif -0.5 <= score <=0.0: 
        return "-0.49 to 0.0"
    else:
        return "-1.0 to -0.5"
customer_reviews_df["SentimentScore"] = customer_reviews_df["ReviewText"].apply(calculate_sentiment)
customer_reviews_df["SentimentCategory"]=customer_reviews_df.apply(
    lambda row: categorize_sentiment(row["SentimentScore"],row["Rating"]), axis=1)
customer_reviews_df["SentimentBucket"] = customer_reviews_df["SentimentScore"].apply(sentiment_bucket)

print(customer_reviews_df.head())
customer_reviews_df.to_csv("customer_reviews_with_sentiment.csv", index=False)