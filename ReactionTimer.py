import time
import random

# Random amount of time before a star is printed
x = random.uniform(1, 3)
time.sleep(x)
print("*")

# Timer is started and waits for any input before stopping the timer
start = time.time()
input()
end = time.time()

# Reaction time (length) is recorded
length = end - start

name = input("What is your name? ")
print(f"{name}'s reaction time is {round(length, 2)} seconds")

# Create leaderboard
with open('leaderboard.txt', 'r+') as file:
    lines = file.readlines()
    for q in enumerate(lines):
        if name in q:
            existing_value = float(q.split()[-2])
            if length < existing_value:
                lines[q] = f"{name}'s reaction time: {round(length, 2)} seconds\n"
            break
    else:
        lines.append(f"{name}'s Reaction time: {round(length, 2)} seconds\n")

    lines.sort(key=lambda line: float(line.split()[-2]))

    file.seek(0)
    file.truncate()
    file.writelines(lines)