Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def MyQuickSort(data):
	if(len(data) != 1)
	
SyntaxError: invalid syntax
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

	
