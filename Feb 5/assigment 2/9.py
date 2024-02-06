# 9.[poem.txt]contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.
from collections import Counter

with open('Feb 5/assigment 2/poem.txt', 'r') as file:
    words = file.read().split()

word_counts = Counter(words)
print(Counter.__dir__)
print(dir())

print(word_counts.get)
max_occurred_word = max(word_counts, key=word_counts.get)

print(f'The word with the maximum occurrence is: {max_occurred_word}')


