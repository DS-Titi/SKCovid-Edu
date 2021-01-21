import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Helper function to compute polarity of each cell in CSV
def polarity(row):
    tweet = row.iloc[2]
    return round(TextBlob(tweet).sentiment.polarity,3)

# Compute sentiment of each row based on tweet
def save_sentiment(input_file, output_file):
    df = pd.read_csv(, encoding = "ISO-8859-1", delimiter=',', header=None)
    df[len(df.columns)+1] = df.apply(polarity, axis=1)
    df.to_csv(output_file, encoding = "ISO-8859-1", header=None)

# Plot histogram of the polarity values
def plot_polarity(data_source):
    df = pd.read_csv(data_source, encoding = "ISO-8859-1", delimiter=',', header=None)
    sentiment_df = df.iloc[:,[3,19]]
    fig, ax = plt.subplots(figsize=(8, 6))

    sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
                ax=ax,
                color="purple")

    plt.title("")
    plt.xlabel("Polarity")
    plt.ylabel("Frequency/Num. Tweets")
    plt.show()

if __name__ == "__main__":
    input_file = 'kovid_edu_2020_16k.csv'
    output_file = 'kovid_edu_polar_16k.csv'

    save_sentiment(input_file, output_file)
    plot_polarity(output_file)