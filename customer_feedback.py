def feedback_cal(ratings):
    positive = 0
    if len(ratings) == 0:
        print("No feedback provided")
    elif 5 not in ratings or 4 not in ratings:
        print("No positive feedback provided")
    else:
        for i in ratings:
            if i == 5 or i == 4:
                positive = positive + 1
        print(f"Positive Feedback: {(positive / len(ratings)) * 100}%")


rating = [5, 4, 3, 5, 2, 4, 1, 5]
feedback_cal(rating)
