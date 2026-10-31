number =int(input("enter a number:"))
count = 0
while number !=0:
    number = number // 10
    count = count + 1
print("number of digit:",count)    