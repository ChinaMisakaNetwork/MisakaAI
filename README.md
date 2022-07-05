# MisakaAI

御坂网络AI模块 - 让御坂 (以及更多角色) 从动漫里走出来

## 设计文档

递进的分为三个部分, 模型训练, 模型推理, 应用前端

### 模型训练

- [ ] 情感分析模型
- [ ] 机器翻译模型
- [ ] 互动聊天模型

#### 语料获取

- [x] 开源聊天语料库: [chinese_chatbot_corpus](https://github.com/codemayq/chinese_chatbot_corpus)
- [x] 情感语料库: [ChineseNlpCorpus](https://github.com/SophonPlus/ChineseNlpCorpus)
- [x] 中文维基百科语料：[wikimedia](https://github.com/misaka-10031/wikipedia-to-zh-cn)
- [ ] 魔禁聊天语料库: 对魔禁小说做加工, 制作成语料库(working)

#### 数据处理

TODO

#### 模型建立

1.bot人格设定
2.敏感词处理
3.文本检索模型的使用
4.文本生成模型的使用
5.回答打分机制
6.万能回答/不回答的使用策略
7.多媒体消息的处理
等

### 模型推理

暂定 [ncnn](https://github.com/Tencent/ncnn) 框架

### 应用前端

- [ ] 服务端: QQ群机器人 ([御坂网络Mirai_bot](https://github.com/ChinaMisakaNetwork/Mirai_Bot))
- [ ] 移动/PC端: 动态桌面 / 游戏角色AI

### 相关教程信息

<https://zhuanlan.zhihu.com/p/166199114>
