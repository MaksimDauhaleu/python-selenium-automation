# Sum of Digits

# def sum_of_digits(given):
#     result = 0
#     for z in range(1, given+1):
#         result += z
#     # Edge case(given == 2)
#     if result == 1:
#         result = 1 + given
#     print(f'Result sum numbers from 1 to Given number is {result}')
#     # Edge case(Negative numbers)
#     y = 0
#     x = -20
#     while x != 0:
#         y += x
#         if x <= 0:
#             x += 1
#         else:
#             x -= 1
#     print(f'Result sum numbers from 1 to negative Given number is {abs(y)}')
#
#
# sum_of_digits(20)


# Maximum number out 3 Given

# def find_max_number(first, second, third):
#     if first > second and first > third:
#         print("First number is bigger")
#     elif second > first and second > third:
#         print("Second number is bigger")
#     elif first == second or first == third or second == third:
#         print("None of numbers are bigger")
#     else:
#         print("Third number is bigger")
#
#
# find_max_number(5, 200, 200)


# Count odd and even numbers

# def count_even_odd(given):
#     given_str = str(given)
#     even_number = 0
#     odd_numbers = 0
#     for x in range(len(given_str)):
#         if int(given_str[x]) % 2 == 0:
#             even_number += int(given_str[x])
#         else:
#             odd_numbers += int(given_str[x])
#     print(f'Even numbers sum = {even_number}, Odd numbers sum = {odd_numbers}')
#
#
# count_even_odd(34560)

