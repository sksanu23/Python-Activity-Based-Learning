
# Case Study 31: String-Based Examination Answer Evaluation

answer_key = ["A", "C", "B", "D", "A"]
total_questions = len(answer_key)

score = 0
correct = 0
incorrect = 0
unanswered = 0

print("Enter A, B, C, D, or press Enter to skip.")

for i in range(total_questions):
    while True:
        answer = input(
            f"Question {i + 1}: "
        ).strip().upper()

        if answer in ["A", "B", "C", "D", ""]:
            break

        print("Invalid answer. Enter A, B, C, D, or blank.")

    if answer == "":
        unanswered += 1
        print("Unanswered")
    elif answer == answer_key[i]:
        correct += 1
        score += 2
        print("Correct: +2 marks")
    else:
        incorrect += 1
        score -= 0.5
        print("Incorrect: -0.5 marks")

score = max(0, score)

print("\n--- EXAMINATION REPORT ---")
print("Total questions:", total_questions)
print("Correct answers:", correct)
print("Incorrect answers:", incorrect)
print("Unanswered:", unanswered)
print("Final score:", score, "out of", total_questions * 2)
