def int_input(num):
    while float(num).is_integer() == False:
        print("정수만 입력 받을 수 있습니다.")
        num = float(input("다시 입력해주세요: "))
    return int(num)

def vending(num):
    if num % 2 == 0:
        print("짝수입니다.")
        vendinglist = [str(i) for i in range(num, num+18, 2)]
        print(', '.join(vendinglist))
    else:
        print("홀수입니다.")
        vendinglist = [str(i) for i in range(num, num+18, 2)]
        print(', '.join(vendinglist))

if __name__ == '__main__':
    while True:
        num = input("숫자를 입력해주세요: ")
        if num == ".":
            print("프로그램을 종료합니다.")
            break
        else:
             vending(int_input(num))


