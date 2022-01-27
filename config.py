from typing import final
from utils import *


all_project_tfidf_token = ['技術', '發展', '計畫', '產業', '應用', '推動', '服務',
                                                         '研發', '創新', '系統']

top10 = ['技術', '發展', '研究', '計畫', '產業', '推動', '服務', '科技', '建立', '整合']

dup_list = list(set(all_project_tfidf_token).intersection(top10))

# df = load_file('data.xlsx')
# sum = len(df)

# -------------------------total tfidf---------------------------------------
# final_string = ''
# for i in range(sum):
#     string = df['計畫重點描述'][i]
#     string = string.replace('_x000D_', '')
#     final_string += string

# tags = tf_idf(final_string)

# # 3152 projects tf-idf top10 token
# all_project_tfidf_token = []
# for key, val in tags:
#     all_project_tfidf_token.append(key)

# print(all_project_tfidf_token)


# -------------------------total token---------------------------------------
# final_string = ''
# for i in range(sum):
#     string = df['計畫重點描述'][i]
#     string = string.replace('_x000D_', '')
#     final_string += string

# cut_result = tokenize(final_string)
# top10 = stat_wordcloud(cut_result)

