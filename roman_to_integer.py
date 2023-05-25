#Convert Roman to Integer
def convert(roman):
    roman_to_int = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    size = len(roman) - 1
    i = size
    final_result = 0
    while(i >= 0):
        if (i < size) and roman_to_int[roman[i]] < roman_to_int[roman[i + 1]]:
            final_result -= roman_to_int[roman[i]]
        else:
            final_result += roman_to_int[roman[i]]
        i -= 1
    print(final_result)

roman_input = str(input("Roman to Integer: "))
convert(roman_input.upper())
