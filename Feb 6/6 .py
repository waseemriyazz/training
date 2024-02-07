# 6.Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
from collections import Counter


def word_count_tuples(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Convert the Counter object to a list of tuples and sort it in descending order of counts
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_counts
selection = int(input("Enter your choice \n 1 to input a string \n 2 to input a file path \n"))
if selection == 1:
    string = input("Enter string: ")
    print(word_count_tuples(string))
elif selection == 2:
    path = input("Enetr file path: ")
    with open(path, "r")as file:
        content = file.read()
        print(word_count_tuples(content))
else:
    print("incorrect input entered.")


