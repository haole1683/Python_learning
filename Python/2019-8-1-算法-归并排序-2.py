def merge_sort(a):
	if len(a) <= 1:
		return a
	middle = len(a) // 2
	left = merge_sort(a[:middle])
	right = merge_sort(a[middle:])
	return merge(left,right)
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c
array1 = [1,2,45,2,73,34,0,-32,432,6]
merge_sort(array1)
