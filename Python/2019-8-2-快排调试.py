Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def MyQuickSort(data):
	if len(data) != 1:
		left = []
		right = []
		mid = data[len(data) - 1]
		data.remove(mid)
		for each in data:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
	else:
		return data

	
>>> arr = [1,5,3,2]
>>> arr
[1, 5, 3, 2]
>>> MyQuickSort(arr)
>>> 
>>>  def MyQuickSort(data):
	if len(data) != 1:
		left = []
		right = []
		mid = data[len(data) - 1]
		data.remove(mid)
		for each in data:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return left + [mid] + right
	else:
		return data
	
SyntaxError: unexpected indent
>>> def MyQuickSort(data):
	if len(data) != 1:
		left = []
		right = []
		mid = data[len(data) - 1]
		data.remove(mid)
		for each in data:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return left + [mid] + right
	else:
		return data

	
>>> MyQuickSort(arr)
[1, 3, 5]
>>> def MyQuickSort(data):
	if len(data) != 1:
		left = []
		right = []
		mid = data[len(data) - 1]
		data.remove(mid)
		for each in data:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return MyQuickSort(left) + [mid] + MyQuickSort(right)
	else:
		return data

	
>>> MyQuickSort(arr)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    MyQuickSort(arr)
  File "<pyshell#10>", line 12, in MyQuickSort
    return MyQuickSort(left) + [mid] + MyQuickSort(right)
  File "<pyshell#10>", line 5, in MyQuickSort
    mid = data[len(data) - 1]
IndexError: list index out of range
>>> RR
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    RR
NameError: name 'RR' is not defined
>>> arr
[1]
>>> arr = [1,3,2,4]
>>> MyQuickSort(arr)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    MyQuickSort(arr)
  File "<pyshell#10>", line 12, in MyQuickSort
    return MyQuickSort(left) + [mid] + MyQuickSort(right)
  File "<pyshell#10>", line 5, in MyQuickSort
    mid = data[len(data) - 1]
IndexError: list index out of range
>>> arr
[1, 3, 2]
>>> arr1 = [1,5,7,3,2]
>>> MyQuickSort(arr)
[1, 2, 3]
>>> def MyQuickSort(data):
	if len(data) >= 1:
		left = []
		right = []
		mid = data[len(data) - 1]
		data.remove(mid)
		for each in data:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return MyQuickSort(left) + [mid] + MyQuickSort(right)
	else:
		return data

	
>>> MyQuickSort(arr)
[1, 3]
>>> arr
[1]
>>> arr1
[1, 5, 7, 3, 2]
>>> MyQuickSort(arr1)
[1, 2, 3, 5, 7]
>>> arr2 = [1,6,4,2,3,5]
>>> MyQuickSort(arr2)
[1, 2, 3, 4, 5, 6]
>>> def MyQuickSort(data):
	if len(data) != 1:
		left = []
		right = []
		mid = data[len(data) - 1]
		data.remove(mid)
		for each in data:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return MyQuickSort(left) + [mid] + MyQuickSort(right)
	else:
		return data

	
>>> arr2
[1, 6, 4, 2, 3]
>>> MyQuickSort(arr2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    MyQuickSort(arr2)
  File "<pyshell#28>", line 12, in MyQuickSort
    return MyQuickSort(left) + [mid] + MyQuickSort(right)
  File "<pyshell#28>", line 12, in MyQuickSort
    return MyQuickSort(left) + [mid] + MyQuickSort(right)
  File "<pyshell#28>", line 5, in MyQuickSort
    mid = data[len(data) - 1]
IndexError: list index out of range
>>> def MyQuickSort(data):
	if len(data) >= 2:
		left = []
		right = []
		mid = data[len(data) - 1]
		data.remove(mid)
		for each in data:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return MyQuickSort(left) + [mid] + MyQuickSort(right)
	else:
		return data

	
>>> MyQuickSort(arr2)
[1, 2, 4, 6]
>>> arr2
[1, 6, 4]
>>> arr2
[1, 6, 4]
>>> MyQuickSort(arr2)
[1, 4, 6]
>>> 

>>> def MyQSort(arr):
	if len(arr) >= 2:
		left , right = [] , []
		mid = len(arr) - 1
		arr.remove(mid)
		for each in arr:
			if each >= mid:
				right.append(each)
			else
			
SyntaxError: invalid syntax
>>> def MyQSort(arr):
	if len(arr) >= 2:
		left , right = [] , []
		mid = len(arr) - 1
		arr.remove(mid)
		for each in arr:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return MyQSort(left) + [mid] + MyQSort(right)
	else
	
SyntaxError: invalid syntax
>>> def MyQSort(arr):
	if len(arr) >= 2:
		left , right = [] , []
		mid = len(arr) - 1
		arr.remove(mid)
		for each in arr:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return MyQSort(left) + [mid] + MyQSort(right)
	else:
		return arr

	
>>> arrrr = [1,5,4,3]
>>> arrrr
[1, 5, 4, 3]
>>> MyQSort(arrrr)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    MyQSort(arrrr)
  File "<pyshell#53>", line 11, in MyQSort
    return MyQSort(left) + [mid] + MyQSort(right)
  File "<pyshell#53>", line 5, in MyQSort
    arr.remove(mid)
ValueError: list.remove(x): x not in list
>>> def MyQSort(arr):
	if len(arr) >= 2:
		left , right = [] , []
		mid = arr[len(arr) - 1]
		arr.remove(mid)
		for each in arr:
			if each >= mid:
				right.append(each)
			else:
				left.append(each)
		return MyQSort(left) + [mid] + MyQSort(right)
	else:
		return arr

	
>>> MyQSort(arrrr)
[1, 4, 5]
>>> arrrr
[1, 5]
>>> arrrr
[1, 5]
>>> qwer = [1,5,2,1,4]
>>> MyQSort(qwer)
[1, 1, 2, 4, 5]
>>> 
