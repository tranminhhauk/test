def twosum(num, target):
    n = len(num)
    for i in range(n):
        for j in range(i+1, n):
            if num[i] + num[j]== target:
                return [i, j]
a = [([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),    
    ([3, 3], 6),]
for num, target in a:
    result = twosum(num, target)
    #print(result)


def count_character(s) -> dict: # "aabc" => a 
    result = dict()
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def isEqual(s, t):
    for char in result_s:
        if char not in result_t:
            return 's!= t'
        elif result_s[char] != result_t[char]:
            return 's != t'
    return 's=t'


s = 'aaac'
result_s = count_character(s)
print(result_s)
t = 'cbbba'
result_t = count_character(t)
print(result_t)
final_result = isEqual(result_s, result_t)
print(final_result)
