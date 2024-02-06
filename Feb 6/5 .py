# 5.Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
def lines_and_words(filepath):

    with open(filepath, "r")as file:
        lines = file.readlines()
    
        print(f"The number of lines in file situated at path {filepath} is : {len(lines)}")

        words_count = 0
        for line in lines:
            words = line.split(" ")
            words_count = words_count + int(len(words))
        print(f"The number of words in file situated at path {filepath} is : {words_count}")
path = input("Enter file path:")
lines_and_words(path)