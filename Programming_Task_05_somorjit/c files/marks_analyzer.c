marks = []

for i in range(5):
    mark = float(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark)

print("\nHighest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))
