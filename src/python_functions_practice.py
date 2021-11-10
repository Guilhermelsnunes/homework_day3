def return_10():
    return 10

def add(number1,number2):
    return number1+number2

def subtract(number1,number2):
    return number1-number2

def multiply(number1,number2):
    return number1*number2

def divide(number1,number2):
    return number1/number2

def length_of_string(string):
    return len(string)

def join_string(string_1,string_2):
    return string_1 + string_2 

def add_string_as_number(string_1,string_2):
    return int(string_1)+int(string_2)

months=["Marchtober","January","February","March","April","May","June","July","August",
"September","October","November","December"]
def number_to_full_month_name(number):
    return months[number]

def number_to_short_month_name(number):
    return months[number][0:3]
