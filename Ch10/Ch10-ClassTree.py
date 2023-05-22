##[2진트리] Class 메서드를 생성하여 노드 검색
class Node:
    def __init__(self, value):  # self는 Node 자신 객체 의미 (__init__는 생성자 함수 의미, 객체 생성 시 자동 실행)
        self.value = value
        self.left = None
        self.right = None

    def get_node(self):
        if self.left is None:
            left = None
        else:
            left = self.left.value
        if self.right is None:
            right = None
        else:
            right = self.right.value
        return self.value, left, right

def in_order_traverse(node):
    if node is not None:
        in_order_traverse(node.left)  # 왼쪽 서브트리 중위 순회
        print(node.value, end=' ')  # 현재 노드 방문
        in_order_traverse(node.right)  # 오른쪽 서브트리 중위 순회

def pre_order_traverse(node):
    if node is not None:
        print(node.value, end=' ')  # 현재 노드 방문
        pre_order_traverse(node.left)  # 왼쪽 서브트리 전위 순회
        pre_order_traverse(node.right)  # 오른쪽 서브트리 전위 순회

def post_order_traverse(node):
    if node is not None:
        post_order_traverse(node.left)  # 왼쪽 서브트리 후위 순회
        post_order_traverse(node.right)  # 오른쪽 서브트리 후위 순회
        print(node.value, end=' ')  # 현재 노드 방문

root = Node('+')  # Node Class로 2진 트리 객체 root 생성하여 value 값을 '+'로 초기화
root.left = Node('3')  # root 객체의 left 변수에 새로운 노드를 초기화 하여 대입(연결)
root.right = Node('/')  # root 객체의 right 변수에 새로운 노드를 초기화 하여 대입(연결)
root.right.left = Node('*')
root.right.left.left = Node('3')
root.right.left.right = Node('5')
root.right.right = Node('3')

print("<In-Order>", end=' ')
in_order_traverse(root)  # left > root > right 순회
print("\n<Pre-Order>", end=' ')
pre_order_traverse(root)  # Root > left > right 순회
print("\n<Post-Order>", end=' ')
post_order_traverse(root)  # left > right > root 순회