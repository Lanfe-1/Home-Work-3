#home work 3.1

# v1

number1 = int(input("Enter first number...:"))
action1 = input("Enter action (+, -, *, /)...:")
number2 = int(input("Enter second number...:"))

if action1 == "+":
    print(number1 + number2)
elif action1 == "-":
    print(number1 - number2)
elif action1 == "*":
    print(number1 * number2)
elif action1 == "/":
    if number2 != 0:
       result = number1 / number2
    else:
       result = "Error"
else:
    result = "Error: Invalid action"
    print("Result:", result)

#v2

number1 = int(input("Enter first number...:"))
action1 = input("Enter action (+, -, *, /)...:")
number2 = int(input("Enter second number...:"))

match action1:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error"
    case _:
        result = "Error: Invalid action"
print("Result:", result)

#home work 3.2\ Перемістити елемент у списку

nums = [1, 2, 3, 4, 5]
if len(nums) > 0:
    nums.insert(0, nums[-1])
    nums.pop()
print(nums)

#home work 3.3\Розділити один список на два списки

nums = [1, 2, 3, 5]
middle_index = len(nums)// 2

if len(nums) % 2 != 0:
    middle_index += 1

part1 = nums[:middle_index]
part2 = nums[middle_index: ]
result = [part1 , part2]

print(result)












