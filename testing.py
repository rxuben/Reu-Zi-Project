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

# Write the user's reaction time to the leaderboard file
with open('leaderboard.txt', 'r+') as file:
    lines = file.readlines()
    for i, q in enumerate(lines):
        if name in q:
            existing_value = float(q.split()[-2])  # Extract the existing time
            if length < existing_value:
                lines[i] = f"{name}'s Reaction time: {round(length, 2)} seconds\n"
            break
    else:  # This block executes if the loop completes without break
        lines.append(f"{name}'s Reaction time: {round(length, 2)} seconds\n")

    # Truncate the file and write the updated lines
    file.seek(0)
    file.truncate()
    file.writelines(lines)
