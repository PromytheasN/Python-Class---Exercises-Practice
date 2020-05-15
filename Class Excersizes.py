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

