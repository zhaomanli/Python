# 现在我们要输入更多的变量并把它们打印出来。这次我们将用一个叫做“格式字符串”的东西。每次你用
# 引号把一段文本引起来，你就是在创建一个字符串。字符串是你让计算机呈现给人看的内容。你可以打
# 印字符串、把字符串保存到文件、或者发送到网络服务器等等。
# 字符串真的非常方便。你将在这个练习中学习如何创建包含变量的字符串。把你需要的变量放在 {} 里
# 面就可以把变量嵌入在字符串中。你还需要在字符串前面加上字母 f （代表 format），比如
#  f"Hello, {somevar}" 。双引号前面的 f 是为了告诉 python3： “这个字符串需要被格式化，把这些变
# 量放在那儿。”

def inTocmFunction():
    my_height = float(input('enter your height: '))
    unit = input('enter the unit: ')
    if unit == 'in':
        print(my_height,my_height * 2.54)
    elif unit == 'cm':
        print(my_height,my_height / 2.54)
    else:
        print('enter invalid')
    return my_height

def ponudsToKilograms():
    my_weight = float(input('Enter your weight: '))
    unit = input('Enter the unit: ')
    if unit == 'pd':
        print(my_weight,my_weight / 2.2)
    elif unit == 'kg':
        print(my_weight,my_weight * 2.2)
    else:
        print('enter invalid')
    return my_weight

my_name = 'Aed A. Shaw'
my_age = 35  #not a lie
my_height = inTocmFunction() #inches
my_weight = ponudsToKilograms() #pounds
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usally {my_teeth} depending on the coffee.")

#This line is tricky,try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age},{my_height},{my_weight} I get {total}.")


# ###########The translation between 'inch' and 'cm'#########
# value = float(input('Please enter length: '))
# unit = input('Please enter unit: ')
# if unit == 'in':
#     print(value,value * 2.54)
# elif unit == 'cm':
#     print(value,value / 2.54)
# else:
#     print('input invalid.')


# ###########The translation between 'pounds' and 'lilograms'#########
# def poundsTokilograms(pounds):
#     kilograms = pounds / 2.2
#     return kilograms
# pounds = float(input('Your weight is: '))
# kilograms = poundsTokilograms(pounds)
# print('Your weight in kilograms is: ' + str(kilograms))



##########XuXiaoDi's version##################
my_name = 'Aed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #pounds
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print('Let\'s talk about',my_name)
print(f"He's {int(my_height*2.54)} cm tall.")
print(f"He's {int(my_weight/2.2)} kg heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usally {my_teeth} depending on the coffee.")

#This line is tricky,try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age},{int(my_height*2.54)},{int(my_weight/2.2)} I get {total}.")

# my_name = 'Aed A. Shaw'
# my_age = 35 #not a lie
# my_height_inch = 74 #inches
# my_height = int(my_height_inch*2.54) #cm
# my_weight_pd = 180 #pounds
# my_weight = int(my_weight_pd/2.2) #kg
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'

# print(f"Let's talk about {my_name}.")
# print(f"He's {my_height} cm tall.")
# print(f"He's {my_weight} kg heavy.")
# print(f"Actually that's not too heavy.")
# print(f"He's got {my_eyes} eyes and {my_hair} hair.")
# print(f"His teeth are usally {my_teeth} depending on the coffee.")

# #This line is tricky,try to get it exactly right
# total = my_age + my_height + my_weight
# print(f"If I add {my_age},{my_height},{my_weight} I get {total}.")
