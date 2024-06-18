def reduce(function, iterable, start_val):
    accum = start_val 
    
    for val in iterable:
        accum = function(val, accum)
    
    return accum

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))     # 300

numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV