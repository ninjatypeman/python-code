shop_list = []  # 列表
for i in range(5):  # 添加5件商品到列表中
    goods = input("Please input the id and goods' name:")
    shop_list.append(goods)

for item in shop_list:
    print(item)

shop_cart = []
while True:
    flag = False  # 列表里面是否存在某个商品
    num = input(
        'Please input the id of the good that you wanna add to shopping cart: ')

    for item in shop_list:
        if num == item[0:4]:  # 切片，获取前四个字符
            flag = True
            shop_cart.append(item)
            print('Added!')
            break  # 跳出for循环

    if not flag and num != 'q':  # 列表里面没有输入的商品 id，并且输入不是 q 时
        print('The good you input not exist!')

    if num == 'q':  # 输入为q时
        break  # 跳出while

print('Goods in your cart: ')
shop_cart.reverse()
for item in shop_cart:
    print(item)
