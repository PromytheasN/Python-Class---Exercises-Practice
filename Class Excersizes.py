#1. Write a Python class to convert an integer to a roman numeral.

class Converter:
    
    def conv_processor(self,num):
        
        values = [1000,900,500,400,
                  100,90,50,40,
                  10,9,5,4,
                  1]
        numerals = ["M","CM","D","CD",
                    "C","XC","L","XL",
                    "X","IX","V","IV",
                    "I"]
        
        i = 0
        roman_num =[]
        while num > 0:
            
            for x in range(num//values[i]):
                
                roman_num += numerals[i]
                num -= values[i]
            i += 1
        return "".join(roman_num)
    
      #you can test it by calling the class like this.
      #print(Converter().conv_processor(num))
      #where num can be a random number eg 550
    
#Write a Python class to convert a roman numeral to an integer:

class Conv_Numeral_Processor:
    
    
    def num_processor(self, roman):
            
        roman_values = { 'I': 1,
                         'IV': 4,
                         'V': 5,
                         'IX': 9,
                         'X': 10,
                         'XL': 40,
                         'L': 50,
                         'XC': 90,
                         'C': 100,
                         'CD': 400,
                         'D': 500,
                         'CM': 900,
                         'M': 1000}

        integ_value = 0
        
        for i in range(len(roman)):
            if i>0 and roman_values[roman[i]] > roman_values[roman[i-1]]:
                
                integ_value += roman_values[roman[i]] - 2*roman_values[roman[i-1]]
            else:
                integ_value += roman_values[roman[i]]
            
        return integ_value
                         
#Call it like this:
#Conv_Numeral_Processor().num_processor("roman")
#Where at roman you insert the roman numeral eg CDXLV


