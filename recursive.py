
# 递归问题
# 递归的两个特点：
# 1.调用自身
# 2.结束条件

# 例子：
# 打印"抱着抱着抱着我的小鲤鱼的我的我的我"

def func(x):
    if x == 0:
        print("我的小鲤鱼", end='')
    else:
        print("抱着", end='')
        func(x-1)
        print("的我", end="")
        
func(5)
