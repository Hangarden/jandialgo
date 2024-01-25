# 전우순회는 부모노드 -> 왼쪽노드 -> 오른쪽노드 순으로 탐색하는데 왼쪽 노드가 존재한다면
# 부모노드를 출력하고 왼쪽노드를 부모노드로 해서 다시 탐색합니다 따라서 부모 -> 왼쪽 -> 오른쪽으로 탐색합니다
def predorder(nodes, idx):

    if idx < len(nodes):
        # 전위의 경우

        # 부모노드 출력
        print(nodes[idx], end = " ")
        # 왼쪽 노드 재귀 탐색 왼쪽 노드으 인덱스는 부모노드 * 2 + 1 이다.
        predorder(nodes, (idx*2) + 1 )
        # 왼쪽 노드 재귀 탐색 오른쪽 노드으 인덱스는 부모노드 * 2 + 2 이다.
        predorder(nodes, (idx*2) + 2 )
    else:
        return


# 중위순회는 왼쪽 -> 부모 -> 오른쪽 순으로 탐색한다. 왼쪽 노드에 값이 있다면
# 왼쪽노드를 부모노드로해서 계속 탐색합니다 차이점은 부모노드를 방문하지 않고 지나친다 는 것 입니다
def inorder(nodes, idx):

    if idx < len(nodes):
        # 전위의 경우

        # 왼쪽 노드 재귀 탐색 왼쪽 노드으 인덱스는 부모노드 * 2 + 1 이다.
        inorder(nodes, (idx*2) + 1 )
        # 부모노드 출력
        print(nodes[idx], end = " ")
        # 왼쪽 노드 재귀 탐색 오른쪽 노드으 인덱스는 부모노드 * 2 + 2 이다.
        inorder(nodes, (idx*2) + 2 )
    else:
        return

# 후위순회는 왼쪽 -> 오른쪽 -> 브모 순으로 탐색한다. 왼쪽 노드에 값이 있다면
# 왼쪽노드를 부모노드로해서 계속 탐색합니다 차이점은 왼 -> 오 -> 부 순서인 것입니다. 따라서 오른쪽에 왼, 오 노드가 있다면 해당 노드를 우선으로 탐색할 것 입니다.
def postorder(nodes, idx):

    if idx < len(nodes):
        # 전위의 경우

        # 왼쪽 노드 재귀 탐색 왼쪽 노드으 인덱스는 부모노드 * 2 + 1 이다.
        postorder(nodes, (idx*2) + 1 )
        # 왼쪽 노드 재귀 탐색 오른쪽 노드으 인덱스는 부모노드 * 2 + 2 이다.
        postorder(nodes, (idx*2) + 2 )
        # 부모노드 출력
        print(nodes[idx], end = " ")
    else:
        return

def solution(nodes):
    predorder(nodes, 0)
    print()
    inorder(nodes, 0)
    print()
    postorder(nodes, 0)


solution([1,2,3,4,5,6,7])