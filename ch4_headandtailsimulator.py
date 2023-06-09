import random

# Practise question that counts number of times a streak of 6 heads or tails occurs in 10 000 coin flips

number_of_streaks = 0
result = []

for flip in range(10000):
    observation = random.randint(0, 1)
    result.append(observation)

    if flip >= 5:  # Ensures check only occurs on 6th flip onwards
        streak_check = sum(result[flip-5:flip+1])
        if streak_check == 0 or streak_check == 6:
            number_of_streaks += 1

print(f"Number of Heads: {10000 - sum(result)}")
print(f"Number of Tails: {sum(result)}")
print(f"Number of Streaks: {number_of_streaks}")
