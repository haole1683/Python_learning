try:
    int('abc')
    sum = 1 + '1'
    f = open('沙雕玩意.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错了\n 错误原因是:' + str(reason))
except TypeError as reason:
    print('类型出错了\n 错误原因是:' + str(reason))
except (TypeError,ValueError):##也可以这么写
    print('出错了')
except:
    print('WRONG')
##try语句一旦有异常，后面的语句将不会执行


##finally:

finally:
    f.close()
    ##无论如何都会执行的代码
    ##用于处理文件关闭，内存清理等操作


