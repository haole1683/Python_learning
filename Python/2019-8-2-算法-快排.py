##快速排序
##1.从数列中挑一个元素，称为“基准”(pivot)
##2.重新排序数列，所有比基准值小的元素摆在基准前面，所有比基准值的大元素摆在基准后面（相同的数可以到任何一边）。在这个分割结束后，该基准就处于数列中间位置，这个称为分割操作
##3.递归地把小于基准值元素的子数列和大于基准值元素的子数列排序

def quick_sort(data):
	if len(data) >= 2:##递归入口及出口
		mid = data[len(data) - 1]##选取基准值
		left,right = [] , []##定义基准值左右两侧的列表
		data.remove(mid)
		for num in data:
			if num >= mid:
				right.append(num)##大于等于基准值放右边
			else:
				left.append(num)##小于等于基准值放左边
		return quick_sort(left) + [mid] + quick_sort(right)
	else:
		return data
