from cProfile import label
from unittest import result
from utils import *
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

def draw(year_word_dict, years):
    plt.xlabel('years')
    plt.ylabel('tf-idf')
    for key, val in year_word_dict.items():
        if(key == '數位' or key == '智慧' or key == '5G'):
            plt.plot(years, val, label = key, linestyle="--")
    font = FontProperties(fname='SourceHanSansCN-Regular.otf')
    plt.legend(bbox_to_anchor=(1.02, 0.7, 0.2, 0.3), loc='upper left', 
                    prop = font, fontsize = 90)
    plt.show()

if __name__ == '__main__':
    df = load_file('data.xlsx')
    years = [i for i in range(103,111)]
    year_word = {}
    for year in years:
        string = ''
        for i in range(len(df)):
            if(df['年度'][i] == year):
                string += df['計畫重點描述'][i].replace('_x000D_', '')

        cut_result = tokenize(string)
        result_string = ''.join(cut_common_word(cut_result))
        print(f'年度:{year}')
        tags = tf_idf(result_string)
        for tag in tags:
            if(tag[0] not in year_word):
                year_word[tag[0]] = []
            #     year_word[tag[0]].append(tag[1])
            # else:
            #     year_word[tag[0]].append(tag[1])
    count = 1
    for year in years:
        string = ''
        for i in range(len(df)):
            if(df['年度'][i] == year):
                string += df['計畫重點描述'][i].replace('_x000D_', '')

        cut_result = tokenize(string)
        result_string = ''.join(cut_common_word(cut_result))
        print(f'年度:{year}')
        tags = tf_idf(result_string)
        for tag in tags:
            if tag[0] in year_word:
                year_word[tag[0]].append(tag[1])
        for key, val in year_word.items():
            if(len(val)!= count):
                year_word[key].append(0)
        count += 1 
        
    final_year = {}
    for key, val in year_word.items():
        if(len(val) == 8):
            final_year[key] = val
    # print(final_year)
    draw(final_year, years)

    
        
    