def common_elements(list1, list2):
    return list(set(list1) & set(list2))


l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
print(common_elements(l1, l2))  
