import random
import time
import copy
import sys


def cal_time(func):
    '''计算函数运行时间的装饰器'''
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2-t1))
        return result
    return wrapper

@cal_time
def bubble_sort(li):
    """
    冒泡排序
    time complexity: O(n^2)
    以下改进版冒泡最好的情况是传进来的列表是有序的，那么只走一趟，比较和移动元素的次数分别是n-1和0，所以最好情况的时间复杂度是O(n)
    平均情况下和最差情况都是O(n^2)
    稳定性：因为每次比较后如果两个相邻元素相等我们并不会将他们交换，所以冒泡不会改变相同元素的下标，所以冒泡排序是一个稳定的排序。
    待排序的记录序列中可能存在两个或两个以上关键字相等的记录。排序前的序列中Ri领先于Rj（即i<j）.若在排序后的序列中Ri仍然领先于Rj，则称所用的方法是稳定的。
    """
    for i in range(len(li)-1):  #趟数
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            break
    return li

def select_sort(li):
    """
    选择排序
    time complexity: O(n^2)
    举个例子，序列5 8 5 2 9， 我们知道第一遍选择第1个元素5会和2交换，那么原序列中2个5的相对前后顺序就被破坏了，所以选择排序不是一个稳定的排序算法
    """
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):  # 无序区，i+1开始，最后的位置是len(li)-1
            if li[j] < li[min_loc]:
                min_loc = j
        li[min_loc], li[i] = li[i], li[min_loc]  # 交换

def insert_sort(li):
    """
    插入排序
    time complexity: O(n^2)
    平均情况O(n^2)，最好情况O(n)，最坏情况O(n^2)
    插入排序是在一个已经有序的小序列的基础上，一次插入一个元素。当然，刚开始这个有序的小序列只有1个元素，就是第一个元素。
    比较是从有序序列的末尾开始，也就是想要插入的元素和已经有序的最大者开始比起，如果比它大则直接插入在其后面，否则一直往前找直到找到它该插入的位置。
    如果碰见一个和插入元素相等的，那么插入元素把想插入的元素放在相等元素的后面。所以，相等元素的前后顺序没有改变，从原无序序列出去的顺序就是排好序后的顺序，所以插入排序是稳定的。

    优化：应用二分查找来寻找插入点（没什么卵用），下面的是顺序查找的
    """
    for i in range(1, len(li)): # 这里的i作为刚抽到的牌,比如len(li)=10,这里循环就是1-9。第一个元素不需要参见排序，最后一个要参加排序，前面两种是最后一个不要排序。
        tmp = li[i]  # 把摸到的牌临时存起来
        j = i - 1       # 手里所有牌中的最后一张牌的位置
        while j >= 0 and li[j] > tmp: # 手里的牌向后挪动，找到新抓的牌应该插入的位置
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = tmp # 空的位置不是j，是j+1

#li = list(range(100))
#random.shuffle(li) #打乱列表
#bubble_sort(li)
#select_sort(li)
#insert_sort(li)
#print(li)



def partition(li, left, right):
    """
    归位第一个元素
    这个函数复杂度，其实就是两个指针从两侧往中间靠，时间复杂度O(n)
    """
    tmp = li[left] # 把第一个元素存起来，这个位置就空了。而left和right作为指针往列表中间移动，直到left和right碰上
    while left < right:
        while left < right and li[right] >= tmp: # 先动右边，找比tmp小的数，移到左边那个空位。加=的时候保证等于的时候也不挪，省时间
            right -= 1
        li[left] = li[right] #这样右边有一个位置空了，再去动左边
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp # 直到left和right碰上
    return left

def _quick_sort(li, left, right): #注意不能给递归函数加装饰器，所以选择套一个马甲
    """
    递归
    """
    if left < right:
        mid = partition(li, left, right) # 归位函数，时间复杂度O(n)
        _quick_sort(li, left, mid-1) # 递归，每次切成一半，时间复杂度O(logn)
        _quick_sort(li, mid+1, right)

@cal_time
def quick_sort(li):
    """
    快速排序
    时间复杂度：O(nlogn)
    最坏情况：比如 [9,8,7,6,5,4,3,2,1]，每次partition的时候都没有分成两部分，这种最坏处情况复杂度是O(n^2)。
    """
    _quick_sort(li, 0, len(li)-1)

# li = [5, 7, 4, 6, 3, 1, 2, 9, 3]
# quick_sort(li)
# print(li)


# 冒泡和快排对比
li = list(range(10000))
random.shuffle(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
bubble_sort(li1)
quick_sort(li2)

#快排最差情况
sys.setrecursionlimit(1000000) #设置递归深度
lix = list(range(1000, 1, -1))
quick_sort(lix)



