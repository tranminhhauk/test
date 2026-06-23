def insert_element(array, num, index_):
    array.append(-1)
    for i in range(len(array)- 2, index_ - 2, -1):
        array[i+1] = array[i]
    array[index_ -1] = num
    print(array)
array = [1,2]
#insert_element(array, 6, 2)
# 1 2 3 4 5 
# 1 2 3 4 5 -1
# i = 4
# 1 2 3 4 5 5
# i = 3 
# 1 2 3 4 4 5
# i = 2
# 1 2 3 3 4 5
# i= 1
# 1 2 2 3 4 5 
# i = 0
# 1 1 2 3 4 5

def delete_element(array, index_at):
    for i in range(index_at -1, len(array)-1):
        array[i] = array[i+1] 
    print(array)
array = [1,2,3,4,5]
#delete_element(array, 3)
