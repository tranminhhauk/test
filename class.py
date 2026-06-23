            # class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#     def prepend(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         new_node.next = self.head
#         self.head = new_node
#     def print_(self):
#         curr = self.head
#         while curr:
#             print(curr.data, end = ' -> ')
#             curr = curr.next
#         print('None')

# #ll.print_()

# class linkedlist():
#     def __init__(self):
#         self.head = None
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node
#     def print__(self):
#         curr = self.head
#         while curr:
#             print(curr.data, end = ' -> ')
#             curr = curr.next
#         print('None')


# class Count:
#     def __init__(self):
#         self.head = None
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node
#     def search(self,data):
#         curr = self.head
#         index = 0
#         while curr is not None:
#             if curr.data == data:
#                 return index
#             curr = curr.next
#             index += 1    
#         return -1
#     def print__(self):
#         curr = self.head
#         while curr is not None:
#             print(curr.data, end = ' -> ')
#             curr = curr.next
#         print("None")
        
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class llist:
#     def __init__(self):
#         self.head = None
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node
#     def dele(self, data):
#         if self.head is None:
#             print('Danh sách rỗng')
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#         curr = self.head
#         while curr.next is not None:
#             if curr.next.data == data:
#                 curr.next = curr.next.next
#                 return
#             curr = curr.next
#     def prin(self):
#         curr = self.head
#         while curr is not None:
#             print(curr.data, end = ' -> ')
#             curr = curr.next
#         print('None')
# class ListNode:
#     def __init__(self, data: int, next = None):
#         self.data = data
#         self.next = next
# def print_llist(head):
#     if head:
#         curr = head
#         while curr:
#             print(curr.data, end = " -> ")
#             curr = curr.next
#         print('None')
# def add_node(head, data, index_):
#     if index_ <= 0:
#         print('Invalid index')
#         return 
#     if head is None:
#         if index_ == 1:
#             return ListNode(data, next = None)
#         else:
#             print('Invalid index, linked list empty')
#     else:
#         is_success = False
#         curr = head
#         position = 0
#         while curr:
#             if index_ == 1:
#                 new_node = ListNode(data, next = None)
#                 return new_node
#             if position == index_ - 1:
#                 new_node = ListNode(data, next = curr.next)
#                 curr.next  = new_node
#                 is_success = True
#             curr = curr.next
#             position += 1
#         if is_success is True:
#             return head
#         else:
#             print('Dont add, no index_ at')
#         pass


# Node4 = ListNode(4, None)
# Node3 = ListNode(3, Node4)
# Node2 = ListNode(2, Node3)
# Node1 = ListNode(1, Node2)
# head = ListNode(0, Node1)
# print_llist(head)
# add_node(head, 5, 3)
# print_llist(head)


# def isPalindrome(s, i, j):
#     while i < j:
#         if s[i] !=  s[j]:
#             return False
#         i += 1
#         j -= 1
#     return True
# def validPalindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             check1 = isPalindrome(s, left + 1, right)
#             check2 = isPalindrome(s, left, right -1)
#             return check1 or check2
#         left += 1
#         right -= 1
#     return True
# s = "aca"
# print(validPalindrome(s))  

class LinkedList:
    def __init__(self, val, next= None):
        self.val = val
        self.next = next
def print_Linked_list(head):
        if head:
            curr = head
            while curr:
                print(curr.val)
                break

                
def find_last_kth_element(head, k):
    if head is None:
        return None
    curr = head
    size = 1
    while curr.next:
        curr = curr.next
        size += 1
    if k > size or k <= 0:
        print("'k' out of index")
        return
    else:
        len_linkedlist = (size - k ) + 1
        pos = 1
        prev = head
        while prev:
            prev= prev.next
            pos += 1
            if pos == len_linkedlist:
                return prev 
def find_last_kth(head, k):
    if k <= 0:
        print("'k' out index")
        return 
    position = 1
    curr = head
    while curr:
        curr = curr.next
        position += 1
        if position == k:
            break
    if k > position:
        print("'k' out index")
        return
    slow = head
    fast = curr
    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow

        
        
def reverse(head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
def middle(head):
    if head is None:
        print('Linked list is now empty')
        return
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
def cycle(head):
    if head is None:
        print('linked list empty')
        return
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
# def palindrome(head):
#     if head is None:
#         print('linked list empty')
#         return
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     curr = slow
#     prev = None
#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp
#     left = head
#     right = prev
#     while right:
#         if left.val != right.val:
#             return False
#         left = left.next
#         right = right.next
#     return True
node4 = LinkedList(4, None)
node3 = LinkedList(3, node4)
node2 = LinkedList(2, node3)
node1 = LinkedList(1, node2)
head = LinkedList(0, node1)
# # print_Linked_list(head)
# h = find_last_kth(head, 4)
# print_Linked_list(h)

class FileReader:
    def __init__(self):
        self.name_file = input('Nhap file: ')
    def reader_file(self):
        with open(self.name_file, 'r', encoding= 'utf-8') as file:
            return file.read()
    def reader_file_list(self):
        with open(self.name_file, 'r', encoding= 'utf-8') as file:
            return file.readlines()
    def reader_file_lines(self, n):
        lines = self.reader_file_list()
        if n >= 1 and n <= len(lines):
            return lines[n-1]
        return 'empty'
    def write_file(self, val):
        with open(self.name_file, 'w',encoding= 'utf-8' ) as file:
            file.write(val)
    def delete_lines(self, val):
        lines = self.reader_file_list()
        if 1 <= val <= len(lines):
            lines.pop(val-1)
            self.write_file(''.join(lines))
    def delete(self, val):
        new_val = self.reader_file()
        new_val = new_val.replace(val, '')
        self.write_file(new_val)
    def update(self, last, now):
        new = self.reader_file()
        new = new.replace(last, now)
        self.write_file(new)
    def append(self, val):
        with open(self.name_file, 'a', encoding= 'utf-8') as file:
            file.write(val)
    def find_char(self, char):
        file = self.reader_file().split()
        count = 0
        for i in file:
            if i == char:
                count += 1
        return count
    def find_char_at(self, char):
        read = self.reader_file()
        count = 0
        i = 0
        while i < len(read):
            if read[i:i+len(char)] == char:
                count += 1
                i += len(char)
            else:
                count = 0
        return count
# reader = FileReader()
# print(reader.reader_file_list())
# reader.delete('123')
# print(reader.find_char('hel'))
# print(reader.find_char('hel'))
# print(reader.reader_file())
# print(readerreader_file())
# document = []
def reader_file():
    with open('monHoc.txt','r', encoding= 'utf-8') as file:
        document = file.read()
    return document
def count_character(document_text):
    word = document_text.lower()
    # sentences = word.split()
    count = {}
    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
data = reader_file()
result = count_character(data)
print(result)