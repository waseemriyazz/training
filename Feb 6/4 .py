# 4.Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below. Note that the autograder
# does not have support for the sorted() function.

with open("Feb 6/mbox-short.txt", "r")as file :
    lines = file.readlines()
for line in lines:
    
    
    if line[0:5]=='From ':
        
        words = line.split(" ")
        
        print(words)
        