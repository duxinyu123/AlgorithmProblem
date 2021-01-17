def shell_sort(l):
    n = len(l)
    # 定义gap为排序间隔

    gap = int(n/2)
    # 最外层循环到gap=1为止

    while gap > 0:
        # 这层为循环的轮数

        for i in range(0, gap):
            # 插入排序
            # j j+gap j+2*gap ....

            for j in range(i+gap, n, gap):
                for k in range(j, 0, -gap):
                    if l[k] < l[k-gap]:
                        l[k], l[k-gap] = l[k-gap], l[k]
                    else:
                        break

        gap = int(gap/2)

l = [7,8,9,1,2,3,4,5,6]
shell_sort(l)
print(l)