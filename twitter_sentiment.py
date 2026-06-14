import pandas as pd
import snscrape.modules.twitter as sntwitter
from textblob import TextBlob
import matplotlib.pyplot as plt

# Collect tweets
tweets = []

query = "iphone"

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    tweets.append(tweet.rawContent)

    if len(tweets) == 100:
        break

# Create DataFrame
df = pd.DataFrame(tweets, columns=["Tweet"])

# Sentiment function
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Analyze sentiment
df["Sentiment"] = df["Tweet"].apply(get_sentiment)

# Save results
df.to_csv("twitter_sentiment_results.csv", index=False)

# Count sentiments
counts = df["Sentiment"].value_counts()

print(counts)

# Pie Chart
plt.pie(
    counts,
    labels=counts.index,
    autopct="%1.1f%%"
)

plt.title("Twitter Sentiment Analysis")
plt.show()
