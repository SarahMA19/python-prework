#####  QUESTION 1 #####

def hello_name(user_name):
    print("Hello_" + user_name.upper() +"!")

hello_name('username')

#####  QUESTION 2 #####

def first_odds():
    for i in range(1, 100):
        if i %2 == 1:
            print(i)

print(first_odds())

##### QUESTION 3 #####

def max_num_in_list(a_list):
        a_list = [1, 2, 3, 4, 5]
        print(a_list[4])
        
max_num_in_list('max number')    

##### QUESTION 4 #####

def is_leap_year(a_year):
        if (a_year % 4) == 0:
            if (a_year % 100) == 0:
                if (a_year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
a_year = 2023
if (is_leap_year(a_year)):
    print('Leap Year')
else:
    print('Not a Leap Year')

##### QUESTION 5 #####

def is_consecutive(a_list):
    if len(set(a_list)) == len(a_list) and max(a_list) - min(a_list) == len(a_list) -1:
        return True
    else:
        return False

a_list = [1, 2, 3, 4, 5, 6]

print(is_consecutive(a_list))
