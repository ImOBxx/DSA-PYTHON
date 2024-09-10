def sumN(n):
    sum = 0
    for i in range(n):
        sum = sum + i
    return sum

n = int(input("Enter Number: "))
print("Sum Of Natural Number: ", sumN(n))