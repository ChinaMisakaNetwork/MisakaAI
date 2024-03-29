import torch
import torch.nn as nn
from torch import optim
from models import Model
from datasets import TextCls, data_loader
from configs import Config

if __name__ == '__main__':
    cfg = Config()

    data_path = 'data/weibo_senti_100k.csv'
    data_stop_path = 'data/hit_stopword'
    dict_path = 'data/dict'
    dataset = TextCls(dict_path, data_path, data_stop_path)
    train_dataloader = data_loader(dataset, cfg)

    cfg.pad_size = dataset.max_len_seq
    print(cfg.pad_size)

    model_text_cls = Model(cfg)
    model_text_cls.to(cfg.devices)
    loss_func = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model_text_cls.parameters(), lr=cfg.learn_rate)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer,
                                                step_size=1,
                                                gamma=0.9)

    for epoch in range(cfg.num_epochs):
        for i, batch in enumerate(train_dataloader):
            label, data = batch
            data = torch.as_tensor(data).to(cfg.devices)
            label = torch.as_tensor(label, dtype=torch.int64).to(cfg.devices)

            optimizer.zero_grad()
            pred = model_text_cls.forward(data)
            loss_val = loss_func(pred, label)

            # print(pred)
            # print(label)
            print("epoch is {}, ite is {}, val is {}".format(epoch, i, loss_val))
            loss_val.backward()
            optimizer.step()

        scheduler.step()
        if epoch % 10 == 0:
            torch.save(model_text_cls.state_dict(), "models/{}.pth".format(epoch))

    torch.cuda.empty_cache()  # 清显存
