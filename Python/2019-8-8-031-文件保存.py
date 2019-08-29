Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pickle
>>> my_list = [123,'dfaf',3.44,['das']]
>>> my_list
[123, 'dfaf', 3.44, ['das']]
>>> pickle_file = open('my_list.pkl','wb')
>>> pickle.dump(my_list,pickle_file)
>>> pickle_file.close()
>>> pickle_file = open('my_list.pkl','rb')
>>> my_list2 = pickle.load(pickle_file)
>>> print(my_list2)
[123, 'dfaf', 3.44, ['das']]
>>> list1 = ['我自己太没']
>>> pickle_file.close()\

		     
>>> pickle_2 = open('a.txt','wb')
>>> pickle.dump(list1,pickle_2)
>>> pickle_2.close()
>>> 
