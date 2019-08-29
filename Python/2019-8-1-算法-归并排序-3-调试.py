Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def MergeSort(MyList):
	mlen = len(MyList)
	middle = mlen // 2
	left = MyList[:middle]
	right = MyList[middle:]
	left = MergeSort(left)
	right = MergeSort(right)
	return merge(left,right)

>>> def merge(left,right):
	i = j = 0
	arr = []
	while i < len(left) and j < len(right)
	
SyntaxError: invalid syntax
>>> def merge(left,right):
	i = j = 0
	arr = []
	while i < len(left) and j < len(right)；
	
SyntaxError: invalid character in identifier
>>> def merge(left,right):
	i = j = 0
	arr = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]
		
SyntaxError: invalid syntax
>>> def merge(left,right):
	i = j = 0
	arr = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr.append(left[i])
			i += 1
		else :
			arr.append(right[j])
			j += 1
	if i >= len(right):
		arr.extend(right[j:])
	else :
		arr.extend(left[i:])
	return arr

>>> a = [1,4,23,56,7]
>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#8>", line 6, in MergeSort
    left = MergeSort(left)
  File "<pyshell#8>", line 6, in MergeSort
    left = MergeSort(left)
  File "<pyshell#8>", line 6, in MergeSort
    left = MergeSort(left)
  [Previous line repeated 990 more times]
  File "<pyshell#8>", line 2, in MergeSort
    mlen = len(MyList)
RecursionError: maximum recursion depth exceeded while calling a Python object
>>> def MergeSort(MyList):
	mlen = len(MyList)
	middle = mlen // 2
	if mlen == 1:
		return MyList[0]
	left = MyList[:middle]
	right = MyList[middle:]
	left = MergeSort(left)
	right = MergeSort(right)
	return merge(left,right)

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#31>", line 8, in MergeSort
    left = MergeSort(left)
  File "<pyshell#31>", line 10, in MergeSort
    return merge(left,right)
  File "<pyshell#27>", line 4, in merge
    while i < len(left) and j < len(right):
TypeError: object of type 'int' has no len()
>>> def MergeSort(MyList):
	mlen = len(MyList)
	middle = mlen // 2
	if mlen == 1:
		return MyList[0]
	left = MergeSort(List[:middle])
	right = MergeSort(MyList[middle:])
	return merge(left,right)

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#34>", line 6, in MergeSort
    left = MergeSort(List[:middle])
NameError: name 'List' is not defined
>>> def MergeSort(MyList):
	mlen = len(MyList)
	middle = mlen // 2
	if mlen == 1:
		return MyList[0]
	left = MergeSort(MyList[:middle])
	right = MergeSort(MyList[middle:])
	return merge(left,right)

>>> MergeSort(a)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    MergeSort(a)
  File "<pyshell#37>", line 6, in MergeSort
    left = MergeSort(MyList[:middle])
  File "<pyshell#37>", line 8, in MergeSort
    return merge(left,right)
  File "<pyshell#27>", line 4, in merge
    while i < len(left) and j < len(right):
TypeError: object of type 'int' has no len()
>>> def MergeSort(MyList):
	mlen = len(MyList)
	middle = mlen // 2
	if mlen == 1:
		return MyList
	left = MergeSort(MyList[:middle])
	right = MergeSort(MyList[middle:])
	return merge(left,right)

>>> MergeSort(a)
[1, 4, 7, 23]
>>> a
[1, 4, 23, 56, 7]
>>> def MergeSort(MyList):
	mlen = len(MyList)
	middle = mlen // 2
	if mlen <= 1:
		return MyList
	left = MergeSort(MyList[:middle])
	right = MergeSort(MyList[middle:])
	return merge(left,right)

>>> a
[1, 4, 23, 56, 7]
>>> MergeSort(a)
[1, 4, 7, 23]
>>> merge
<function merge at 0x000001CBC4FFFD38>
>>> def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = MergeSort(lists[:middle])
    right = MergeSort(lists[middle:])
    return merge(left, right)

>>> MergeSort(a)
[1, 4, 7, 23]
>>> def merge(left,right):
	i = j = 0
	arr = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr.append(left[i])
			i += 1
		else :
			arr.append(right[j])
			j += 1
	if i >= len(right):
		arr.extend(right[j:])
	else :
		arr.extend(left[i:])
	return arr

>>> a = [1,4,23,56,
	 
SyntaxError: invalid syntax
>>> def merge(left,right):
	i = j = 0
	arr = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr.append(left[i])
			i += 1
		else :
			arr.append(right[j])
			j += 1
	if i >= len(right):
		arr.extend(right[j:])
	else :
		arr.extend(left[i:])
	return arr

>>> a = [1,4,23,56,7]
>>> MergeSort(a)
SyntaxError: invalid syntax
>>> def merge(left,right):
	i = j = 0
	arr = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr.append(left[i])
			i += 1
		else :
			arr.append(right[j])
			j += 1
	if i >= len(right):
		arr.extend(right[j-1:])
	else :
		arr.extend(left[i-1:])
	return arr

>>> MergeSort(a)
[1, 4, 4]
>>> a
[1, 4, 23, 56, 7]

>>> def merge(left,right):
	i = j = 0
	arr = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr.append(left[i])
			i += 1
		else :
			arr.append(right[j])
			j += 1
	if i >= len(left):
		arr.extend(right[j:])
	else :
		arr.extend(left[i:])
	return arr

>>> MergeSort(a)
[1, 4, 7, 23, 56]
>>> 
