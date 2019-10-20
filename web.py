import jieba  # 分词包
import numpy  # numpy计算包
import codecs  # codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
import re
import pandas as pd
import matplotlib.pyplot as plt
from urllib import request
from bs4 import BeautifulSoup as bs
import matplotlib
import xlwt
import operator
from functools import reduce
from wordcloud import WordCloud

file = open("hw.txt", "w", encoding='utf-8')

def getComments(pageNum):
    eachCommentList = []
    eachDateList = []
    if pageNum > 0:
        start = (pageNum-1) * 20
    else:
        return False
    requrl = 'https://movie.douban.com/subject/20645019/' + \
        '?' + 'start=' + str(start) + '&limit=20' + '&sort=new_score&status=P'

    print(requrl)

    resp = request.urlopen(requrl)
    html_data = resp.read().decode('utf-8')  # 有中文，所以要转码
    soup = bs(html_data, 'html.parser')  # 用美丽汤先进先进行分析
    # 找到所有<div, class = 'comment'>的部分
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p'):
            # 准确的找到comment所在的那个<span>
            eachCommentList.append(item.find_all('span', class_='short')[0].string)
            tmpDate = item.find_all('span')[-2].string
            eachDateList.append(tmpDate)
    return eachCommentList, eachDateList  # 组合评论
def main():
    commentList = []
    dateList = []
    for i in range(50):
        num = i + 1
        [commentList_temp, dateList_temp] = getComments(num)
        commentList.append(commentList_temp)
        dateList.append(dateList_temp)
    commentList = reduce(operator.add, commentList)
    dateList = reduce(operator.add, dateList)

    dataTmp = {'comments': commentList[:], 'date': dateList[:]}
    df2 = pd.DataFrame(dataTmp)
    pd.DataFrame(df2).to_excel("text-movie.xls",
                               sheet_name="sheet1", index=False, header=True)

    comments = ''
    final = ''
    for k in range(len(commentList)):
        comments = comments + (str(commentList[k])).strip()
        final+=comments
    file.write(final)
    file.close()
    
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)  # 过滤标点 用正则表达式
    cleaned_comments = ''.join(filterdata)

    segment = jieba.lcut(cleaned_comments)
    # 请实践 -- 调整分词
    #https://github.com/fxsjy/jieba  结巴分词的网站
    #使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
    #使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
    #jieba.add_word('孟晚舟')
    #jieba.del_word('今天天气')
    #jieba.suggest_freq(('今天', '天气'), True)

    words_df = pd.DataFrame({'segment': segment})  # 割词

    stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                            encoding='utf-8')
    # -- 请实践： 停止词， 在 stopwords.txt 文件中，可以添加和修改停止词。
    # 例如将 “电影” 这个词加入到 stopwords文件中，

    
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

    words_stat = words_df.groupby(by=['segment'])[
        'segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(
        by=["计数"], ascending=False)
    print(words_stat.head())  # 数词

    wordcloud = WordCloud(font_path="simhei.ttf",
                          background_color="white", max_font_size=80)
    word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}  # 画图

    word_frequence_list = []
    for key in word_frequence:
        temp = (key, word_frequence[key])
        word_frequence_list.append(temp)

main()

import jieba
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

back_color = imread('bg.jpg')  # 解析该图片

wc = WordCloud(background_color='white',  # 背景颜色
               max_words=16000,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=30,  # 显示字体的最大值
               stopwords=STOPWORDS.add('tm'),  # 使用内置的屏蔽词，再添加'苟利国'
               font_path="simhei.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               )
# WordCloud各含义参数请点击 wordcloud参数

# 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
# 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
jieba.add_word('霸王')
jieba.add_word('虞姬')
jieba.add_word('蝶衣')
# 打开词源的文本文件
text = open('bawangbieji.txt', encoding = 'utf-8').read()


# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('stopwords.txt', encoding = 'utf-8') as f:
        str_text = f.read()
        str_text.encode(encoding = 'utf-8')
        unicode_text = str_text  # 把str格式转成unicode格式
        f.close()  # stopwords文本中词的格式是'一词一行'
    for word in word_generator:
        if word.strip() not in unicode_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格


text = stop_words(text)

wc.generate(text)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
# 保存图片
wc.to_file('build.png')
