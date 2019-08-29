Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##三向切分快速排序
>>> 、
>>> \
  
>>> ##快速三向切分
>>> def quick_3_way_sort(arr,lo,hi):
	base = arr[lo]
	p , q , i , j = lo + 1 , hi , lo + 1 ，hi
	
SyntaxError: invalid character in identifier
>>> def quick_3_way_sort(arr,lo,hi):
	base = arr[lo]
	p , q , i , j = lo + 1 , hi , lo + 1 ，hi
	
SyntaxError: invalid character in identifier
>>> def quick_3_way_sort(arr,lo,hi):
	base = arr[lo]
	p , q , i , j = lo + 1 , hi , lo + 1 ，hi
	
SyntaxError: invalid character in identifier
>>> def quick_3_way_sort(arr,lo,hi):
	if 
	base = arr[lo]
	p , q , i , j = lo + 1 , hi , lo + 1 , hi
	while i <= j:
		if arr[i] == base:
			arr[p] , arr[i] = arr[i] ,arr[p]
			i += 1
			p += 1
		elif arr[i] < base:
			i += 1
		else:
			arr[i] , arr[j] = arr[j] , arr[i]
			j -= 1
		if arr[j] == base:
			arr[q] ,arr[j] = arr[j] , arr[q]
			j -= 1
			q -= 1
		elif arr[j] > base:
			j -= 1
		else:
			arr[i] , arr[j] = arr[j] , arr[i]
			i += 1
	arr[lo:p] , arr[p:i] = arr[p:i] , arr[lo:p]
	arr[q:hi] , arr[j:q] = arr[j:q] , arr[q:hi]
	return 
