def knapSack(val_list,wt_list,W,n):
	K = [[0 for i in range(W + 1)] for i in range(n + 1)]
	for item in range(n + 1):
		for wt in range(W + 1):
			if item == 0 or wt == 0:
				K[item][wt] = 0
			elif wt > wt_list[item - 1]:
				K[item][wt] = max(K[item - 1][wt],K[item - 1][wt - wt_list[item - 1]] + val_list[item - 1])
			else:
				K[item][wt] = K[item - 1][wt]
	return K[n][W]

if __name__ == '__main__':
	val_list = [44,12,23,54,22,51]
	wt_list = [6,10,12,14,9,18]
	n = 6
	W = 30
	print(knapSack(val_list,wt_list,W,n))