#二維清單
product = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入價格')
	#清單簡寫 p = [name, price] or product.append([name, price])
	p = []
	p.append(name)
	p.append(price)
	product.append(p)
print(product)
print(product[0][0])

for p in product:
	print(p[0], '價格是:', p[1])
print(p)