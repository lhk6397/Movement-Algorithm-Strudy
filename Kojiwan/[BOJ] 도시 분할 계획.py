def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
N, M = map(int, input().split()) # 집의 개수, 길의 개수
parent = [0] * (N + 1)

edges = []
result = 0

for i in range(1, N + 1):
  parent[i] = i
  
for _ in range(M):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()
max_cost = 0

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    max_cost = max(max_cost, cost)
    result += cost

print(result - max_cost)