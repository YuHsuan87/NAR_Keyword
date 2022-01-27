from utils import *
from tqdm import tqdm
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from itertools import combinations


# tags = topic_tf_idf
def duplicate_keyword(topic_keyword_list):
    duplicate_result = []
    num = list(combinations("012",2))
    for i, j in num:
        i, j = int(i), int(j)
        duplicate_result.append(list(set(topic_keyword_list[i]).intersection(
                                                        topic_keyword_list[j])))
    result = list(set(duplicate_result[0]).union(duplicate_result[1], 
                                                        duplicate_result[2]))
    return result
        

if __name__ == '__main__' :
    df = load_file('data.xlsx')
    topic_keyword_list = []
    topics = ['主題1', '主題2', '主題3']
    # find topic
    for topic in topics:
        topic_sum = len(df[df[topic].notnull()])
        topic_index = df[df[topic].notnull()].index
        print(topic)
        topic_string = ''
        topic_token = []
        for index in topic_index:
            string = df[df[topic].notnull()]['計畫重點描述'][index]
            string = string.replace('_x000D_', '')
            topic_token += cut_common_word(tokenize(string))
            # string to tf-idf
            # print(topic_token)
            topic_string = ''.join(topic_token)

            # string to tokenize
            # topic_token += tokenize(string)

        stat_wordcloud(topic_token)

        # result
        tags = tf_idf(topic_string)
        # only need keyword
        tmp_keyword = []
        for key, value in tags:
            tmp_keyword.append(key)
        topic_keyword_list.append(tmp_keyword)

    # duplicate keyword
    duplicate_result = duplicate_keyword(topic_keyword_list)
    print(duplicate_result)
    # non_duplicate keyword
    non_duplicate_result = []
    for i in range(3):
        for key in topic_keyword_list[i]:
            if key not in duplicate_result:
                non_duplicate_result.append(key)
    print(non_duplicate_result)
    
