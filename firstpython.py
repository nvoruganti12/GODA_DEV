# Multiplication table for a specific number
num = int(input("Enter a number: "))

print(f"\nMultiplication Table for {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
