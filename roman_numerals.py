def romanToInt(s: str) -> int : 
   
   roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

   result = roman_numerals[s[0]]

   for i in range (len(s) - 1):
        if (roman_numerals[s[i]] < roman_numerals[s[i + 1]]):
            result += roman_numerals[s[i + 1]] - (roman_numerals[s[i]] * 2)
        else :
            result += roman_numerals[s[i + 1]]

   return result


print(romanToInt("LVIII"))