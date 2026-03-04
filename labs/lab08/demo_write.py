# Demo: Writing text files

# Read
f = open("scores.txt", "r")
lines = f.readlines()
f.close()

# Process
scores = []
for line in lines:
    score = int(line.strip())
    scores.append(score)

average = sum(scores) / len(scores)

# Write
f = open("report.txt", "w")
f.write(f"Average: {average}\n")
f.close()