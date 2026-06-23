class ListNode:
    def __init__(self, value: int, next):
        self.val = value
        self.next = next
    
def print_linked_list(head: ListNode):
    if head: # head is not None
        curr = head
        while curr: # curr is not None
            print(f"-> {curr.val} ")
            break
def add_node(head: ListNode, val: int, index_at: int):
    if index_at <= 0:
        print(f"Invalid index: {index_at}. Because the linked list is now empty")
        return
    if head is None:
        if index_at == 1: # linked list is empty and want at the first
            return ListNode(val, next=None)
        else: 
            print(f"Invalid index: {index_at}. Because the linked list is now empty")
    else:
        is_successfuly_add = False
        curr = head
        position = 1
        while curr: # curr is not None
            if index_at == 1:
                new_node = ListNode(val, next = head)
                return new_node
            if position == index_at - 1:
                new_node = ListNode(val, next = curr.next)
                curr.next = new_node
                is_successfuly_add = True
                pass
            curr = curr.next
            position += 1
        if is_successfuly_add is True:
            return head
        else:
            print("don't add, no index_at")
def middle(head: ListNode):
    if head is None:
        print('Linked list now empty')
        return
    else:
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1
            if curr is None:
                break
        print(size)
        size_list = int((size /2) + 1)
        print(size_list)
        curr = head
        size_curr = 1
        while curr:
            size_curr += 1
            curr = curr.next
            if size_curr == size_list:
                return curr
            
        
node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(0, node1)
#print_linked_list(head)
head = middle(head)
print_linked_list(head)









# #class Node:
#     def __init__(self, val: int, next = None):
#         self.val = val
#         self.next = next
# def print_linkedlist(head: Node):
#     if head:
#         curr = head
#         while curr:
#             print(curr.val, end = " -> ")
#             curr = curr.next
#             pass
#         print('None')
# def delete_node(head, index_):
#     if head is None:
#         print('Linkedlist is now empty')
#         return None
#     if index_ < 0:
#         print('Invalid index')
#         return head
#     if index_ == 0:
#         head = head.next
#         print('Deleted at index 0')
#         return head
#     else:
#         curr = head
#         position = 0
#         while curr.next and position < index_ -1:
#             curr = curr.next
#             position += 1
#         if curr.next is None:
#             print(f'Invalid index {index_}')
#             return head
#         curr.next = curr.next.next  
#         print(f'Deleted node at {index_}')
#         return head
# # nod4 = Node(4, None)
# # nod3 = Node(3, nod4)
# # nod2 = Node(2, nod3)
# # nod1 = Node(1, nod2)
# # head = Node(0, nod1)
# # print_linkedlist(head)
# # delete_node(head, 4)
# # print_linkedlist(head)



# def is_cycle(head):
#     if head is None and head.next is None:
#         return False
#     curr = head
#     prev = head
#     while prev and prev.next:
#         curr = curr.next
#         prev = prev.next.next
#         if curr == prev:
#             return True
#     return False
# head = is_cycle(head)
# print(head
