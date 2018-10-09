
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud


# In[6]:


# 打开文本
text = open('xyj.txt').read()
# 生成对象
wc = WordCloud(font_path='Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)


# In[7]:


# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[8]:


# 保存到文件
wc.to_file('wordcloud_2.png')

