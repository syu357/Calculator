import arithmetic_op
import IsNext

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3): ")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except: #입력이 float가 아닐 경우
            print("Enter only number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", arithmetic_op.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", arithmetic_op.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", arithmetic_op.multiply(num1, num2))
            
        elif choice =='4':
            print(num1, "/", num2, "=", arithmetic_op.divide(num1,num2))
            
        IsNext.IsNext() #다음 계산을 계속 할 것인지 물어보는 함수

    else: # 1, 2, 3, 4 외 입력
        print("Invalid Input, Try again.")
