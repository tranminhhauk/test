class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(1)
root.left.right = Node(9)
root.right.left = Node(14)
root.right.right = Node(19)
# def inodertraversa(root):
#     result = []
#     def inoder(node):
#         if node is None:
#             return []
#         inoder(node.left)
#         result.append(node.data)
#         inoder(node.right)
#     inoder(root)
#     return result

# def preorderTraversal(root):
#     result = []
#     def preorder(node):
#         if node is None:
#             return
#         result.append(node.data)
#         preorder(node.left)
#         preorder(node.right)
#     preorder(root)
#     return result

# def postorderTraversal(root):
#     result = []
#     def postorder(node):
#         if node is None:
#             return
#         postorder(node.left)
#         postorder(node.right)
#         result.append(node.data)
#     postorder(root)
#     return result

# def  maxDepth(root):
#     if root is None:
#         return 0
#     left = maxDepth(root.left)
#     right = maxDepth(root.right)
#     return 1 + max(left, right)
# print(maxDepth(root))

def inoderTraversal(root):
    result = []
    stack = []  
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.data)
        curr = curr.right
    return result
#print(inoderTraversal(root))

def preorder(root):
    result = []
    stack = [root]  
    if root is None:
        return []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:  
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
# print(preorder(root))

def postorderTraversal(root):
    stack1 = [root]
    stack2 = []
    result = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        node = stack2.pop()
        result.append(node.data)
    return result
# print(postorderTraversal(root))
def levelorder(root):
    if not root:
        return []
    result = []
    list = [root]
    while list:
        node = list.pop(0)
        result.append(node.data)
        if node.left:
            list.append(node.left)
        if node.right:
            list.append(node.right)
    return result
# print(levelorder(root))
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    new_node = TreeNode(data)
    if root is None:
        root = new_node
        return root
    node = root
    while True:
        if data < root.data:
            if node.left is None:
                node.left = new_node
                break
            node = node.left
        elif data > root.data:
            if node.right is None:
                node.right = new_node
                break
            node = node.right
        else:
            return 'data is existed'
            
    return root
def inoder(root):   
    result = []
    def ino(node):
        if root is None:
            return
        ino(node.left)
        result.append(node.data)
        ino(node.right)
    ino(root)
    return result
def insert_at_position(root, val, position):
    if root is None:
        if position == 1:
            return TreeNode(val)
        else:
            return 'Tree is None'
    if position == 1:
        new_node = TreeNode(val)
        new_node.left = root
        return new_node
    queue = [root]
    pos = 1
    while queue:
        node = queue.pop(0)
        pos += 1
        if pos == position:
            new_node = TreeNode(val)
            new_node.left = node.left
            node.left = new_node
            return root
        if node.left:
            queue.append(node.left)
        if pos == position:
            new_node = TreeNode(val)
            new_node.right = node.right
            node.right = new_node
            return root
        if node.right:
            queue.append(node.right)
def delete(root, val)       :
    if root is None:
        return None
    if val < root.data:
        root.left = delete(root.left, val)
    elif val > root.data:
        root.right = delete(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        replace = root.right
        while replace.left:
            replace = replace.left
        root.data = replace.data
        root.right = delete(root.right, replace.data)
    return root 
def pathSum(root, target):
    if root is None:
        return 0
    if not root.left and not root.right:
        return root.data == target
    new_target = target - root.data
    pathSum(root.left, new_target) or pathSum(root.right, new_target)
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data, end = ' ')
        print_tree(root.right)
print_tree(root)    
