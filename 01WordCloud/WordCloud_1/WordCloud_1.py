
# coding: utf-8

# ## WordCloud_1
# 以英文为例，显示词云制作过程

# ## 导入词云包

# In[2]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt


# ## 生成对象

# In[11]:


text = open('../constitution.txt').read()
wc = WordCloud().generate(text)


# ## 显示词云

# In[12]:


plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# ## 保存图片

# In[13]:


wc.to_file('wordcloud.png')

