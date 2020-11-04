import sys

token_hex = sys.argv[1]
split_count = 2
token_hex_array = [token_hex[i:i+split_count] for i in range(0, len(token_hex), split_count)]

letter_index = 0
flag = ""
for hex_value in token_hex_array:
    if abs(letter_index) == 25:
        break
    letter_value = int(hex_value, 16)
    letter = chr(letter_index + letter_value)
    flag += letter
    letter_index -= 1

print(flag)
