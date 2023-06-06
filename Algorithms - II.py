# def split_in_half_1(string):
#     first_half_string = ''
#     second_half_string = ''
#     for i in range(0, len(string)):
#         if len(string) % 2 == 0 and len(string) / 2 <= i:
#             first_half_string += string[i]
#         elif len(string) % 2 != 0 and len(string) / 2 < i:
#             first_half_string += string[i]
#         else:
#             second_half_string += string[i]
#     new_string = first_half_string + second_half_string
#
#     print(new_string)
#
#
# split_in_half_1('123456789')
#
#
# def split_in_half_2(string):
#     new_string = ''
#     str_len = len(string) / 2
#     if len(string) % 2 != 0:
#         new_string += string[int(str_len)+1:len(string)]
#         new_string += string[0:int(str_len)+1]
#     else:
#         new_string += string[int(str_len):len(string)]
#         new_string += string[0:int(str_len)]
#     print(new_string)
#
#
# split_in_half_2('123456789')
#

# def unique_characters(string):
#     for i in range(len(string)):
#         for y in range(i+1, len(string)):
#             if string[i] == string[y]:
#                 return False
#     return True
#
# print(unique_characters('mabcds'))
