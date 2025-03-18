def exchange(a):
    q = a // 500
    w = (a-500*q)//100 
    r = (a-500*q-100*w)//50
    s = (a-500*q-100*w-50*r)//10
    print(f"500원 동전의 개수: {q}")
    print(f"100원 동전의 개수: {w}")
    print(f"50원 동전의 개수: {r}")
    print(f"10원 동전의 개수: {s}")

def get_integer(prompt):
    return int(input(prompt))

cost = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(cost)