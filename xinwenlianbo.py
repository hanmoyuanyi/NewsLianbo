import time
import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
print('新闻联播生成器 1.0.0 by 翰墨远逸')
print('国内新闻部分')
a = input('哪位领导/人干的？')
an = input('ta会见了哪国？')
b = input('ta搞了些什么大新闻？')
e = input('附加题（必答）：反对派干了些啥？')
d = '{}在钓鱼台国宾馆亲切会见了{}国总统，双方进行了{}。{}高度赞赏了{}并对{}一贯坚持“一个中国”的原则表示感谢。{}高度赞扬中{}两国关系，对{}表示欢迎，并强烈谴责了某些国家{}的做法。'.format(a,an,b,a,an,an,a,an,b,e)
print('国际新闻部分')
f = input('哪国？')
g = input('不满什么政策？')
h = input('天数？')
i = input('伤亡人数？')
k = input('地震级数？')
j = '{}群众不满{}，举行示威活动。骚乱已持续{}天。同国发生{}级地震，目前已造成{}人伤亡。'.format(f,g,h,k,i)
print('今天是',year,'年',month,'月',day,'日。下面请听详细内容。',d,j,'今天的新闻联播播送完了，感谢你的收看，更多新闻资讯，请关注央视新闻,，再见。')
print('======================来自 @翰墨远逸 https://qiu-lnt.blogspot.com Inspired by Gengshuang Emulator===============================')
