

NUM_V,NUM_E = list(map(int,input().split()))
edges = []
for edge in range(NUM_E):
	node1,node2,cost = list(map(int,input().split()))
	edges.append((node1,node2,cost))

edges = sorted(edges,key=lambda edge: edge[2])

parent = [-1 for i in range(NUM_E)]
# initially,we assume that all vertices are roots,so parent's values are all -1
# parent:list is storing the root of every vertices
# if parent[vertices] == -1,it represents vertices is root
# if parent[vertices] != -1, it represents vertices is connected with parent[vertices] then keep finding its root
# for example:
# 0  1  2 3 4  5
#-1  2 -1 4 5 -1
# parent[0] = -1,it represents its root is itself,parent[1] = 2 it represents it connects with vertices 2,
# from parent[3]=4, parent[4]=5,parent[5]=-1,we can judge vertices 5 is root of vertices 3,4
# as you see vertices 0,2,5 they belong to different trees because their values of parent is -1
def find_root(vertices):
	if parent[vertices] != -1:
		vertices = find_root(parent[vertices])
	return vertices

MST = []
MST_cost = 0

for edge in edges:
	parent_a = find_root(edge[0])
	parent_b = find_root(edge[1])
# if parent_a == parent_b,it represents node1 and node2 have the same root.so they will be cyclic,continue
	if parent_a != parent_b:
		MST_cost += edge[2]
		MST.append(edge)
		parent[parent_a] = parent_b

print(MST_cost)
for edge in MST:
	print(edge)

#input data like:
'''
3 3
0 1 3
0 2 3
1 2 4
'''


