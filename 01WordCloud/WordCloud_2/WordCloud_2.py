
# coding: utf-8

# ## WordCloud_2
# 
# 以《西游记》为，制作中文词汇中文词云，但结果中会出现各种双字、三字和四字等,很多并不是合理的词语。

# <a id='导入词云包'></a>

# ## 导入词云包

# In[1]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud


# ## 生成对象

# In[5]:


text = open('../xyj.txt').read()
wc = WordCloud(font_path='../Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)


# ## 显示词云

# In[6]:


plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# ## 保存图片

# In[7]:


wc.to_file('wordcloud_2.png')

