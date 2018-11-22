import sys

'''
to be honest,Dijkstra has great similarity with Prim
when it comes to their difference,the biggest difference is their shortestDist:list.
Dijkstra's shortestDist:
	represents the distance of source(usually a vertex) with other vertices that haven't been visited
Prim's shortestDist:
	represents the distance of minimum spanning tree(MST) with other vertices that haven't been visited

After all,as these difference,they adopt a bit of different update rules
'''


def minVertices(visit, shortestDist):
	min = sys.maxsize
	minVertexID = -1
	for i in range(len(shortestDist)):
		if visit[i] == False and min > shortestDist[i]:
			min = shortestDist[i]
			minVertexID = i
	return minVertexID


def Dijkstra(Graph):
	visited = [False for num in range(len(Graph))]
	shortestDist = [sys.maxsize for num in range(len(Graph))]
	shortestDist[0] = 0
	for i in range(len(Graph)):
		minVertexID = minVertices(visited, shortestDist)
		visited[minVertexID] = True
		for v in range(len(Graph)):
			if visited[v] == False and shortestDist[v] > Graph[minVertexID][v] + shortestDist[minVertexID] and \
					Graph[minVertexID][v] != INF:
				shortestDist[v] = Graph[minVertexID][v] + shortestDist[minVertexID]
	print(shortestDist)


if __name__ == '__main__':
	NUM_V, NUM_E = map(int, input('Please input the number of Vertices and Edges:').split())

	INF = sys.maxsize
	Graph = [[INF for row in range(NUM_V)] for col in range(NUM_V)]
	for i in range(NUM_V):
		Graph[i][i] = 0
	for i in range(NUM_E):
		source, destination, weight = map(int, input('Please input Edge and its Weight:').split())
		Graph[source][destination] = weight
		Graph[destination][source] = weight
	Dijkstra(Graph)