print("-------------")
print("📝 Quiz Game")
print("-------------")

score = 0
# 🧠 Dictionary of questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the largest country in the world by land area?": "Russia",
    "What is the smallest country in the world?": "Vatican City",
    "What is the highest mountain in the world?": "Mount Everest"
}

# 🎮 Loop through every question
for question,answer in questions.items():
    print("\n",question)
    user_answer = input("Your answer: ")

    if user_answer.lower().strip() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect!")
        print("The correct answer is:", answer)

print(f"Your total score is {score}/{len(questions)}")