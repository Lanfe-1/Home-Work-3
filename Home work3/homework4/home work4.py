

# home work 4.1
numbers = [0, 1, 0, 12, 3]
result = []
while numbers:
    minimum = min(numbers)
    numbers.remove(minimum)
    if minimum != numbers :
        result.append(minimum)
result += [0] * numbers.count(0)
print(result)

numbers = [0]
result = []
while numbers:
    minimum = min(numbers)
    numbers.remove(minimum)
    if minimum != numbers :
        result.append(minimum)
result += [0] * numbers.count(0)
print(result)

numbers = [1, 0, 13, 0, 0, 0, 5]
result = []
while numbers:
    minimum = min(numbers)
    numbers.remove(minimum)
    if minimum != numbers :
        result.append(minimum)
result += [0] * numbers.count(0)
print(result)

numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = []
while numbers:
    minimum = min(numbers)
    numbers.remove(minimum)
    if minimum != numbers :
        result.append(minimum)
result += [0] * numbers.count(0)
print(result)

####################################


# # home work 4.3
import random
NUMS_SIZE = 3
numbers = []
for i in range(NUMS_SIZE):
    numbers.append(random.randint(1, 10))
print(numbers)
new_numbers = [numbers [0], numbers [2], numbers [-2]]
print(new_numbers)


# home work 4.2
numbers = []
print ("Список чисел:", numbers)

if numbers:
     even_sum = sum(numbers[i] for i in range(0, len(numbers), 2))
     result = even_sum * numbers[-1]
else:
    result = 0
print("Результат:", result)



