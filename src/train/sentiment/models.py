import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class Model(nn.Module):
    def __init__(self, config):
        super(Model, self).__init__()
        self.embeding = nn.Embedding(config.n_vocab,  # 字典大小
                                     config.embed_size,  # 词向量长度
                                     padding_idx=config.n_vocab - 1,  # 词的索引
                                     )
        # RNN-LSTM的输入是embeding的输出
        self.lstm = nn.LSTM(config.embed_size,
                            config.hidden_size,
                            config.num_layers,  # LSTM数量
                            bidirectional=True,  # 双向LSTM
                            batch_first=True,
                            dropout=config.dropout,  # 随机抑制节点防止过拟合
                            )

        # 卷积网络
        self.maxpool = nn.MaxPool1d(config.pad_size)
        # FC线性层
        self.fc = nn.Linear(config.hidden_size * 2 + config.embed_size,  # 输入数量
                            config.num_classes,  # 输出: 要预测的类别数量
                            )
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        embed = self.embeding(x)  # [batchsize, seqlen, embed_size]
        out, _ = self.lstm(embed)
        out = torch.cat((embed, out), 2)
        out = F.relu(out)  # relu层, 增加非线性表达能力
        out = out.permute(0, 2, 1)  # 交换维度
        out = self.maxpool(out).reshape(out.size()[0], -1)  # reshape转为二维
        out = self.fc(out)
        out = self.softmax(out)
        return out


if __name__ == '__main__':
    from configs import Config

    cfg = Config()
    cfg.pad_size = 640
    model = Model(config=cfg)
    input_tensor = torch.tensor([i for i in range(640)]).reshape([1, 640])
    out_tensor = model.forward(input_tensor)
    print(out_tensor.size())
    print(out_tensor)
