############ Define one function named cheese_and_crackers ##############
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f'You have {cheese_count} cheeses!')
    print(f'You have {boxes_of_crackers} boxes of crackers!')
    print(f'Man that\'s enough for a patry!')
    print(f'Get a blanket.\n')

######## Assign values to two variables of the function cheese_and_crackers #########
print('We can just give the funtcion numbers directly:')
cheese_and_crackers(20,30)

############# Define teo new variables of the function cheese_and_crackers#############
print('O,we can use variables from our script:')
amount_of_cheese = 10
amount_of_crackers = 50

######### Call the function ##########
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

######## Call the funciton after adding ##########
print('We can even do math inside too:')
cheese_and_crackers(10 + 20,5 + 6)


print('And we combine the two,variables and math:')
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)


