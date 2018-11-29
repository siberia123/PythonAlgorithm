def heapify(list,index,length):
	largest = index
	left_index = 2 * index + 1
	right_index = 2 * index + 2
	if left_index < length and list[largest] < list[left_index]:
		largest = left_index
	if right_index < length and list[largest] < list[right_index]:
		largest = right_index
	if largest != index:
		list[index],list[largest] = list[largest],list[index]
		heapify(list,largest,length) #up to bottom

def heap_sort(list):
	length =len(list)
	# first,create a max heap
	for i in range(length // 2 -1,-1,-1):
		heapify(list,i,length) # bottom to up
	# a max heap have been made,so now we can heap sort
	for i in range(length - 1,0,-1):
		list[0],list[i] = list[i],list[0]
		heapify(list,0,i) # up to bottom

if __name__ == '__main__':
	list = list(map(int,input().split()))
	heap_sort(list)
	print(list)