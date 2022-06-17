# MisakaAI
御坂网络AI模块 - 让御坂 (以及更多角色) 从动漫里走出来

(以当前时代的技术而看, 只有NLP部分, 就连CV都很悬, 等机器人CV更成熟吧)

## 设计文档
递进的分为三个部分, 模型训练, 模型推理, 应用前端

### 模型训练
- 情感分析模型
- 机器翻译模型
- 互动聊天模型

#### 语料获取
1. 开源语料库 [chinese_chatbot_corpus](https://github.com/codemayq/chinese_chatbot_corpus) 
2. 处理魔禁小说, 将其制作为魔禁语料库

#### 数据处理
TODO

#### 模型建立
TODO

### 模型推理
暂定 [ncnn](https://github.com/Tencent/ncnn) 框架

### 应用前端
- 服务端: QQ群机器人 (暂定 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp))
- 移动/PC端: 动态桌面 / 游戏角色AI
