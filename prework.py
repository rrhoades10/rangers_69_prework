
# Print Username
def hello_name(user_name):
    print("Hello, " + user_name.title() + "!")
# hello_name("Ryan is Cool")

# odd numbers betwen 1 and 100


def odd_numbers():
    for num in range(2, 101, 2):
        print(num)

# print(odd_numbers())


def even_numbers():
    for num in range(1, 100, 2):
        if num % 2 != 0:
            print(num)

# print(even_numbers())

# 3. max number in a list
# def max_num_in_list(a_list):
#     max = a_list[0]
#     for x in a_list:
#         if x > max:
#             max = x
#     return max
# print(max_num_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def max_num_in_list(a_list):
    max = 0
    for x in a_list:
        if x > max:
            max = x
    return max


# print(max_num_in_list([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))


def max_in_list(a_list):
    a_list.sort()
    new_list = sorted(a_list)

    print(a_list[-1])


# print(max_in_list([2, 1, 6, 4, 8, 3, 10, 27]))

def max_num(a_list):
    print(max(a_list))

# print(max_num([2,6,5,7,8,1,2,100]))

#


def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False


# print(is_leap_year(2008))

# a_year = int(input('a_year'))
#


def is_leap_year2(a_year):
    leap_year = False
    if a_year % 400 == 0:
        leap_year = True
    elif a_year % 100 == 0:
        leap_year = False
    elif a_year % 4 == 0:
        leap_year = True
    if leap_year == True:
        print(str(a_year) + " is a leap year!")
    else:
        print(str(a_year) + " is not a leap year.")

    prompt = "\n Is this a leap year?"
    prompt += "\n Please enter a year: "
    test_year = int(input(prompt))


# is_leap_year2(test_year)


# print(is_leap_year2(2008))

# consecutive numbers

def is_consecutive(a_list):
    x = a_list[0] - 1
    for number in a_list:
        if number == x + 1:
            number = x
            return True
        else:
            return False


# print(is_consecutive([2, 1, 7, 8, 1, 17]))

def is_consecutive(a_list):
    a_list = sorted(a_list)
    for index in range(len(a_list)):
        if a_list[index] == a_list[-1]:
            x = "True"
        elif a_list[index] + 1 == a_list[index + 1]:
            continue
        else:
            x = "False"
            break
    return x


print(is_consecutive([1, 2, 3, 4, 5, 6]))


