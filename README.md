# python 学习

## fastApi 学习
- [starlette](https://starlette.dev/)
- [pydantic](https://pydantic.dev/docs/)




## 版本
python = v3.12.6




## 启动项目
```bash
# 1. 创建虚拟环境（或者在编辑器里面创建）
python -m venv .venv

# 2. Mac/Linux 激活
source .venv/bin/activate

# 3. 激活后前面会出现 (venv)，再pip install即可
pip install xxx

# 4. 导出依赖清单
pip freeze > requirements.txt

# 别人部署一键安装所有依赖
# pip install -r requirements.txt

# 激活后再执行启动命令(每次重新打开编辑器，要先激活环境再执行启动命令)
uvicorn app.main:app --reload

# 查看当前版本
which python


# 运行docker
docker compose up -d
```

## 数据库迁移
aerich 是一个基于 tortoise 的数据库迁移工具。

### 初始化配置，只需要使用一次
```bash
# TORTOISE_ORM 配置的位置
# 因为 vscode 编辑器的原因, 搭建的虚拟环境的限制
# aerich init -t settings.TORTOISE_ORM

# 进入到工作的目录，采用以下的命令
/Users/yyp92/Desktop/code/project/python-fastApi/.venv/bin/aerich init -t settings.TORTOISE_ORM
```

> 初始化完会在当前的目录生成一个文件 `pyproject.toml` 和 一个文件夹 `migrations` 
> - `pyproject.toml` 保存配置文件路径，低版本可能是 `aerich.ini`。
> - `migrations` 存放迁移文件。


### 初始化数据库，一般情况下只用一次
```bash
# 进入到工作的目录，采用以下的命令
/Users/yyp92/Desktop/code/project/python-fastApi/.venv/bin/aerich init-db
```

> 此时数据库中就有相应的表格。
> 如果 `TORTOISE_ORM` 配置文件中的 `models` 改了名，则执行这条命令时需要增加 `--app` 参数，来指定你修改的名字。


### 更新模型并进行迁移
```bash
# 进入到工作的目录，采用以下的命令
# --name 可以指定迁移的名称，默认是当前时间戳
/Users/yyp92/Desktop/code/project/python-fastApi/.venv/bin/aerich migrate [--name]
```

> 注意：此时 sql 并没有执行，数据库中表中没有xxx字段。


### 重新执行迁移，写入数据库
```bash
# 进入到工作的目录，采用以下的命令
/Users/yyp92/Desktop/code/project/python-fastApi/.venv/bin/aerich upgrade
```


### 回到上一个版本
```bash
# 进入到工作的目录，采用以下的命令
/Users/yyp92/Desktop/code/project/python-fastApi/.venv/bin/aerich downgrade
```


### 查看历史迁移记录
```bash
# 进入到工作的目录，采用以下的命令
/Users/yyp92/Desktop/code/project/python-fastApi/.venv/bin/aerich history
```






## 遇到的问题
### 如果重新打开编辑器，提示导入的包无法解析导入
在项目的根目录配饰 .vscode/settings.json 文件。
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "code-runner.executorMap" : {
        "python" : "/Users/yyp92/Desktop/code/project/python-fastApi/.venv/bin/python -u"
    }
}
```



## 项目结构
```plaintext
fastapi_demo/
├── app/                           # 核心源码包（Python包）
│   ├── __init__.py
│   ├── main.py                    # 项目入口，创建FastAPI实例、注册路由、中间件
│   ├── core/                      # 核心基础组件
│   │   ├── __init__.py
│   │   ├── config.py              # 全局配置、读取环境变量
│   │   ├── security.py            # 鉴权、JWT、密码加密
│   │   └── exceptions.py          # 全局异常捕获、统一异常处理器
│   ├── api/                       # 路由接口层（路由蓝图拆分）
│   │   ├── __init__.py
│   │   ├── deps.py                # 依赖项：登录鉴权、公共依赖
│   │   ├── v1/                    # API版本管理（v1接口）
│   │   │   ├── __init__.py
│   │   │   ├── user.py            # 用户相关路由
│   │   │   └── file.py            # 文件相关路由
│   ├── schemas/                   # Pydantic模型：请求体、响应体DTO
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── common.py              # 通用返回模型
│   ├── crud/                      # 数据库CRUD操作（数据访问层）
│   │   ├── __init__.py
│   │   ├── base.py                # 基础通用CRUD封装
│   │   └── user.py
│   ├── models/                    # ORM数据库模型表结构(SQLAlchemy)
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/                  # 业务逻辑层（复杂业务编排）
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── db/                        # 数据库连接相关
│   │   ├── __init__.py
│   │   ├── session.py             # 数据库会话Session
│   │   └── base.py
│   └── utils/                     # 通用工具类
│       ├── __init__.py
│       ├── logger.py              # 日志封装
│       └── common.py              # 通用工具类
├── tests/                         # pytest单元/接口测试
│   ├── __init__.py
│   ├── conftest.py                # pytest配置文件：共享测试环境、数据库连接
│   └── test_api_user.py
├── scripts/                       # 脚本：数据库初始化、定时任务、迁移脚本
│   └── init_db.py
├── logs/                          # 日志文件目录
├── .env                           # 【本地开发环境】git忽略，自己本地用，本地venv读取的配置
├── .env.test                      # 测试环境配置
├── .env.prod                      # 正式环境配置（本地模拟线上使用）
├── .env.example                   # 模板！提交到git，不能填真实密码
├── Dockerfile                     # 线上使用，Dockerfile：构建Docker镜像
├── docker-compose.yml                # 公共基础compose配置
├── docker-compose.override.dev.yml   # 【本地开发专用】只启动 mysql、redis，**不启动api**
├── docker-compose.override.test.yml  # 测试环境覆盖配置
├── docker-compose.override.prod.yml  # 生产环境覆盖配置
├── .gitignore                     # Git忽略文件，避免提交敏感信息
├── pyproject.toml                 # 依赖、代码格式化配置
├── requirements.txt               # 依赖清单，用于pip install
├── README.md                      # 项目说明文档
```

| 环境 | FastAPI 运行位置 | docker-compose 作用 |
| ---- | ---- | ---- |
| dev 本地开发 | 本机 .venv | 仅启动 MySQL、Redis 等中间件 |
| test 测试服务器 | Docker 容器 | 完整集群：api + mysql + redis |
| prod 正式服务器 | Docker 容器 | 完整集群：api + mysql + redis |




## python 其他知识点
### Python 字符串前缀：`f` / `r` / `u` / `b`
| 前缀   | 名称                 | 作用                                                         |
| ------ | -------------------- | ------------------------------------------------------------ |
| `f""`  | 格式化字符串         | 解析 `{变量/表达式}`，做字符串插值                           |
| `r""`  | 原始 (raw) 字符串    | 关闭反斜杠`\`转义，`\`当作普通字符（正则、文件路径高频）     |
| `u""`  | Unicode 字符串       | 字面量是 unicode 文本，Python3 默认全部字符串就是 u 类型，几乎不用手写 |
| `b""`  | bytes 字节串         | 二进制字节，网络、数据库、socket 传输用，不是普通文本         |


### `*` 和 `**` 完整区别
|符号|使用位置|作用|接收/产出类型|
|---|---|---|---|
|`*`|**调用函数** `func(*seq)`|把列表/元组拆开，作为多个位置参数传入|序列 → 多个位置参数|
|`**`|**调用函数** `func(**dict)`|把字典拆开，作为多个关键字参数传入|字典 → 多个key=value参数|
|`*args`|**定义函数** `def fn(*args)`|收集全部多余位置参数，打包成元组|多个位置参数 → tuple元组|
|`**kwargs`|**定义函数** `def fn(**kwargs)`|收集全部多余关键字参数，打包成字典|多个key=value参数 → dict字典|


