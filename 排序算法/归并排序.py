
def merge_sort(l, start, end):
    if start + 1 >= end:
        return
    length = end-start+1
    mid = start + int(length/2)
    # 分

    merge_sort(l, start, mid)
    merge_sort(l, mid, end)
    # 治

    new = []
    k = start
    i = start
    j = mid
    while k < end:
        while i < mid and (j >= end or l[i] <= l[j]):
            new.append(l[i])
            i += 1
            k += 1
        while j < end and (i >= mid or l[i] > l[j]):
            new.append(l[j])
            j += 1
            k += 1
    m = start
    for item in new:
        l[m] = item
        m += 1

l = [8,7,6,6,5,4,3,3,1,2]
merge_sort(l, 0, len(l))
print(l)



