Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##原地快速排序
>>> 
>>> def inplace_quick_sort(S,a,b):
	if a <= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left >=right:
			break
		##交换左右元素
		S[left] , S[right] = S[right] , S{left]
		
SyntaxError: invalid syntax
>>> def inplace_quick_sort(S,a,b):
	if a <= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left >=right:
			break
		##交换左右元素
		S[left] , S[right] = S[right] , S[left]
	S[left] , S[b] = S[b] , S[left]
	inplace_quick_sort(S,a,left - 1)
	inplace_quici_sort(S,left+1,b)

	
>>> arr = [1,6,3,2,5,4]
>>> arr
[1, 6, 3, 2, 5, 4]
>>> inplace_quick_sort(arr,1,len(arr))
>>> 
>>> arr
[1, 6, 3, 2, 5, 4]
>>> def inplace_quick_sort(S,a,b):
	if a <= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left >=right:
			break
		##交换左右元素
		S[left] , S[right] = S[right] , S[left]
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)

>>> inplace_quick_sort(arr,1,len(arr))
>>> arr
[1, 6, 3, 2, 5, 4]
>>> def inplace_quick_sort(S,a,b):
	if a <= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left >=right:
			break
		##交换左右元素
		S[left] , S[right] = S[right] , S[left]
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S

>>> inplace_quick_sort(arr,0,5)
>>> 
>>> def inplace_quick_sort(S,a,b):
	if a <= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left >=right:
			break
		##交换左右元素
		S[left] , S[right] = S[right] , S[left]
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S
\

  
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left >=right:
			break
		##交换左右元素
		S[left] , S[right] = S[right] , S[left]
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S

>>> inplace_quick_sort(arr,0,5)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
def inplace_quick_sort(S, a, b):
    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left+1, right-1

    S[left], S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left+1, b)
    return S

>>> inplace_quick_sort(arr,0,5)
[1, 2, 3, 4, 5, 6]
>>> arr
[1, 2, 3, 4, 5, 6]
>>> 
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left >=right:
			break
		##交换左右元素
		S[left] , S[right] = S[right] , S[left]
		left , right = left + 1,right +1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S

>>> arr1 = [1,4,3,5,2,6]
>>> arr1
[1, 4, 3, 5, 2, 6]
>>> inplace_quick_sort(arr,0,5)
>>> 
>>> 
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		 if left <= right:
			S[left], S[right] = S[right], S[left]
			left, right = left+1, right-1

	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S
SyntaxError: unindent does not match any outer indentation level
>>>  def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		 if left <= right:
			 
			 S[left], S[right] = S[right], S[left]
			 left, right = left+1, right-1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S
SyntaxError: unexpected indent
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		 if left <= right:
			 
			 S[left], S[right] = S[right], S[left]
			 left, right = left+1, right-1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S
SyntaxError: unindent does not match any outer indentation level
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		 if left <= right:
			 S[left], S[right] = S[right], S[left]
			 left, right = left+1, right-1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		 if left <= right:
			 S[left] ,S[right] = S[right] ,S[left]
			 left , right = left+1,right+1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S
SyntaxError: unindent does not match any outer indentation level
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left <= right:
			S[left] ,S[right] = S[right] ,S[left]
			left , right = left+1,right+1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S

>>> inplace_quick_sort(arr1)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    inplace_quick_sort(arr1)
TypeError: inplace_quick_sort() missing 2 required positional arguments: 'a' and 'b'
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left <= right:
			S[left] ,S[right] = S[right] ,S[left]
			left , right = left+1,right-1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S

>>> inplace_quick_sort(arr1)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    inplace_quick_sort(arr1)
TypeError: inplace_quick_sort() missing 2 required positional arguments: 'a' and 'b'
>>> arr1
[1, 4, 3, 5, 2, 6]
>>> inplace_quick_sort(arr1,0,5)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left <= right:
			S[left] ,S[right] = S[right] ,S[left]
			left , right = left+1,right-1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S

>>> def inplace_quick_sort(S, a, b):
    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left+1, right-1

    S[left], S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left+1, b)
    return S

>>> inplace_quick_sort(arr1,0,5)
[1, 2, 3, 4, 5, 6]
>>> def inplace_quick_sort(S,a,b):
	if a >= b:
		return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left <= right:
			S[left] ,S[right] = S[right] ,S[left]
			left , right = left+1,right-1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S

>>> 
>>> inplace_quick_sort(arr1,0,5)
>>> 
>>> def inplace_quick_sort(S,a,b):
	if a >= b:return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left <= right:
			S[left] ,S[right] = S[right] ,S[left]
			left , right = left+1,right-1
	S[left] , S[b] = S[b] , S[left]
	return inplace_quick_sort(S,a,left - 1)
	return inplace_quici_sort(S,left+1,b)
	return S

>>> inplace_quick_sort(arr,0,5)
>>> 
>>> def inplace_quick_sort(S,a,b):
	if a >= b:return
	pivot = S[b]
	left = a
	right = b - 1
	while left <=right:
		##左指针向右移动，寻找第一个比基准值大的元素
		while left <=right and S[left] < pivot:
			left += 1
		##右指针向左移动，寻找第一个比基准值小的元素
		while left <= right and pivot < S[right]:
			right -= 1
		if left <= right:
			S[left] ,S[right] = S[right] ,S[left]
			left , right = left+1,right-1
	S[left] , S[b] = S[b] , S[left]
	inplace_quick_sort(S,a,left - 1)
	inplace_quici_sort(S,left+1,b)
	return S

>>> inplace_quick_sort(arr,0,5)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    inplace_quick_sort(arr,0,5)
  File "<pyshell#97>", line 17, in inplace_quick_sort
    inplace_quick_sort(S,a,left - 1)
  File "<pyshell#97>", line 17, in inplace_quick_sort
    inplace_quick_sort(S,a,left - 1)
  File "<pyshell#97>", line 17, in inplace_quick_sort
    inplace_quick_sort(S,a,left - 1)
  [Previous line repeated 1 more time]
  File "<pyshell#97>", line 18, in inplace_quick_sort
    inplace_quici_sort(S,left+1,b)
NameError: name 'inplace_quici_sort' is not defined
>>> arr1 = [1,5,3,4,2]
>>> inplace_quick_sort(arr1,0,4)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    inplace_quick_sort(arr1,0,4)
  File "<pyshell#97>", line 18, in inplace_quick_sort
    inplace_quici_sort(S,left+1,b)
NameError: name 'inplace_quici_sort' is not defined
>>> arr1
[1, 2, 3, 4, 5]
>>> arr2 = [1,7,6,2,3,4,5]
>>> inplace_quick_sort(arr2,0,6)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    inplace_quick_sort(arr2,0,6)
  File "<pyshell#97>", line 17, in inplace_quick_sort
    inplace_quick_sort(S,a,left - 1)
  File "<pyshell#97>", line 18, in inplace_quick_sort
    inplace_quici_sort(S,left+1,b)
NameError: name 'inplace_quici_sort' is not defined
>>> arr2
[1, 2, 3, 4, 5, 7, 6]
>>> def inplace_quick_sort(S, a, b):
    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left+1, right-1

    S[left], S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left+1, b)
    return S

>>> inplace_quick_sort(arr2,0,6)
[1, 2, 3, 4, 5, 6, 7]
>>> 
