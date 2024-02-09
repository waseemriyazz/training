 #Function to fetch all data from the file

def get_data():
    try:
        
        path = input("Enter file path : ")
        with open(path, "r", encoding="utf-8") as file:
            content = file.readlines()
            return content
    except Exception as e:
        print(e)
        return get_data()
    
    #Question class

class Question:
    def __init__(self, question_text, options, correct_answer, penalty, points) :
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.penalty = penalty
        self.points = points
        self.options = []
        for option in options:
            self.options.append(option)

        
    def __str__(self) -> str:
        return f"{self.question_text}, {self.options}, {self.correct_answer}, {self.penalty}, {self.points}"

raw_data = get_data()
question_object_list = []
# Making question objects from raw data and putting them in a list
for data in raw_data:

    question_answer = data.split('|')
    
    question_options = question_answer[0].split('/')
    

    question_text = question_options[0]
    correct_answer = question_answer[1].strip()
    options = []
    for i in range(1, 5):
        try:
            options.append(question_options[i])
        except:
            break
    

    if len(options) == 0:
        penalty = 0
        points = 2
    else:
        penalty = 1/4
        points = 1
    
    question_object = Question( question_text , options , correct_answer , penalty , points )
    question_object_list.append(question_object)


# game logic
    
score = 0

# getting one question at a time from the list and prompting it to the user

for question in question_object_list:

    
    print(question.question_text)
    for options in question.options:
        print(options)
    
    
    user_answer = input("Answer the above question : ")

    if user_answer.lower() == question.correct_answer.lower():
        print("You answered correctly")
        score = score + int(question.points)
    else:
        print("You answered incorrectly")
        score = score - float(question.penalty)
    
print("GAME OVER")
print(f"You scored {score}")





