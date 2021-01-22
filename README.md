# 项目介绍
本平台是一个机器人的调度中心，拥有各种各样的机器人实例，对各种机器人的API进行封装，并拟加入定时任务。


# 项目结构
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

# 数据库设计
拟创建三张表，bot、日志、定时任务


# TODO
- [ ] 定时任务
- [ ] API设计
- [ ] 数据库设计
- [ ] 流程设计
- [ ] CRUD
