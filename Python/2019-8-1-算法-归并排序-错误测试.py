Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = MergeSort(lists[:middle])
    right = MergeSort(lists[middle:])
    return merge(left, right)


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

SyntaxError: invalid syntax
>>> def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = MergeSort(lists[:middle])
    right = MergeSort(lists[middle:])
    return merge(left, right)


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

>>> a = [1,3,5,2,5,6,7]
>>> MergeSort(a)
[1, 2, 3, 5, 5, 6, 7]
>>> def merge(left,right):
	i = j = 0
	m = len(left)
	n = len(right)
	arr = []
	while i <= m and j <= n:
		if left[i] <= right[j]:
			arr.append(left[i])
			i += 1
		else :
			arr.append(right[j])
			j += 1
	if i >= m:
		for a in right[j:]:
			arr.append(a)
	else :
		for b in left[i:]:
			arr.append(b)
	return arr

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#1>", line 5, in MergeSort
    left = MergeSort(lists[:middle])
  File "<pyshell#1>", line 6, in MergeSort
    right = MergeSort(lists[middle:])
  File "<pyshell#1>", line 7, in MergeSort
    return merge(left, right)
  File "<pyshell#6>", line 7, in merge
    if left[i] <= right[j]:
IndexError: list index out of range
>>> def merge(left,right):
	i = j = 0
	m = len(left)
	n = len(right)
	arr = []
	while i <= m and j <= n:
		if left[i] <= right[j]:
			arr.append(left[i])
			i += 1
		else :
			arr.append(right[j])
			j += 1
	if i == m:
		for a in right[j:]:
			arr.append(a)
	else :
		for b in left[i:]:
			arr.append(b)
	return arr

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#1>", line 5, in MergeSort
    left = MergeSort(lists[:middle])
  File "<pyshell#1>", line 6, in MergeSort
    right = MergeSort(lists[middle:])
  File "<pyshell#1>", line 7, in MergeSort
    return merge(left, right)
  File "<pyshell#9>", line 7, in merge
    if left[i] <= right[j]:
IndexError: list index out of range
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

>>> MergeSort(a)
[1, 2, 3, 5, 5, 6, 7]
>>> def merge(left,right):
	i = j = 0
	m = len(left)
	n = len(right)
	c = []
	while i <= m and j <= n:
		if left[i] <= right[j]:
			c.append(left[i])
			i += 1
		else :
			c.append(right[j])
			j += 1
	if i >= m:
		for a in right[j:]:
			c.append(a)
	else :
		for b in left[i:]:
			c.append(b)
	return c

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#1>", line 5, in MergeSort
    left = MergeSort(lists[:middle])
  File "<pyshell#1>", line 6, in MergeSort
    right = MergeSort(lists[middle:])
  File "<pyshell#1>", line 7, in MergeSort
    return merge(left, right)
  File "<pyshell#14>", line 7, in merge
    if left[i] <= right[j]:
IndexError: list index out of range
>>> def merge(left,right):
	i = j = 0
	m = len(left)
	n = len(right)
	c = []
	while i <= len(left) and j <= n:
		if left[i] <= right[j]:
			c.append(left[i])
			i += 1
		else :
			c.append(right[j])
			j += 1
	if i >= len(left):
		for a in right[j:]:
			c.append(a)
	else :
		for b in left[i:]:
			c.append(b)
	return c

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#1>", line 5, in MergeSort
    left = MergeSort(lists[:middle])
  File "<pyshell#1>", line 6, in MergeSort
    right = MergeSort(lists[middle:])
  File "<pyshell#1>", line 7, in MergeSort
    return merge(left, right)
  File "<pyshell#17>", line 7, in merge
    if left[i] <= right[j]:
IndexError: list index out of range
>>> def merge(left,right):
	i = j = 0
	m = len(left)
	n = len(right)
	c = []
	while i <= len(left) and j <= len(right):
		if left[i] <= right[j]:
			c.append(left[i])
			i += 1
		else :
			c.append(right[j])
			j += 1
	if i >= len(left):
		for a in right[j:]:
			c.append(a)
	else :
		for b in left[i:]:
			c.append(b)
	return c

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#1>", line 5, in MergeSort
    left = MergeSort(lists[:middle])
  File "<pyshell#1>", line 6, in MergeSort
    right = MergeSort(lists[middle:])
  File "<pyshell#1>", line 7, in MergeSort
    return merge(left, right)
  File "<pyshell#20>", line 7, in merge
    if left[i] <= right[j]:
IndexError: list index out of range
>>> def merge(left,right):
	i = j = 0
	c = []
	while i <= len(left) and j <= len(right):
		if left[i] <= right[j]:
			c.append(left[i])
			i += 1
		else :
			c.append(right[j])
			j += 1
	if i >= len(left):
		for a in right[j:]:
			c.append(a)
	else :
		for b in left[i:]:
			c.append(b)
	return c

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#1>", line 5, in MergeSort
    left = MergeSort(lists[:middle])
  File "<pyshell#1>", line 6, in MergeSort
    right = MergeSort(lists[middle:])
  File "<pyshell#1>", line 7, in MergeSort
    return merge(left, right)
  File "<pyshell#22>", line 5, in merge
    if left[i] <= right[j]:
IndexError: list index out of range
>>> def merge(left,right):
	i = j = 0
	c = []
	while i < len(left) and j <len(right):
		if left[i] <= right[j]:
			c.append(left[i])
			i += 1
		else :
			c.append(right[j])
			j += 1
	if i >= len(left):
		for a in right[j:]:
			c.append(a)
	else :
		for b in left[i:]:
			c.append(b)
	return c

>>> MergeSort(a)
[1, 2, 3, 5, 5, 6, 7]
>>> 
