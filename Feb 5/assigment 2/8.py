# 8.Writing List to Files in Python
# Using write()
# Using writelines()
# Using String Join Along with “with open” syntax

# Using write()
data = ['line 1', 'line 2', 'line 3']
with open('Feb 5/assigment 2/8.txt', 'w') as file:
    for line in data:
        file.write(line + '\n')

# Using writelines()
with open('Feb 5/assigment 2/8.txt', 'w') as file:
    file.writelines("\n".join(data))

# Using String Join Along with “with open” syntax
with open('Feb 5/assigment 2/8.txt', 'w') as file:
    file.write("\n".join(data))
