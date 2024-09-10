

def fbuzz(n):
    x = []  # Create a local list
    for i in range(1, n + 1):
        x.append(i)
    return x

def buzzbuzz(x):
    result = []  # Create a new list for the FizzBuzz result
    for i in x:
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)  # Keep the original number if no condition matches
    return result

n = int(input("Enter Number: "))

x = fbuzz(n)

print(buzzbuzz(x))
