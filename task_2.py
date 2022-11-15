def from_list_to_dict(arr):
    return {num: arr.count(num) for num in arr}



assert (from_list_to_dict([1])) == {1: 1}
assert (from_list_to_dict([0, 0, 0, 0])) == {0: 4}
assert (from_list_to_dict([1, 2, 3, 1, 3, 5])) == {1: 2, 2: 1, 3: 2, 5: 1}
assert (from_list_to_dict([1, -1, 1.1, 1.1, 10, 100, 100, 100])) == {1: 1, -1: 1, 1.1: 2, 10: 1, 100: 3}
