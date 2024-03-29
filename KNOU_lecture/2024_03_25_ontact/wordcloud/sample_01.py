from wordcloud import WordCloud
import matplotlib.pyplot as plt

a = '저는 수학을 참 좋아합니다. 수학 문제를 풀 때 기분이 좋아요'

wordcloud = WordCloud(font_path="NanumGothicExtraBold.ttf", width=400, height=400, background_color="white")
wordcloud = wordcloud.generate(a)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
