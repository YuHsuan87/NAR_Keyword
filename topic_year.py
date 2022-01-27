from utils import *

if __name__ == '__main__':
    df = load_file('data.xlsx')
    topics = ['主題1', '主題2', '主題3']
    years = [i for i in range(103,111)]

    topic_index = {}
    for topic in topics:
        topic_index[topic] = []
        for j in range(len(df)):
            if(pd.isna(df[topic][j])):
                continue
            else:
                topic_index[topic].append(j)

    # print(topic_index)
    num = 0
    for key, indexs in topic_index.items():
        print(key + ':')
        for year in years:
            token = []
            print(f'{year} 年度:')
            for index in indexs:
                if(df['年度'][index] == year):
                    tmp_string = df['計畫重點描述'][index].replace('_x000D_', '')
                    token += cut_common_word(tokenize(tmp_string))
            result_string = ''.join(token)
            tf_idf(result_string)
            
            