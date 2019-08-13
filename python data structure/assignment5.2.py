# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


# 입력한 숫자 중에서 가장 큰 수와 가장 작은 수 출력하는 프로그램 만들어라
# 사용자가 done을 입력하기 전까지는 계속해서 숫자를 입력해라


largest = None
smallest = None

while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
    except:
        print ("Invalid input")
    else:
        if smallest is None:
            smallest = num
            largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

print ("Maximum is", int(largest))
print ("Minimum is", int(smallest))
