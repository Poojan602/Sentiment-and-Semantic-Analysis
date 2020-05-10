# Sentiment-and-Semantic-Analysis
Sentiment and Semantic Analysis on twitter and news API respectively


  # Sentiment Analysis

## Data Cleaning
- Twitter data scraping can be found in the project <a href = "https://github.com/Poojan602/Extraction-Transform-Load">ETL</a>
- That scraped data was further cleaned. In cleaning, RT and usernames(starts with @) from tweets were removed. As there were some special characters left, those were cleaned also.

## Analysis
- Python script named wordcount.py was written which creates bag of words which can be found in Sentiment_Analysis/wordcount.py.
- Positive and negative words were downloaded from online sources and it was compared to the created bag of words.
- Based on the number of occurrence of positive and negative words in tweets, polarity was calculated and added column in cleaned csv file of tweeter API.
- Using tableau, most frequently occurred words in both positive and negative tweets collected were visualized as follows.


![Image](https://github.com/Poojan602/Sentiment-and-Semantic-Analysis/blob/master/Images/Word%20cloud.png)


# Semantic Analysis

## Process
- News API data were scraped and cleaned which can be found in the project <a href = "https://github.com/Poojan602/Extraction-Transform-Load">ETL</a>
- As there were 100 news articles, 100 different txt files were generated using python script. Each txt file has Title, Description and Content.
- And as per shown in pdf, 2 tables named 10_a and 10_b were generated using python files
- Also when running python file named semantic_analysis.py, it displays file name which has highest relative frequency
