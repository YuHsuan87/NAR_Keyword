import pandas as pd
import jieba
import jieba.analyse
import openpyxl
from tqdm import tqdm
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from config import all_project_tfidf_token
from config import top10
import re


def load_file(file_name):
    print('Data load.....')
    df = pd.read_excel(file_name)
    num = len(df)
    print(f'共 {num} 項')
    return df

def is_not_number(str):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(str)
    if result:
        return False
    else:
        return True

def cut_stopword(seq_list):
    filepath = 'stopword.txt'
    stopwordlist = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]

    result = []
    for word in seq_list:
        if((word not in stopwordlist) and (word != '\n') and (word != '\t')
                                            and (word != ' ') and is_not_number(word)):
            result.append(word)
    return result

def tokenize(string):
    # print(string)
    result = jieba.cut(string, cut_all=False, HMM=True)
    # add word
    addword_list = ['臺灣', '農作物', '物種', '系統']
    for word in addword_list:
        jieba.add_word(word)
    
    # print('|'.join(result))
    seq_list = jieba.lcut(string)
    # print(seq_list)
    # print('-----------------------------------------------------------------')

    # cut stopword and whitespace
    cut_result = cut_stopword(seq_list)
    return cut_result

def cut_common_word(token):
    tokenize_result = []
    for word in token:
        if ((word not in all_project_tfidf_token) and (word not in top10)):
            tokenize_result.append(word)
    return tokenize_result

def tf_idf(string):
    tags = jieba.analyse.extract_tags(string, topK = 8, withWeight = True)
    for tag in tags:
        print('| {} | {:.6f} |'.format(tag[0], tag[1]))
        # print(' {} |'.format(tag[0]), end = '')
    print()
    return tags

# draw wordcloud
def stat_wordcloud(token_list):
    dic = {}
    for key in token_list:
        if key not in dic:
            dic[key] = 1
        else:
            dic[key] += 1
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
    top10 = top_10(dic)
    wc = WordCloud(scale = 2,
                    max_font_size = 100,
                    font_path = 'SourceHanSansCN-Regular.otf',  # 中文字體
                    background_color = 'white',
                    collocations= False, # 字詞重不重複
                )
    token_str = ' '.join(token_list)
    wc.generate(token_str)
    plt.imshow(wc, interpolation='bilinear') 
    plt.axis('off') 
    plt.tight_layout() 
    plt.show()
    return top10

# top10 token quantity
def top_10(sorted_dic):
    top10 = []
    count = 0
    # print(sorted_dic) 
    for key, value in sorted_dic.items():
        print(f'| {key} | {value} |')
        top10.append(key)
        count += 1 
        if count == 10:
            break
    return top10

def cut_row(string):
    return string.replace('_x000D_', '')

if __name__ == '__main__':
    df = load_file('data.xlsx')
    sum = len(df['系統編號'])
    final_token = []
    final_string = ''
    for i in tqdm(range(sum)):
        project_number = df['系統編號'][i]
        # print(f'系統編號:{project_number}')
        string = df['計畫重點描述'][i]
        string = string.replace('_x000D_', '')
        
        method = 2
        # tokenize
        if method == 0:
            tokenize(string)
        # tf-idf
        elif method == 1:
            tf_idf(string)
        # do all
        elif method == 2:
            temp_tokenlist = tokenize(string)
            final_token += temp_tokenlist
            final_string += string
        else:
            print('Tokenize:')
            tokenize(string)
            print('tf-idf:')
            tf_idf(string)

    # print(final_token)
    tf_idf(final_string)
    

    