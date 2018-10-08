
# coding: utf-8

# In[2]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[3]:


# 打开文本
text = open('constitution.txt').read()
# 生成对象
wc = WordCloud().generate(text)


# In[4]:


# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[5]:


# 保存到文件
wc.to_file('wordcloud.png')

