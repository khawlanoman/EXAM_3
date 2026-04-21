def ft_conv(number_str, from_base,to_base):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    try:
        if from_base < 2 or from_base > 36:
            return "ERROR"
        if to_base < 2 or to_base > 36:
            return "ERROR"
        
        number = int(number_str,from_base)
        out_put = ""
        if number == 0:
            return "0"
        
        while number > 0:
            rem = number % to_base
            out_put = digits[rem] + out_put
            number //= to_base
        
        out_put = out_put.upper()
        return out_put
    except Exception:
        return "ERROR"

# Basic conversions
print(ft_conv("1010", 2, 10))        # "10"
print(ft_conv("10", 10, 2) )        # "1010"
print(ft_conv("1A", 16, 10) )        # "26"
print(ft_conv("26", 10, 16)  )       # "1A"

print(ft_conv("123", 10, 10) )      # "123"

print(ft_conv("0", 10, 2)   )        # "0"
print(ft_conv("000", 2, 10) )        # "0"

print(ft_conv("ZZZ", 36, 10))        # "46655"
print(ft_conv("46655", 10, 36))      # "ZZZ"

print(ft_conv("A", 16, 10) )         # "10"
print(ft_conv("F", 16, 10)  )        # "15"

print(ft_conv("1F4", 16, 10))        # "500"
print(ft_conv("500", 10, 16) )       # "1F4"

print(ft_conv("2", 2, 10))           # Error / invalid input
print(ft_conv("G", 16, 10) )         # Error / invalid input