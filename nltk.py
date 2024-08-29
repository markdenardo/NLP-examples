#Tokenization using nltk

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK data
nltk.download('punkt')

# Example text
text = "Natural Language Processing (NLP) is fascinating. It enables machines to understand human language."

# Sentence tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word tokenization
words = word_tokenize(text)
print("Words:", words)

# Explanation:

# Sentence Tokenization: Breaks down text into sentences.
# Word Tokenization: Breaks down text into words.
