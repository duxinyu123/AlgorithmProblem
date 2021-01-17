def select_sort(l):
    n = len(l)
    # 第一层循环控制迭代轮数

    for i in range(0, n-1):
        mix_index = i
        # 第二层循环控制比较次数

        for j in range(i+1, n):
            if l[mix_index] > l[j]:
                mix_index = j
        if mix_index != i:
            l[mix_index], l[i] = l[i], l[mix_index]
    print(l)

select_sort([1,2,3,6,5,4])