Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##三向快速排序
>>> def quick_3_way(a,lo,hi):
	if lo >= hi:
		return
	pivot = a[lo]
	lt , i , gt = lo , lo + 1 , hi
	while i <= gt:
		##a[i]小于基准值，则a[i] 和 a[lt] 进行交换 ,i 和 lt 分别 + 1
		if a[i] < pivot:
			a[i] , a[lt] = a[lt] , a[i]
			i += 1
			lt += 1
		##a[i]大于基准值 ,则a[i]和a[gt]进行交换 gt - 1
		elif a[i] > pivot:
			a[i] , a[gt] = a[gt] , a[i]
			gt -= 1
		##a[i] 等于基准值，则 i + 1
		else:
			i += 1
	quick_3_way(a,lo,lt - 1)
	quick_3_way(a,gt + 1,hi)
	return a

>>> arr = [1,6,4,3,2,5]
>>> quick_3_way(arr,0,5)
[1, 2, 3, 4, 5, 6]
>>> ##简言之：将比基准值小的放到数组左端，将比基准值大的放到数组右边，将等于基准值的放到一起

>>> ##适用于大量重复的基准值
>>> def quick_3_way_my(arr,le,ri):
	if le > right:
		return
	pivot = arr[le]
	lt , i , gt =  le , le + 1 , ri
	while i <= gt:
		if arr[i] < pivot:
			arr[i] , arr[lt] = arr[lt] , arr[i]
			i , lt = i + 1 , lt + 1
		elif arr[i] > pivot:
			arr[i] ,arr[gt] = arr[gt] , arr[i]
			gt -= 1
		else:
			i += 1
	quick_3_way_my(arr,le,lt - 1)
	quick_3_way_my(arr,gt + 1,hi)
	return arr

>>> quick_3_way_my(arr)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    quick_3_way_my(arr)
TypeError: quick_3_way_my() missing 2 required positional arguments: 'le' and 'ri'
>>> arr = [1,6,2,5,3,4]
>>> quick_3_way_my(arr,0,5)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    quick_3_way_my(arr,0,5)
  File "<pyshell#46>", line 2, in quick_3_way_my
    if le > right:
NameError: name 'right' is not defined
>>> def quick_3_way_my(arr,le,ri):
	if le > ri:
		return
	pivot = arr[le]
	lt , i , gt =  le , le + 1 , ri
	while i <= gt:
		if arr[i] < pivot:
			arr[i] , arr[lt] = arr[lt] , arr[i]
			i , lt = i + 1 , lt + 1
		elif arr[i] > pivot:
			arr[i] ,arr[gt] = arr[gt] , arr[i]
			gt -= 1
		else:
			i += 1
	quick_3_way_my(arr,le,lt - 1)
	quick_3_way_my(arr,gt + 1,hi)
	return arr

>>> quick_3_way_my(arr,0,5)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    quick_3_way_my(arr,0,5)
  File "<pyshell#51>", line 16, in quick_3_way_my
    quick_3_way_my(arr,gt + 1,hi)
NameError: name 'hi' is not defined
>>> def quick_3_way_my(arr,le,ri):
	if le > ri:
		return
	pivot = arr[le]
	lt , i , gt =  le , le + 1 , ri
	while i <= gt:
		if arr[i] < pivot:
			arr[i] , arr[lt] = arr[lt] , arr[i]
			i , lt = i + 1 , lt + 1
		elif arr[i] > pivot:
			arr[i] ,arr[gt] = arr[gt] , arr[i]
			gt -= 1
		else:
			i += 1
	quick_3_way_my(arr,le,lt - 1)
	quick_3_way_my(arr,gt + 1,ri)
	return arr

>>> quick_3_way_my(arr)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    quick_3_way_my(arr)
TypeError: quick_3_way_my() missing 2 required positional arguments: 'le' and 'ri'
>>> def quick_3_way(a,lo,hi):
	if lo >= hi:
		return
	pivot = a[lo]
	lt , i , gt = lo , lo + 1 , hi
	while i <= gt:
		##a[i]小于基准值，则a[i] 和 a[lt] 进行交换 ,i 和 lt 分别 + 1
		if a[i] < pivot:
			a[i] , a[lt] = a[lt] , a[i]
			i += 1
			lt += 1
		##a[i]大于基准值 ,则a[i]和a[gt]进行交换 gt - 1
		elif a[i] > pivot:
			a[i] , a[gt] = a[gt] , a[i]
			gt -= 1
		##a[i] 等于基准值，则 i + 1
		else:
			i += 1
	quick_3_way(a,lo,lt - 1)
	quick_3_way(a,gt + 1,hi)
	return a

>>> quick_3_way(arr)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    quick_3_way(arr)
TypeError: quick_3_way() missing 2 required positional arguments: 'lo' and 'hi'
>>> 
====================== RESTART: D:/Python/三项快速排序test.py ======================
>>> arr = [1,4,5,2,3]
>>> quick_3_way(arr,0,4)
[1, 2, 3, 4, 5]
>>> 
====================== RESTART: D:/Python/三项快速排序test.py ======================
>>> arr
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    arr
NameError: name 'arr' is not defined
>>> arr = [1,5,4,3,2]
>>> quick_3_way_my(arr,0,len(arr) - 1)
[1, 2, 3, 4, 5]
>>> 
