def count_decimal_places(num):
    abs_num = abs(num)
    factor = 1
    if abs_num >=10:
        factor = 1
    elif abs_num>=1:
        factor = 10
    else:
        num_str = str(abs_num)
        decimal_part = num_str.split('.')[1]
        counter = 2
        for num_str in decimal_part:
           if num_str == '0':
              counter+=1
           else:
              break
        print(counter)
        factor = 10 ** counter
        print(factor)
    return factor
    

my_float = -0.0019888888
my_float = -0.0019888888
my_float = 1.232
print(count_decimal_places(my_float)*my_float)