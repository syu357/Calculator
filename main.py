import arithmetic_op
import IsNext

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    choice = input("Enter choice(1/2/3): ")

    f = open("C:/Users/윤서연/Desktop/오픈소스소프트웨어개발/중간대체과제/Calc_log.txt", "a") #계산 로그 저장용 파일 open

    if choice in ('1', '2', '3', '4'):
    
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except: #입력이 float가 아닐 경우
                print("Enter only number.")
                continue

        if choice == '1':
            result = arithmetic_op.add(num1, num2)
            printresult = str(num1) + " + " + str(num2) + " = " + str(result)

        elif choice == '2':
            result = arithmetic_op.subtract(num1, num2)
            printresult = str(num1) + " - " + str(num2) + " = " + str(result)

        elif choice == '3':
            result = arithmetic_op.multiply(num1, num2)
            printresult = str(num1) + " * " + str(num2) + " = " + str(result)

        elif choice == '4':
            result = arithmetic_op.divide(num1, num2)
            if result == 0:
                printresult = "Can't be divided by zero."
            else:
                printresult = str(num1) + " / " + str(num2) + " = " + str(result)

        print(printresult) #콘솔창에 연산 결과 출력
        f.write(printresult + '\n') #계산 로그 파일에 연산 결과 저장

        IsNext.IsNext() #다음 계산을 계속 할 것인지 물어보는 함수

    else: # 1, 2, 3, 4 외 입력
        print("Invalid Input, Try again.")
        printresult = "Invalid Input: " + str(choice) #콘솔창에 잘못된 입력 결과 출력
        f.write(printresult + '\n') #계산 로그 파일에 잘못된 입력 결과 저장

    f.close() #파일 닫기
