# dfs 함수 구현
def dfs(G,v,m): # G = 그래프 v = 현재 노드 m = 방문여부 리스트
    # 현재 노드 방문처리하기
    m[v] = 1
    # 방문노드 출력은 이 위치에서!
    print(v)

    # 인접노드 탐색 시작
    # 2차원 리스트의 v번째 행 = v와 인접한 노드 저장
    for i in G[v]:
        # v와 인접한 노드 중 하나인 i가 미방문(0)이라면
        if not m[i]:
            # i부터 dfs 탐색
            dfs(G,i,m)
            # 이제 이 G[i]에 있는 노드를 탐색하고(for k in G[i])
            # if문에서 false로 걸리면(방문한 노드면)
            # 그냥 for 의미없이 돌다가 계속 리턴(스택 pop)하다 종료

# 그래프 G 생성 (인접 리스트)
# 노드 수 만큼 2차원 리스트의 행이 있어야 함. 비었음 빈 리스트로 꼭 채워넣기!
# 안 그럼 for 돌 때 out of range 오류남
G = [
    [], # 0번 노드가 없으면 비움
    [2,3,8], # 각 행 별로 꼭 정렬할 필요는 없으나,
    [1,7], # 관행적으로 작은 노드부터 순회하기에 정렬하는 게 좋대
    [1,4,5], # 문제 조건 잘 보고 정렬할말 결정하기!
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 방문여부 리스트 생성
m = [0]*9 # 9는 여기서 주어진 노드 수 8개 + 계산편의를 위한 0번까지 한 것

# dfs 실행
# 그래프 G에서 1번 노드부터 dfs 탐색
dfs(G,1,m)