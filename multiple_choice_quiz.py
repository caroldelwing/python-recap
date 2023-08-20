#Write an array of questions for your quiz
question_prompts = [
    "What color are stars?\n(a) Yellow\n(b) White\n(c) Colorful\n\n",
    "What is the best chocolate?\n(a) White\n(b) Dark\n(c) Milk\n\n",
    "What is the biggest city?\n(a) Toronto\n(b) Montreal\n(c) Vancouver\n\n"
]
#Write a Question class with prompt and answer
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#Create an array of object questions
questions = [Question(question_prompts[0], "c"),
             Question(question_prompts[1], "a"),
Question(question_prompts[2], "a")
                          ]
#Create a function to ask the user
def run_test(questions):
    score = 0
    for x in questions:
        answer = input(x.prompt)
        if answer == x.answer:
            score += 1
    print ("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)
