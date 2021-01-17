def bubble_sort(l):
    n = len(l)
    # 外层循环控制轮数

    for i in range(n-1):
        count = 0
        # 内层循环控制每轮比较的次数

        for j in range(n-1-i):
            if l[j] > l[j+1]:
                count += 1
                l[j], l[j+1] = l[j+1], l[j]
    print(l)

bubble_sort([6,5,4,3,2,1])
