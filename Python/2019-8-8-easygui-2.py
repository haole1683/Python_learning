import easygui as g
import sys
while True:
        g.msgbox('Hi,welcome to the first gui game')##msgbox其实还可以设置第二个参数，第二个参数代表标题栏
        #代表标题栏上面的文字，相当于设置标题


        msg = '请问你希望在鱼C工作室学到什么指示'
        title = '小游戏互动'
        choices = ['谈恋爱','编程','OOXX','琴棋书画']


        choices = g.choicebox(msg,title,choices)
        ##这个choice可以接受三个参数
        # choicebox(msg="Pick something."，问题
        # title=" "，
        #choices=()，
        #):

        g.msgbox('你的选择是' + str(choices) , '结果')

        msg = '你希望重新开始小游戏吗'
        title = '请选择'

        if g.ccbox(msg,title):
                pass
        else:
                sys.exit(0)
                
