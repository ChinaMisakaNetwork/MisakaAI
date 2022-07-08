import torch
import torch.nn as nn
from torch import optim
from models import Model
from datasets import data_loader, TextCls
from configs import Config

if __name__ == '__main__':

    cfg = Config()
    data_path = "data/weibo_senti_100k.csv"
    data_stop_path = "data/hit_stopword"
    dict_path = "data/dict"

    dataset = TextCls(dict_path, data_path, data_stop_path, limit=1000)
    train_dataloader = data_loader(dataset, cfg)

    cfg.pad_size = dataset.max_len_seq
    print(cfg.pad_size)

    model_text_cls = Model(cfg)
    model_text_cls.to(cfg.devices)
    model_text_cls.load_state_dict(torch.load("models/10.pth"))

    for i, batch in enumerate(train_dataloader):
        label, data = batch
        data = torch.as_tensor(data).to(cfg.devices)
        label = torch.as_tensor(label, dtype=torch.int64).to(cfg.devices)
        pred_softmax = model_text_cls.forward(data)
        pred = torch.argmax(pred_softmax, dim=1)
        out = torch.eq(pred, label)
        print(len(out.tolist()) / pred.size()[0])  # 训练集上的准确率
    torch.cuda.empty_cache()  # 清显存
