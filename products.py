products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products)
for p in products:#for loop 把清單中的東西一個個拿出來
	print(p[0], '的價格是', p[1])