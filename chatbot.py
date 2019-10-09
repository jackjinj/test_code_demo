import jieba
import numpy as np
from flask import Flask
from sklearn.metrics.pairwise import cosine_similarity

word_vector_list = ["我们","来","贪心","学院","学习","人工智能","和","Python","课程","助教","基础","开始","哪个","周期","方式","什么","优势","有效期","优惠"]
question_answer = {"Python课程是线上课程还是线下课程":"线上课程为主","Python课程有助教吗":"为提高服务效率和质量，课程都配备专业的全职助教","我没有基础应该从哪个课开始学":"周老师的Python基础集训营非常适合你哦，可以在这里学习","Python的学习周期是多久":"如果你没有基础的话两个月可以搞定","Python课程的学习方式是什么呢？":"无需安装环境，在线直接写代码、看视频、看漫画，趣味性学习","Python课程的优势是什么呢？":"全网覆盖最全的Python基础知识体系\
练与学的深度结合，每一个知识点都配有练习项目\
生动有趣、授课方式多样，视频、文字、图片、在线代码编辑，在聊天与娱乐中学习"," Python课程的有效期是多久呢？":"我们把有效期确定为1年，1年内可无限次学习","Python课程有优惠吗？":"我们定价为开课后是599，现在是针对老学员预售199，开课后恢复原价"}

def get_vector(data):
  vector_list = []
  for i in word_vector_list:
    if i in list(jieba.cut(data)):
      vector_list.append(1)
    else:
      vector_list.append(0)
  return np.array(vector_list).reshape(1,-1)

app=Flask(__name__)
@app.route('/greedyai/<question>')
def hellow_world(question):
    question_vector = get_vector(question)
    final_result = 0
    for key in question_answer.keys():
      key_vector = get_vector(key)
      result = cosine_similarity(question_vector,key_vector)
      if result > final_result:
        final_result = result
        answer = question_answer[key]
    print(answer)
    return answer

if __name__=='__main__':
    app.run()
