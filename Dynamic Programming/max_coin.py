def max_coin(coinValue):
	coinList = [0] * (len(coinValue) + 1)
	coinList[1] = coinValue[0]
	for i in range(2,len(coinValue)+1):
		coinList[i] = max(coinList[i - 1],coinValue[i - 1] + coinList[i - 2])
	return coinList.pop()

if __name__ == '__main__':
	coinValue = [2,5,9,12,3]
	print(max_coin(coinValue))