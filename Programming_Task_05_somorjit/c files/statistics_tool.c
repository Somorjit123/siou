numbers = []

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)
total = sum(numbers)
average = total / len(numbers)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nLargest Number:", largest)
print("Smallest Number:", smallest)
print("Sum:", total)
print("Average:", average)
print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)
