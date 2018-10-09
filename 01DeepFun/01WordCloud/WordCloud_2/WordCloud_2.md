

```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud
```


```python
# 打开文本
text = open('xyj.txt').read()
# 生成对象
wc = WordCloud(font_path='Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)
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
wc.to_file('wordcloud_2.png')
```




    <wordcloud.wordcloud.WordCloud at 0x110a84828>


