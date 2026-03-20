import sys

input = sys.stdin.readline

computer_count = int(input())
pair_count = int(input())

graph = [[] for _ in range(computer_count + 1)]
visited = [False] * (computer_count + 1)

for _ in range(pair_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

dfs(1)

print(sum(visited) - 1)