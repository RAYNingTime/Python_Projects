#Recursion
def rec(n):
    if n == 0:
        return []
    return rec(n-1) + [n]

print(rec(5))

#Tail Recursion
def rec_tail(n, acc = []):
    if n == 0:
        return acc
    return rec_tail(n-1, acc + [n])

print(rec_tail(5))

#Second version with test
def recursion(numbers, index=0):
    if index == len(numbers):
        return 0
    return numbers[index] + recursion(numbers, index + 1)

def tail_recursion(numbers, index=0, total=0):
    if index == len(numbers):
        return total
    return tail_recursion(numbers, index + 1, total + numbers[index])

numbers = [1, 2, 3, 4, 5]

sum_recursion = recursion(numbers)
sum_tail_recursion = tail_recursion(numbers)

print("Sum (recursion): ", sum_recursion)
print("Sum (tail recursion): ", sum_tail_recursion)
