def read_single_digit(a):
    number_list = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    print(number_list[a], end=" ") 
   
def read_number(prompt):
    number = str(prompt)

    if len(number) == 1:
        read_single_digit(int(number[0]))
    elif len(number) == 2:
        read_single_digit(int(number[0]))
        read_single_digit(int(number[1]))
    elif len(number) == 3:
        read_single_digit(int(number[0])) 
        read_single_digit(int(number[1]))
        read_single_digit(int(number[2]))
    else: pass
    
integer = int(input("세 자리 정수 입력: "))
if 0 <= integer <= 999:
    read_number(integer)
else: pass
