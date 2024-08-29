from textblob import TextBlob

# Example text
text = "I love programming in Python. It's so intuitive and fun!"

# Create a TextBlob object
blob = TextBlob(text)

# Get the sentiment
sentiment = blob.sentiment

# Print the sentiment polarity and subjectivity
print(f"Sentiment Polarity: {sentiment.polarity}")  # Output: 0.5 (Positive)
print(f"Sentiment Subjectivity: {sentiment.subjectivity}")  # Output: 0.6 (Subjective)

#Explanation:

#Polarity: Ranges from -1 (negative) to 1 (positive).
#Subjectivity: Ranges from 0 (objective) to 1 (subjective).
