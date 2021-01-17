def quick_sort(l, start, end):
    left = start
    right = end
    if end <= start:
        return
    mid = l[start]
    while start < end:
        while l[end] >= mid and start < end:
            end -= 1
        l[start] = l[end]
        while l[start] < mid and start < end:
            start += 1
        l[end] = l[start]
    l[start] = mid
    quick_sort(l, left, start-1)
    quick_sort(l, start + 1, right)

l = [1,2,3,6,5,4,3,3,3]
quick_sort(l, 0, len(l)-1)
print(l)