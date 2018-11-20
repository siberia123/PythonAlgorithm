import sys
'''
first,we should know some variables:
visited:	sign which vertex has been visited,it means it cannot used next time
shortestDist:	it record the shortest distance that the MST away from outside vertices,whichever vertices from.
				distinguish it from Dijkstra
MST:	the key role,it will record the shortest vertex
'''

class Graph(object):
	def __init__(self,numOfVertices):
		self.NUM_V = numOfVertices
		self.graph = [[0 for col in range(self.NUM_V)] for row in range(self.NUM_V)]

	# first all,we should find the shortest distance from shortestDist,then we will return the shortest one
	def minVertexValues(self,visited,shortestDist):
		min = sys.maxsize
		minVertex = 0
		for vertex in range(self.NUM_V):
			if visited[vertex] == False and min > shortestDist[vertex]:
				min = shortestDist[vertex]
				minVertex = vertex
		return minVertex

	def prim(self):
		# initially,visited are all False,which means all vertices are not being visited
		visited = [False] * self.NUM_V
		# shortestDist are all infinity(INF)
		shortestDist = [sys.maxsize] * self.NUM_V
		# we first start from 0 vertex
		shortestDist[0] = 0
		MST = [-1] * self.NUM_V

		for count in range(self.NUM_V):
			minVertex = self.minVertexValues(visited,shortestDist)
			visited[minVertex] = True
			# update the shortDist
			for vertex in range(self.NUM_V):
				if visited[vertex] == False and shortestDist[vertex] > self.graph[minVertex][vertex]:
					shortestDist[vertex] = self.graph[minVertex][vertex]
					MST[vertex] = minVertex

		self.print(MST)

	def print(self,MST):
		print('  edge\t\tweight')
		for i in range(1,self.NUM_V):
			print(MST[i],'\t',i,'\t\t',self.graph[i][MST[i]])

if __name__ == '__main__':
	g = Graph(5)
	INF = sys.maxsize
	g.graph = [[INF, 5, 7, INF, 2],
			   [5, INF, INF, 6, 3],
			   [7, INF, INF, 4, 4],
			   [INF, 6, 4, INF, 5],
			   [2, 3, 4, 5, INF]]
	g.prim()
