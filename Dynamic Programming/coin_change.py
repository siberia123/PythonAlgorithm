

def coin_change(coin_value, change):
	table = [0] * (change + 1)
	for i in range(1, change + 1):
		temp = change
		j = 0
		while j < len(coin_value) and i >= coin_value[j]:
			temp = min(table[i - coin_value[j]], temp)
			j += 1
		table[i] = temp + 1
	return table.pop()


if __name__ == '__main__':
	coin_value = [1, 5, 10, 25]
	change = 63
	print(coin_change(coin_value, change))


