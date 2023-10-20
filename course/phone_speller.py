phone = "+33265987412"
result = ""

digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

for digit in phone:
    result += digits_mapping.get(digit, "[Character not mapped]") + ' '

result.trim
print(result)