Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##pickle 模块
>>> import pickle
>>> my_list = [123,3.14,'sha',['dfd',1]]
>>> pickle_file = open('my_list.pkl','wb')
>>> pickle.dump(my_list,pickle_file)
>>> pickle_file.close()
>>> pickle_file = open('my_list.pkl','wb')
>>> my_list2 = pickle.load()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my_list2 = pickle.load()
TypeError: load() missing required argument 'file' (pos 1)
>>> my_list2 = pickle.load(pickle_file)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    my_list2 = pickle.load(pickle_file)
io.UnsupportedOperation: read
>>> pickle_file = open('my_list.pkl','wr')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    pickle_file = open('my_list.pkl','wr')
ValueError: must have exactly one of create/read/write/append mode
>>> pickle_file = open('my_list.pkl','rb')
>>> my_list2 = pickle.load(pickle_file)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    my_list2 = pickle.load(pickle_file)
EOFError: Ran out of input
>>> my_list2 = pickle.load(pickle_file)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    my_list2 = pickle.load(pickle_file)
EOFError: Ran out of input
>>> pickle_file.close()
>>> pickle_file = open('my_list.pkl','rb')
>>> my_list2 = pickle.load(pickle_file)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    my_list2 = pickle.load(pickle_file)
EOFError: Ran out of input
>>> 
