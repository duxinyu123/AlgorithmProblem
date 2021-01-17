def insert_sort(l):
    n = len(l)
    # 第一层循环控制轮数

    for i in range(1, n):
        # 第二层循环控制每一轮比较次数

        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break
    print(l)

insert_sort([6,5,4,3,2,1])