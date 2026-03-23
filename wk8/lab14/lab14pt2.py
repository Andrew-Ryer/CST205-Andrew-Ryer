#Task 4
import matplotlib.pyplot as plt

# reference: https://docs.python.org/3/library/collections.html
from collections import Counter

# import your stuff from lab14.py
from lab14 import book_text, get_clean_words

# Run clean up function on book text
words = get_clean_words(book_text)

# count words / build in Counter
counts = Counter(words)

# choose top 5 / build in Counter
top_5 = counts.most_common(5)

# convert to a dictionary
top_words = {word: count for word, count in top_5}

# Make to bar graph
plt.bar(list(top_words.keys()), list(top_words.values()))
plt.title("Top 5 Words in Wuthering Heights Chapter 1")
plt.ylabel("Count")
plt.xlabel("Words")
plt.show()