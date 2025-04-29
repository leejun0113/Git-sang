shopping_bag = {}

print('[구입]')

while True:
    item_name = input('상품명? ')

    if item_name == '':
        break
    else:
        item_amount = int(input('수량은? '))
        shopping_bag[item_name] = item_amount
        print(f'장바구니에 {item_name} {item_amount}개가 담겼습니다. \n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')

print('\n[검색]')
search_item = input('장바구니에서 확인하고자 하는 상품은? ')

if search_item in shopping_bag:
    find_item = shopping_bag[search_item]
    print(f'{search_item}은(는) {find_item}개 담겨 있습니다.')
else:
    pass
