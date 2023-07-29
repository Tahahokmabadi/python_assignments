hour_a = int(input("Enter the hour: "))
minute_a = int(input("Enter the minute: "))
second_a = int(input("Enter the second: "))
print()
hour_b = int(input("Enter the hour: "))
minute_b = int(input("Enter the minute: "))
second_b = int(input("Enter the second: "))

while True:  
    choice = int(input("sum or sub(1, 2): "))
    if choice == 1 or 2:
       break
    else:
       print("number should be 1 or 2.")

def sum(hour_a,minute_a,second_a,hour_b,minute_b,second_b):
    hour_sum = hour_a + hour_b
    minute_sum = minute_a + minute_b
    second_sum = second_a + second_b

    while True:
        if second_sum >= 60:
            second_sum -= 60
            minute_sum += 1
        else:
            break
    while True:
            if minute_sum >= 60:
                minute_sum -= 60
                hour_sum += 1
            else:
                break
    print(f"The sum is {hour_sum} hours, {minute_sum} minutes, and {second_sum} seconds.")

def sub(hour_a,minute_a,second_a,hour_b,minute_b,second_b):
    hour_sub = hour_a - hour_b
    minute_sub = minute_a - minute_b
    second_sub = second_a - second_b
    while True:
        if second_sub < 0:
            minute_sub -= 1
            second_sub += 60
        else:
            break
    while True:
        if minute_sub < 0:
            hour -= 1
            minute_sub += 60
        else:
            break
    print(f"The sub is {hour_sub} hours, {minute_sub} minutes, and {second_sub} seconds.")

if choice == 1:
    sum(hour_a,minute_a,second_a,hour_b,minute_b,second_b)
else :
    sub(hour_a,minute_a,second_a,hour_b,minute_b,second_b)