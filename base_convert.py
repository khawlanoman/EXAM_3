def convert_to_decimal(numbert_str,base):
        if base < 2 and base > 36:
                return "error, base invalid"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbert_str = numbert_str.upper()
        sign = 1
        value = 0
        if numbert_str[0] == '-':
                sign = -1
                numbert_str = numbert_str[1:]
        
        for i in numbert_str:
                if i not in digits:
                        return "error,invalid input"
                digit = digits.index(i)
                if digit >= base:
                       return "error,invalid input"
                value = value * base + digit
        return sign * value

def convert_from_decimal(number, base):
        if base < 2 and base > 36:
                return "error, base invalid"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        out_put = ""
        if number == 0:
                return "0"
        if number < 0:
            sign = "-"
            number *= -1
        else:
               sign = ""
        
        while number > 0:
            rem = number % base
            out_put = digits[rem] + out_put
            number //= base

        return sign + out_put

def convert_base(numbert_str, from_base, to_base):
       
       number = convert_to_decimal(numbert_str, from_base)
       if isinstance(number, str):
              return number
       return convert_from_decimal(number, to_base)


print(convert_base("1010", 2, 10))        # "10"
print(convert_base("10", 10, 2))        # "1010"
print(convert_base("1A", 16, 10))     # "26"
print(convert_base("26", 10, 16))         # "1A"



# Same base
print(convert_base("123", 10, 10))    # "123"

# Edge cases
print(convert_base("0", 10, 2))      # "0"
print(convert_base("000", 2, 10))        # "0"

# Larger bases
print(convert_base("ZZZ", 36, 10))    # "46655"
print(convert_base("46655", 10, 36))  # "ZZZ"

# Uppercase handling
print(convert_base("A", 16, 10))       # "10"
print(convert_base("F", 16, 10))        # "15"

# Mixed digits and letters
print(convert_base("1F4", 16, 10))      # "500"
print(convert_base("500", 10, 16))     # "1F4"

# Invalid cases 
print(convert_base("2", 2, 10))        # Error / invalid input
print(convert_base("G", 16, 10))       # Error / invalid input