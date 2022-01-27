from utils import *
from config import all_project_tfidf_token
from config import top10

# Basic information
def output(project_number):
    project_id = df['系統編號'][project_number]
    project_year = df['年度'][project_number]
    print('-------------------------------------------------------------')
    print(f'系統編號: {project_id}')
    print(f'年份: {project_year}')
    description = df['計畫重點描述'][project_number]
    description = description.replace('_x000D_', '')
    print(description)
    # take description to tokenize
    tmp_tokenize = tokenize(description)
    tokenize_result = []
    for word in tmp_tokenize:
        if ((word not in all_project_tfidf_token) and (word not in top10)):
            tokenize_result.append(word)
    stat_wordcloud(tokenize_result)
    description = ''.join(tokenize_result)
    # doing tf-idf
    tf_idf(description)


if __name__ == '__main__':
# 針對各年度計畫作tf-idf分析
    df = load_file('data.xlsx')
    # total number of projects
    sum = len(df)
    
    project_number = 1000
    output(project_number)
    
