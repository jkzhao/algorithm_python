
def linear_search(data_set, value):
    '''顺序查找'''
    for i in range(len(data_set)):
        if data_set[i] == value:
            return i
    return -1

def bin_search(li, val):
    '''二分查找'''
    low = 0
    high = len(li) - 1
    while low <= high:  # 候选区有值
        mid = (low + high) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            high = mid - 1
        else:  # <
            low = mid + 1
    return -1

def bin_search_recursive(li, val, low, high):
    '''递归实现二分查找'''
    if low <= high:
        mid = (low + high) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            return bin_search_recursive(li, val, low, mid - 1)
        else:
            return bin_search_recursive(li, val, mid + 1, high)
    return -1

if __name__ == '__main__':
    # li = list(range(0, 100000, 2))
    li = list(range(0, 100000))
    print(linear_search(li, 3980))
    print(bin_search(li, 3980))
    print(bin_search_recursive(li, 3980, 0, len(li)-1))

# 可以在ipython中使用timeit来计算下运行时间：
# In [6]: %timeit linear_search(li, 3980)
# 269 µs ± 3.55 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
#
# In [7]: %timeit bin_search(li, 3980)
# 4.32 µs ± 79.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

