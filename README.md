# 一、项目介绍
本平台是一个机器人的调度中心，拥有各种各样的机器人实例，对各种机器人的API进行封装，并拟加入定时任务。


# 二、项目结构
```
├── Dockerfile
├── LICENSE
├── README.md
├── __init__.py
├── app
│   ├── __init__.py
│   └── app.py              # Web入口
├── bots                    # 机器人实现
│   ├── __init__.py
│   ├── dingbot.py          # 钉钉机器人实现
│   ├── telebot.py          # 电报机器人实现
│   └── wxbot.py            # 微信机器人实现
├── data                    # 数据文件，如sqlite数据库位置，需挂载出去
├── docker-compose.yaml     # 可直接启动docker-compose
├── requirements.txt        # 依赖包维护
├── services                # 机器人服务
├── setup.py                # 打包用文件
├── sql
│   └── db.sql              # 数据库建表时依赖
├── templates               # 模板，用于存放静态资源
│   └── home.html           # 主页
├── tests                   # 测试类
└── utils                   # 工具类
    ├── __init__.py
    └── db_util.py          # sqlite数据库访问模块
```

# 三、数据库设计
拟创建三张表，bot、日志、定时任务
拟创建tag表

## 1. bot表
bot表为记录bot的所有信息的表, 需要ID, chatID（telegrambot用）, secret（dingbot用）

| 字段    | 类型      | 备注                         |
| ------- | --------- | ---------------------------- |
| id      | number(5) |                              |
| name    | text(7)   | 机器人的简称                 |
| type    | number(1) | 0: 企业微信, 1: 钉钉, 2 电报 |
| token   | text(64)  | 机器人的访问Token            |
| chat_id | text(32)  | telegram用chat_id            |
| secret  | text(67)  | ding用secret                 |

## 2. user表


# 四、接口设计
## 1. BOT接口

| 接口名          | 接口参数                                    | 接口返回值   | 描述             |
| --------------- | ------------------------------------------- | ------------ | ---------------- |
| add_bot         | bot_type,bot_token,chat_id=None,secret=None | 插入的bot_id | 添加机器人接口   |
| delete_bot      | bot_id                                      | 删除是否成功 | 删除机器人的接口 |
| update_bot      | bot_id                                      | 修改后的bot  | 更新bot的数据    |
| get_bot         | bot_id                                      | 修改后的bot  | 更新bot的数据    |
| get_bots        | 没有                                        | [bots]       | 获取所有bot    |
| get_bot_by_user | user_id                                     | [bots]       | 查询bot数据      |



# 五、 页面设计

![平台](README.assets\首页.png)
![平台](README.assets\bot页.png)

# TODO

- [ ] 定时任务
- [ ] API设计
- [ ] 数据库设计
- [ ] 流程设计
- [ ] CRUD
