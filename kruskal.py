

NUM_V,NUM_E = list(map(int,input().split()))
edges = []
for edge in range(NUM_E):
	node1,node2,cost = list(map(int,input().split()))
	edges.append((node1,node2,cost))

edges = sorted(edges,key=lambda edge: edge[2])

parent = [-1 for i in range(NUM_E)]

def find_root(vertices):
	if parent[vertices] != -1:
		vertices = find_root(parent[vertices])
	return vertices

MST = []
MST_cost = 0

for edge in edges:
	parent_a = find_root(edge[0])
	parent_b = find_root(edge[1])
	if parent_a != parent_b:
		MST_cost += edge[2]
		MST.append(edge)
		parent[parent_a] = parent_b

print(MST_cost)
for edge in MST:
	print(edge)


