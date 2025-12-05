for day in range(1, 161+1):
    new_word = day
    # review_days = [1, 2, 4, 7, 15, 30, 60]
    # review_days = [1, 2, 4, 7, 14, 28, 56, 112, 224]
    review_days = [1, 3, 6, 12, 24, 40, 60, 90, 135]
    reviews = []
    for d in range(1, day):
        for offset in review_days[1:]:  # exclude first day which is new word
            if d + offset == day:
                reviews.append(d)
                break
    print(f"Day {day}: Learn word {new_word}, Review words: {reviews}")