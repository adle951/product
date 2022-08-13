product = []
#確認有無檔案
#讀取檔案
import os #oerating system
if os.path.isfile('product.csv'):
	print('有檔案')
	with open('product.csv', 'r', encoding ='utf-8') as f:
		for line in f:
			#(可替代下面一行)
			# s = line.strip().split(',')
			# name = s[0]
			# price = s[1] 
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
	print(product)
else:
	print('沒有檔案')

#二維清單
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

#存入檔案
with open('product.csv', 'w', encoding ='utf-8') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')