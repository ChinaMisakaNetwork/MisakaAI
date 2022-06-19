from torch.utils.data import Dataset, DataLoader
import jieba
import numpy as np

from constants import UNK, PAD, MIN_SEQ, TOP_N, utf8


def read_dict(dict_path: str):
    words_dict = {}
    words_dict_list = open(dict_path, encoding=utf8).readlines()
    for item in words_dict_list:
        k, v = item.split(',')
        words_dict[k] = int(v.strip())
    return words_dict


def load_data(data_path: str, stop_words_path: str, n: int = None):
    data = open(data_path, encoding=utf8).readlines()[1:]
    stop_words = [word.strip() for word in open(stop_words_path, encoding=utf8).readlines()] + [' ', '\n']
    np.random.shuffle(data)

    max_len_seq = 0  # 最长的句子的长度. 以此为分界线
    res = []
    n = len(data) if n is None else n
    for item in data[:n]:
        label = item[0]
        content = item[2:].strip()
        content_words = jieba.cut(content, cut_all=False)
        this_res = []
        for word in content_words:
            if word in stop_words:
                continue
            this_res.append(word)

        if len(this_res) > max_len_seq:
            max_len_seq = len(this_res)
        res.append([label, this_res])

    return res, max_len_seq


class TextCls(Dataset):
    def __init__(self, dict_path, data_path, stop_words_path, max_len_seq=None):
        self.words_dict = read_dict(dict_path)  # 词频字典
        self.data_path = data_path  # 待分类数据
        self.stop_words_path = stop_words_path  # 停止词
        self.data, self.max_len_seq = load_data(self.data_path, self.stop_words_path, 1000)  # 加载数据
        if max_len_seq is not None:
            self.max_len_seq = max_len_seq  # 最长的句子的长度. 以此为分界线

        np.random.shuffle(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        data = self.data[item]
        label = int(data[0])  # 情感标签
        words = data[1]

        input_idx = []
        for word in words:
            input_idx.append(self.words_dict.get(word, self.words_dict[UNK]))
        if len(input_idx) < self.max_len_seq:
            input_idx += [self.words_dict[PAD] for _ in range(self.max_len_seq - len(input_idx))]
        res = np.array(input_idx)

        return label, res


def new_data_loader(dict_path, data_path, stop_words_path):
    dataset = TextCls(dict_path, data_path, stop_words_path)
    return DataLoader(dataset, batch_size=10, shuffle=True)


if __name__ == '__main__':
    input_data_path = 'data/weibo_senti_100k.csv'
    input_stop_words_path = 'data/hit_stopword'
    input_dict_path = 'data/dict'
    train_data_loader = new_data_loader(input_dict_path, input_data_path, input_stop_words_path)
    for i, batch in enumerate(train_data_loader):
        print(batch)
