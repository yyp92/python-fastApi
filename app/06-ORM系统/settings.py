TORTOISE_ORM = {
    "connections": {
        "default": {
            # 数据库引擎
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "admin",
                "database": "fastapi",
                "minsize": 1,
                "maxsize": 5,
                "charset": "utf8mb4",
                "echo": True,
            }
        }
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai",
}