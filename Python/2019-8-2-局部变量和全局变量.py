def discounts(price,rate):
	final_price = price * rate
	old_price = 50
	print('修改后old_price的值是',old_price)
	return final_price
old_price = float(input('请输入原价'))
rate = float(input('请输入折扣率'))
new_price = discounts(old_price,rate)
print('修改后old_price的值是' ,old_price)
print('打折后的价格是',new_price)
                  
##注意函数之中的old_price就是局部变量，相当于自己函数内部定义的，与外部的old_price
##关系

##不要在函数内部试图修改全局变量，Python默认会新建一个局部变量
