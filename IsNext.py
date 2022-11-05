import sys

def IsNext():
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation.lower() == "no":
            real_choice = input("Are you sure? (yes/no): ")

            if real_choice.lower() == "yes":
                sys.exit("Exit the Calculator.") #프로그램 종료
            elif real_choice.lower() == "no":
                continue #다시 질문
            else: #잘못된 입력
                print("Invalid Input, Try again.")
                continue

        elif next_calculation.lower() == "yes":
            break #다음 계산 진행

        else: #잘못된 입력
            print("Invalid Input, Try again. ")
            continue

#다음 계산 진행, 잘못된 입력에 대한 로그(비정상입력) 수정 필요!!
