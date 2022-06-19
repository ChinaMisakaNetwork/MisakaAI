import os.path

import jieba

from constants import UNK, PAD, MIN_SEQ, TOP_N, utf8

data_path = 'data/weibo_senti_100k.csv'  # read
stop_words_path = 'data/hit_stopword'  # read
dict_path = 'data/dict'  # write

if __name__ == '__main__':
    if os.path.exists(dict_path):
        print('The dictionary already exists.\nDo you want to rebuild it?(y/n)')
        i = input()
        if not i[0] in 'yY':
            exit(0)

    # 情感标签和评论
    data = open(data_path, encoding=utf8).readlines()[1:]
    # 停止词(出现频率非常高,但是对文章或页面的意义没有实质影响)
    stop_words = [word.strip() for word in open(stop_words_path, encoding=utf8).readlines()] + [' ', '\n']

    words_dict = {}  # 词频: {'词组': 频率}

    for item in data:
        label = item[0]
        content = item[2:].strip()
        content_words = jieba.cut(content)
        # res = []
        for word in content_words:
            if word in stop_words:
                continue
            # res.append(word)
            if word in words_dict.keys():
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        # print(res)

    # [('词组', 频率)]
    top_words_list = sorted([_ for _ in words_dict.items() if _[1] > MIN_SEQ], key=lambda x: x[1], reverse=True)[:TOP_N]
    # print(top_words_list)

    # {'词组': 排序}
    top_words_dict = {word_count[0]: idx for idx, word_count in enumerate(top_words_list)}
    top_words_dict.update({UNK: len(top_words_dict), PAD: len(top_words_dict) + 1})
    # print(top_words_dict)

    with open(dict_path, "w", encoding=utf8) as f:
        for item in top_words_dict.keys():
            f.writelines("{},{}\n".format(item, top_words_dict[item]))
