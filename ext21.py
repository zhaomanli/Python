
# def add(a,b):
#     print(f'ADDING {a} + {b}')
#     return a + b

# def subtract(a,b):
#     print(f'SUBTRACTING {a} - {b}')
#     return a - b

# def multiply(a,b):
#     print(f'MULTIPLY {a} * {b}')
#     return a * b

# def divide(a,b):
#     print(f'DIVIDED {a} / {b}')
#     return a / b

# print('Let\'s do some math with just functions!')

# age = add(30,5)
# height = subtract(78,4)
# weight = multiply(90,2)
# iq = divide(100,2)

# print(f'Age:{age},height{height},weight:{weight},IQ:{iq}')

# ## A puzzle for the extra credit,type it in anway.
# print('Here is a puzzle.')

# what = add(age,subtract(height,multiply(weight,divide(iq,2))))

# print('That becomes: ',what,'Can you do it by hand?')



def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a,b):
    return a / b

A = subtract(add(24,divide(34,100)),1023)
print(A)
