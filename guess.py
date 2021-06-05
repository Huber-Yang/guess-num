import random

r = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num > r:
		print('再小一點')
	elif num < r:
		print('再大一點')
	else:
		print('你猜中了!!!')
		print('這是你猜的', count, '次')
		break
	print('這是你猜的', count, '次')