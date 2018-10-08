

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
```


```python
# 打开文本
text = open('constitution.txt').read()
# 生成对象
wc = WordCloud().generate(text)
```


```python
# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
```


![png](output_2_0.png)



```python
# 保存到文件
wc.to_file('wordcloud.png')
```




    <wordcloud.wordcloud.WordCloud at 0x10511dcc0>


