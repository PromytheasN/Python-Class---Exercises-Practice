#1. Write a Python class to convert an integer to a roman numeral.

class RomanNumeral:
    
    def transformation(self, num):
        integ = [1000, 900, 500, 400,
                 100, 90, 50, 40,
                 10, 9, 5, 4,
                 1]
        roman = ["M", "CM", "D", "CD",
                 "C", "XC", "L", "XL",
                 "X", "IX", "V", "IV",
                 "I"]
        
        roman_num = ""
        i = 0
        while num > 0:
            for x in range(num//integ[i]):
                num -= integ[i]
                roman_num += roman[i]
            i += 1
                
        return roman_num
      
      #you can test it by calling the class like this.
      #print(RomanNumeral().transformation(number))
      #where number is a random number eg 550

