Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def merge_sort(a):
	if len(a) <= 1:
		return a
	middle = len(a) // 2
	left = merge_sort(a[:middle])
	right = merge_sort(a[middle:])
	return merge(left,right)

>>> def merge(left,right):
	i,j = 0,0
	result = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[i])
			j += 1
	result.extend(left[i:])
	result.extend(right[j:])
	return result

>>> array1 = [1,2,45,2,73,34,0,-32,432,6]
>>> merge_sort(array1)
[-32, -32, 1, 2, 2, 34, 34, 45, 73, 432]
>>> array1
[1, 2, 45, 2, 73, 34, 0, -32, 432, 6]
>>> def merge_sort_new(a):
	if len(a) <= 1:
		return a
	middle = len(a) // 2
	left = merge_sort(a[:middle])
	right = merge_sort(a[middle+1:])
	return merge(left,right)

>>> merge_sort_new(array1)
[-32, -32, 1, 2, 2, 432, 45, 73, 432]
>>> merge_sort(array1)
[-32, -32, 1, 2, 2, 34, 34, 45, 73, 432]
>>> array1
[1, 2, 45, 2, 73, 34, 0, -32, 432, 6]
>>> array2 = [1,9,3,6,4,2,7,5]
>>> merge_sort(array2)
[1, 4, 4, 4, 6, 6, 7, 9]
>>> def merge(a, b):
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

>>> merge_sort(array2)
[1, 2, 3, 4, 5, 6, 7, 9]
>>> merge_sort(array1)
[-32, 0, 1, 2, 2, 6, 34, 45, 73, 432]
>>> array1
[1, 2, 45, 2, 73, 34, 0, -32, 432, 6]
>>> 
