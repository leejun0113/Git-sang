def get_fixed_price(price):
    global discount_rate
    result = int(price * (100/(100-discount_rate)))
    return result

discount_rate = int(input("할인율은? "))
a_discounted_price = int(input("A 상품의 할인된 가격은? "))
b_discounted_price = int(input("B 상품의 할인된 가격은? "))
a_price = get_fixed_price(a_discounted_price)
b_price = get_fixed_price(b_discounted_price)
print(f"A 상품의 정가는 {a_price} 원")
print(f"B 상품의 정가는 {b_price} 원")