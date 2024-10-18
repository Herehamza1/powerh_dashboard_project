# 2
questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What color do you get when you mix red and white?": "Pink",
    "what is your working?": "Job"
}

# score = 0

# for question, answer in questions.items():
#     user_answer = input(question + " ")
#     if user_answer.lower() == answer.lower():
#         score += 1
#         print("Correct!")
#     else:
#         print(f"Wrong! The correct answer is {answer}.")

# print(f"Your final score is: {score}/{len(questions)}")




score = 0
for questions, answer in questions.items():
    user_answer = input(questions + " ")
    if user_answer.lower() == answer.lower():
        score += 1
        print("corect answer:")
    else:
        print(f"wrong! the corect answer is {answer}")

print(f"the final score is : {answer}/{len(questions)}")



















