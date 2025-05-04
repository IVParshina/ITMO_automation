def append_list(mylist: list):
    mylist.append('test')
    return mylist

print(append_list(['one', 1, 2]))

def sum_list(mylist: list) -> int:
    result = 0
    for elem in mylist:
        result = result + elem
    return result

print(sum_list([1, 2, 3]))


